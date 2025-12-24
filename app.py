import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import json

# 1. KI Konfiguration (holt den Key sicher aus dem Tresor)
# Stelle sicher, dass du den Key in den Streamlit Secrets unter "GEMINI_API_KEY" gespeichert hast!
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
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
                # PDF Text lesen
                reader = PdfReader(uploaded_file)
                raw_text = "".join([page.extract_text() for page in reader.pages])
                
                # KI-Anfrage (Prompt)
                prompt = f"""
                Extrahiere das Rezept aus folgendem Text und gib es NUR als JSON zurück.
                Format: {{"name": "...", "Zutaten": ["..."], "Werkzeuge": ["..."], "Anleitung": ["..."]}}
                Text: {raw_text}
                """
                
                response = model.generate_content(prompt)
                
                # Bereinigung der KI-Antwort
                json_str = response.text.replace("```json", "").replace("```", "").strip()
                recipe_data = json.loads(json_str)
                
                st.success("Analyse fertig!")
                
                # Felder zum Bestätigen
                new_name = st.text_input("Name des Rezepts:", value=recipe_data.get("name", "Neues Rezept"))
                
                col1, col2 = st.columns(2)
                with col1:
                    zutaten_liste = recipe_data.get("Zutaten", [])
                    zutaten = st.text_area("Zutaten (bearbeitbar)", value="\n".join(zutaten_liste), height=200)
                with col2:
                    werkzeuge_liste = recipe_data.get("Werkzeuge", [])
                    werkzeuge = st.text_area("Werkzeuge", value=", ".join(werkzeuge_liste))
                
                anleitung_liste = recipe_data.get("Anleitung", [])
                anleitung = st.text_area("Anleitung", value="\n".join(anleitung_liste), height=200)
                
                if st.button("Rezept endgültig speichern"):
                    st.session_state.recipes[new_name] = {
                        "Zutaten": zutaten.split("\n"),
                        "Werkzeuge": werkzeuge.split(","),
                        "Anleitung": anleitung.split("\n")
                    }
                    st.balloons()
                    st.success(f"'{new_name}' wurde gespeichert!")
            except Exception as e:
                st.error(f"Fehler bei der Analyse: {e}")
