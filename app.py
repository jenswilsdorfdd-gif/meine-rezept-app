import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import json

# KI Konfiguration
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Wir definieren das Modell hier explizit
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    except Exception as e:
        st.error(f"Fehler bei der KI-Konfiguration: {e}")
else:
    st.error("API Key fehlt! Bitte in den Streamlit Secrets hinterlegen.")

# Datenbank initialisieren
if 'recipes' not in st.session_state:
    st.session_state.recipes = {}

st.set_page_config(page_title="KI Rezept-App", layout="wide")
st.title("🤖 Rezept-App mit KI-Import")

menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "KI PDF-Import"])

if menu == "Rezepte ansehen":
    if not st.session_state.recipes:
        st.info("Noch keine Rezepte vorhanden. Nutze den KI-Import!")
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

elif menu == "KI PDF-Import":
    st.subheader("📄 Automatischer Import via Gemini KI")
    uploaded_file = st.file_uploader("PDF hochladen", type="pdf")
    
    if uploaded_file:
        with st.spinner("KI analysiert das Rezept..."):
            try:
                # Text aus PDF extrahieren
                reader = PdfReader(uploaded_file)
                text_content = ""
                for page in reader.pages:
                    text_content += page.extract_text() + "\n"
                
                if not text_content.strip():
                    st.error("Das PDF scheint keinen lesbaren Text zu enthalten (vielleicht ein Scan?).")
                else:
                    # Die KI-Anfrage
                    prompt = (
                        "Extrahiere das Rezept aus folgendem Text. "
                        "Antworte NUR mit einem validen JSON-Objekt. "
                        "Struktur: {\"name\": \"...\", \"Zutaten\": [\"...\"], \"Werkzeuge\": [\"...\"], \"Anleitung\": [\"...\"]} "
                        f"Hier ist der Text: {text_content}"
                    )
                    
                    response = model.generate_content(prompt)
                    
                    # JSON-Teil aus der Antwort fischen
                    raw_res = response.text
                    if "```json" in raw_res:
                        raw_res = raw_res.split("```json")[1].split("```")[0]
                    elif "```" in raw_res:
                        raw_res = raw_res.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(raw_res.strip())
                    
                    st.success("Analyse erfolgreich!")
                    
                    # Bearbeitbare Felder anzeigen
                    final_name = st.text_input("Name:", value=recipe_data.get("name", "Neues Rezept"))
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        final_zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])))
                    with c2:
                        final_werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                    
                    final_anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])))
                    
                    if st.button("Rezept speichern"):
                        st.session_state.recipes[final_name] = {
                            "Zutaten": final_zutaten.split("\n"),
                            "Werkzeuge": final_werkzeuge.split(","),
                            "Anleitung": final_anleitung.split("\n")
                        }
                        st.balloons()
                        st.success("Gespeichert!")
            
            except Exception as e:
                st.error(f"Da ist etwas schiefgelaufen: {e}")
                st.info("Tipp: Manchmal hilft es, das PDF noch einmal hochzuladen.")
