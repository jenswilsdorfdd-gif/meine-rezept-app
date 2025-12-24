import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import json
from PIL import Image
import io

# KI Konfiguration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
else:
    st.error("API Key fehlt!")

if 'recipes' not in st.session_state:
    st.session_state.recipes = {}

st.set_page_config(page_title="KI Rezept-App", layout="wide")
st.title("🤖 Rezept-App (liest jetzt auch Scans & Fotos)")

menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "KI Import (PDF/Foto)"])

if menu == "Rezepte ansehen":
    if not st.session_state.recipes:
        st.info("Noch keine Rezepte vorhanden.")
    else:
        name = st.selectbox("Wähle ein Rezept:", list(st.session_state.recipes.keys()))
        r = st.session_state.recipes[name]
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛒 Zutaten")
            for z in r["Zutaten"]: st.write(f"- {z}")
        with col2:
            st.subheader("🛠 Hilfsmittel")
            for w in r["Werkzeuge"]: st.write(f"- {w}")
        st.subheader("👨‍🍳 Zubereitung")
        for i, step in enumerate(r.get("Anleitung", []), 1):
            st.write(f"**{i}.** {step}")

elif menu == "KI Import (PDF/Foto)":
    st.subheader("📄 Upload: PDF oder Foto vom Rezept")
    # Erlaubt jetzt auch Bilder!
    uploaded_file = st.file_uploader("Datei wählen (PDF, JPG, PNG)", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        with st.spinner("KI liest das Rezept..."):
            try:
                content_to_send = []
                
                if uploaded_file.type == "application/pdf":
                    # Versuche Text zu lesen
                    reader = PdfReader(uploaded_file)
                    text = "".join([p.extract_text() for p in reader.pages])
                    if text.strip():
                        content_to_send.append(f"Extrahiere Rezept-JSON aus diesem Text: {text}")
                    else:
                        st.warning("Gescannte PDF erkannt. Tipp: Mache lieber ein Foto oder einen Screenshot vom Rezept!")
                        # Für echte Scans in PDFs bräuchten wir ein Zusatztool. 
                        # Einfacher Workaround: Der User lädt ein Bild hoch.
                else:
                    # Es ist ein Bild!
                    img = Image.open(uploaded_file)
                    content_to_send = ["Extrahiere das Rezept aus diesem Bild. Antworte NUR mit JSON: {'name': '...', 'Zutaten': ['...'], 'Werkzeuge': ['...'], 'Anleitung': ['...']}", img]

                if content_to_send:
                    response = model.generate_content(content_to_send)
                    raw_res = response.text
                    if "```json" in raw_res:
                        raw_res = raw_res.split("```json")[1].split("```")[0]
                    elif "```" in raw_res:
                        raw_res = raw_res.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(raw_res.strip())
                    st.success("Erkannt!")
                    
                    final_name = st.text_input("Name:", value=recipe_data.get("name", "Neues Rezept"))
                    c1, c2 = st.columns(2)
                    with c1:
                        final_zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])))
                    with c2:
                        final_werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                    final_anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])))
                    
                    if st.button("Speichern"):
                        st.session_state.recipes[final_name] = {
                            "Zutaten": final_zutaten.split("\n"),
                            "Werkzeuge": final_werkzeuge.split(","),
                            "Anleitung": final_anleitung.split("\n")
                        }
                        st.balloons()
            except Exception as e:
                st.error(f"Fehler: {e}")
