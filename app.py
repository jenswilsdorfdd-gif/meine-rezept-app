import streamlit as st
import google.generativeai as genai
import json
import os
from PIL import Image

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

menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "KI Import (Foto/PDF)"])

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

elif menu == "KI Import (Foto/PDF)":
    st.subheader("📄 Lade ein Foto oder ein PDF hoch")
    st.info("Tipp: Fotos (JPG/PNG) funktionieren bei Scans oft am besten!")
    
    uploaded_file = st.file_uploader("Datei wählen", type=["jpg", "jpeg", "png", "pdf"])
    
    if uploaded_file:
        if st.button("Analyse starten"):
            with st.spinner("KI liest das Rezept..."):
                try:
                    # Wir nutzen hier den Namen OHNE 'models/' Präfix
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = (
                        "Extrahiere das Rezept aus diesem Bild/Dokument. "
                        "Antworte NUR mit einem JSON-Objekt: "
                        "{'name': '...', 'Zutaten': ['...'], 'Werkzeuge': ['...'], 'Anleitung': ['...']}"
                    )
                    
                    # Wir senden die Datei direkt als Datenstrom (sehr robust gegen 404)
                    if uploaded_file.type == "application/pdf":
                        # Für PDFs nutzen wir weiterhin den Upload-Weg, aber falls das hakt:
                        st.warning("Falls PDF einen Fehler wirft, probiere bitte einen Screenshot/Foto vom Rezept!")
                    
                    # Bildverarbeitung
                    img = Image.open(uploaded_file)
                    response = model.generate_content([prompt, img])
                    
                    # JSON extrahieren
                    res_text = response.text
                    if "```json" in res_text:
                        res_text = res_text.split("```json")[1].split("```")[0]
                    elif "```" in res_text:
                        res_text = res_text.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(res_text.strip())
                    st.success("Erfolgreich gelesen!")
                    
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
                except Exception as e:
                    st.error(f"Fehler: {e}")
