import streamlit as st
import google.generativeai as genai
import gspread
from google.oauth2.service_account import Credentials
import json
from PIL import Image

# 1. Verbindung zur Tabelle "Rezept_Datenbank"
def get_spreadsheet():
    try:
        scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        # Nutzt deine hinterlegten Secrets
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
        client = gspread.authorize(creds)
        # Öffnet exakt die Tabelle, die du angelegt hast
        return client.open("Rezept_Datenbank").sheet1
    except Exception as e:
        st.error(f"Verbindung zur Tabelle 'Rezept_Datenbank' fehlgeschlagen: {e}")
        return None

# 2. KI Konfiguration (Fix für den 404-Fehler)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Wir nutzen den stabilen Namen ohne v1beta-Präfix
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API Key fehlt! Bitte in den Streamlit Secrets eintragen.")

st.set_page_config(page_title="Rezept_Datenbank", layout="wide")
st.title("🍳 Meine Rezepte (Rezept_Datenbank)")

menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "Neues Rezept (KI Upload)"])

# --- REZEPTE ANSEHEN ---
if menu == "Rezepte ansehen":
    sheet = get_spreadsheet()
    if sheet:
        data = sheet.get_all_records()
        if not data:
            st.info("Die Datenbank ist aktuell leer.")
        else:
            names = [r["Name"] for r in data if r["Name"]]
            selected = st.selectbox("Wähle ein Rezept aus deiner Liste:", names)
            recipe = next(item for item in data if item["Name"] == selected)
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("🛒 Zutaten")
                st.write(recipe.get("Zutaten", ""))
            with col2:
                st.subheader("🛠 Hilfsmittel")
                st.write(recipe.get("Werkzeuge", ""))
            st.subheader("👨‍🍳 Anleitung")
            st.write(recipe.get("Anleitung", ""))

# --- KI UPLOAD ---
elif menu == "Neues Rezept (KI Upload)":
    st.subheader("📄 Rezept per Foto oder PDF hinzufügen")
    uploaded_file = st.file_uploader("Datei wählen", type=["pdf", "jpg", "jpeg", "png"])
    
    if uploaded_file and st.button("Analyse & Speichern"):
        with st.spinner("KI liest Rezept..."):
            try:
                prompt = (
                    "Extrahiere das Rezept als JSON-Objekt mit den Feldern: "
                    "'name', 'Zutaten', 'Werkzeuge', 'Anleitung'. "
                    "Antworte NUR mit dem JSON."
                )
                
                # Datei-Handling
                if uploaded_file.type == "application/pdf":
                    import pypdf
                    reader = pypdf.PdfReader(uploaded_file)
                    content = [prompt, "".join([p.extract_text() for p in reader.pages])]
                else:
                    img = Image.open(uploaded_file)
                    content = [prompt, img]
                
                # KI Anfrage
                response = model.generate_content(content)
                res_text = response.text.replace("```json", "").replace("```", "").strip()
                res = json.loads(res_text)
                
                # In die Tabelle "Rezept_Datenbank" schreiben
                sheet = get_spreadsheet()
                if sheet:
                    sheet.append_row([res['name'], res['Zutaten'], res['Werkzeuge'], res['Anleitung']])
                    st.success(f"'{res['name']}' wurde erfolgreich in deiner Tabelle gespeichert!")
                    st.balloons()
            except Exception as e:
                st.error(f"Fehler bei der Analyse: {e}")
