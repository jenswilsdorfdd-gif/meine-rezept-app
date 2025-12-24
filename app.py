import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import json

# KI Konfiguration
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Wir nutzen hier die stabilste Bezeichnung
    model = genai.GenerativeModel('gemini-1.5-flash')
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
        for i, step in enumerate(r["Anleitung"], 1):
            st.write(f"**{i}.** {step}")

elif menu == "KI PDF-Import":
    st.subheader("📄 Automatischer Import via Gemini KI")
    uploaded_file = st.file_uploader("PDF hochladen", type="pdf")
    
    if uploaded_file:
        with st.spinner("KI analysiert das Rezept..."):
            try:
                reader = PdfReader(uploaded_file)
                raw_text = "".join([page.extract_text() for page in reader.pages])
                
                # Der Prompt wurde etwas verfeinert für bessere Stabilität
                prompt = f"Verwandle diesen Rezepttext in ein JSON-Objekt mit den Feldern 'name', 'Zutaten' (Liste), 'Werkzeuge' (Liste) und 'Anleitung' (Liste). Text: {raw_text}"
                
                response = model.generate_content(prompt)
                
                # Falls die KI Text um das JSON herum baut, filtern wir das hier
                clean_text = response.text.strip()
                if "```json" in clean_text:
                    clean_text = clean_text.split("```json")[1].split("```")[0].strip()
                elif "```" in clean_text:
                    clean_text = clean_text.split("```")[1].split("```")[0].strip()
                
                recipe_data = json.loads(clean_text)
                st.success("Analyse erfolgreich!")
                
                new_name = st.text_input("Rezept Name:", value=recipe_data.get("name", "Unbekannt"))
                
                col1, col2 = st.columns(2)
                with col1:
                    zutaten = st.text_area("Zutaten", value="\n".join(recipe_data.get("Zutaten", [])), height=200)
                with col2:
                    werkzeuge = st.text_area("Werkzeuge", value=", ".join(recipe_data.get("Werkzeuge", [])))
                
                anleitung = st.text_area("Anleitung", value="\n".join(recipe_data.get("Anleitung", [])), height=200)
                
                if st.button("Speichern"):
                    st.session_state.recipes[new_name] = {
                        "Zutaten": zutaten.split("\n"),
                        "Werkzeuge": werkzeuge.split(","),
                        "Anleitung": anleitung.split("\n")
                    }
                    st.balloons()
            except Exception as e:
                st.error(f"Fehler: {str(e)}")
                st.write("Versuche es bitte noch einmal oder prüfe, ob das PDF Text enthält.")
