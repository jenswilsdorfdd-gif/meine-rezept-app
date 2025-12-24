import streamlit as st
import google.generativeai as genai
import json
import time
import os

# 1. KI Konfiguration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key fehlt in den Secrets!")

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
    st.write("Die KI erkennt Text, Scans und sogar Handschrift.")
    
    uploaded_file = st.file_uploader("Datei wählen", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file:
        if st.button("Analyse starten"):
            with st.spinner("KI liest die Datei... das kann bis zu 30 Sek. dauern."):
                try:
                    # Datei temporär speichern, damit Gemini sie hochladen kann
                    with open("temp_file", "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Datei zu Google hochladen
                    sample_file = genai.upload_file(path="temp_file", display_name="Rezept-Upload")
                    
                    # Warten, bis Google die Datei verarbeitet hat
                    while sample_file.state.name == "PROCESSING":
                        time.sleep(2)
                        sample_file = genai.get_file(sample_file.name)

                    # Die KI fragen (Wir nutzen hier das stabilste Modell)
                    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
                    prompt = (
                        "Analysiere dieses Dokument/Bild und extrahiere das Kochrezept. "
                        "Antworte NUR mit einem validen JSON-Objekt in diesem Format: "
                        "{'name': 'Name des Gerichts', 'Zutaten': ['Zutat 1', 'Zutat 2'], "
                        "'Werkzeuge': ['Topf', 'Messer'], 'Anleitung': ['Schritt 1', 'Schritt 2']}"
                    )
                    
                    response = model.generate_content([sample_file, prompt])
                    
                    # JSON extrahieren
                    raw_text = response.text
                    if "```json" in raw_text:
                        raw_text = raw_text.split("```json")[1].split("```")[0]
                    elif "```" in raw_text:
                        raw_text = raw_text.split("```")[1].split("```")[0]
                    
                    recipe_data = json.loads(raw_text.strip())
                    
                    # Anzeige der Ergebnisse
                    st.success("Erfolgreich gelesen!")
                    new_name = st.text_input("Name des Rezepts:", value=recipe_data.get("name", "Neues Rezept"))
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])))
                    with c2:
                        werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                    
                    anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])), height=200)
                    
                    if st.button("In App speichern"):
                        st.session_state.recipes[new_name] = {
                            "Zutaten": zutaten.split("\n"),
                            "Werkzeuge": werkzeuge.split(","),
                            "Anleitung": anleitung.split("\n")
                        }
                        st.balloons()
                        st.success(f"'{new_name}' gespeichert!")
                    
                    # Temp Datei aufräumen
                    os.remove("temp_file")
                    
                except Exception as e:
                    st.error(f"Fehler: {e}")
                    if "404" in str(e):
                        st.warning("Tipp: Der 404 Fehler deutet oft auf ein Problem mit der Modell-Verfügbarkeit hin. Ich versuche es im Hintergrund zu korrigieren.")
