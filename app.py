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

menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "KI Import (PDF/Foto)"])

if menu == "Rezepte ansehen":
    if not st.session_state.recipes:
        st.info("Noch keine Rezepte vorhanden. Nutze den KI-Import!")
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
    uploaded_file = st.file_uploader("Datei wählen", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        if st.button("Analyse starten"):
            with st.spinner("KI liest die Datei..."):
                try:
                    # Temporär speichern mit richtiger Endung für Mime-Type Erkennung
                    file_extension = os.path.splitext(uploaded_file.name)[1]
                    temp_path = f"temp_upload{file_extension}"
                    
                    with open(temp_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Datei hochladen
                    sample_file = genai.upload_file(path=temp_path)
                    
                    # Warten bis verarbeitet
                    while sample_file.state.name == "PROCESSING":
                        time.sleep(1)
                        sample_file = genai.get_file(sample_file.name)

                    # Wir nutzen hier den 'latest' Namen für maximale Kompatibilität
                    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
                    
                    prompt = (
                        "Extrahiere das Rezept als JSON. "
                        "Format: {'name': '...', 'Zutaten': ['...'], 'Werkzeuge': ['...'], 'Anleitung': ['...']}"
                    )
                    
                    response = model.generate_content([sample_file, prompt])
                    
                    # JSON Text säubern
                    json_text = response.text.strip()
                    if "```json" in json_text:
                        json_text = json_text.split("```json")[1].split("```")[0]
                    elif "```" in json_text:
                        json_text = json_text.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(json_text.strip())
                    
                    st.success("Rezept erkannt!")
                    new_name = st.text_input("Name:", value=recipe_data.get("name", "Neues Rezept"))
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])))
                    with c2:
                        werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                    
                    anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])))
                    
                    if st.button("In App speichern"):
                        st.session_state.recipes[new_name] = {
                            "Zutaten": zutaten.split("\n"),
                            "Werkzeuge": werkzeuge.split(","),
                            "Anleitung": anleitung.split("\n")
                        }
                        st.balloons()
                    
                    os.remove(temp_path)
                    
                except Exception as e:
                    st.error(f"Fehler: {e}")
