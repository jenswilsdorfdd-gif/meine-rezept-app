import streamlit as st
import google.generativeai as genai
import json
import time
import os

# 1. KI Konfiguration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key fehlt! Bitte in den Streamlit Secrets unter 'GEMINI_API_KEY' eintragen.")

# Datenbank initialisieren
if 'recipes' not in st.session_state:
    st.session_state.recipes = {}

st.set_page_config(page_title="KI Rezept-App", layout="wide")
st.title("👨‍🍳 Deine intelligente Rezept-App")

# --- MODELL-DETEKTOR ---
# Wir suchen automatisch nach dem richtigen Namen für das Flash-Modell
@st.cache_resource
def get_working_model():
    try:
        for m in genai.list_models():
            # Wir suchen ein Modell, das Inhalte generieren kann und "flash" im Namen hat
            if 'generateContent' in m.supported_generation_methods:
                if 'gemini-1.5-flash' in m.name:
                    return m.name
        return "models/gemini-1.5-flash" # Fallback, falls die Liste leer ist
    except Exception as e:
        return f"Fehler bei Modellsuche: {e}"

selected_model = get_working_model()

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
            for z in r.get("Zutaten", []): st.write(f"- {z}")
        with col2:
            st.subheader("🛠 Hilfsmittel")
            for w in r.get("Werkzeuge", []): st.write(f"- {w}")
        st.subheader("👨‍🍳 Zubereitung")
        for i, step in enumerate(r.get("Anleitung", []), 1):
            st.write(f"**{i}.** {step}")

elif menu == "KI Import (PDF/Foto)":
    st.subheader("📄 Lade ein PDF oder ein Foto hoch")
    # Hier zeigen wir an, welchen Namen die App gefunden hat
    st.info(f"Verbunden mit KI-Modell: {selected_model}")
    
    uploaded_file = st.file_uploader("Datei wählen", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        if st.button("Analyse starten"):
            with st.spinner("KI liest die Datei..."):
                try:
                    # Datei temporär speichern
                    file_ext = os.path.splitext(uploaded_file.name)[1]
                    temp_path = f"temp_upload{file_ext}"
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Datei hochladen
                    sample_file = genai.upload_file(path=temp_path)
                    while sample_file.state.name == "PROCESSING":
                        time.sleep(1)
                        sample_file = genai.get_file(sample_file.name)

                    # KI Anfrage mit dem ERKANNTEN Modellnamen
                    model = genai.GenerativeModel(model_name=selected_model)
                    prompt = "Extrahiere das Rezept als JSON: {'name': '...', 'Zutaten': ['...'], 'Werkzeuge': ['...'], 'Anleitung': ['...']}"
                    
                    response = model.generate_content([sample_file, prompt])
                    
                    # JSON extrahieren
                    res_text = response.text
                    if "```json" in res_text:
                        res_text = res_text.split("```json")[1].split("```")[0]
                    elif "```" in res_text:
                        res_text = res_text.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(res_text.strip())
                    st.success("Rezept erkannt!")
                    
                    new_name = st.text_input("Name:", value=recipe_data.get("name", "Neues Rezept"))
                    c1, c2 = st.columns(2)
                    with c1:
                        final_zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])))
                    with c2:
                        final_werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                    final_anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])))
                    
                    if st.button("Speichern"):
                        st.session_state.recipes[new_name] = {
                            "Zutaten": final_zutaten.split("\n"),
                            "Werkzeuge": final_werkzeuge.split(","),
                            "Anleitung": final_anleitung.split("\n")
                        }
                        st.balloons()
                    
                    os.remove(temp_path)
                except Exception as e:
                    st.error(f"Fehler: {e}")
