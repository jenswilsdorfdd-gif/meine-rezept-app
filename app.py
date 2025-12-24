import streamlit as st
from pypdf import PdfReader

# 1. Datenbank initialisieren
if 'recipes' not in st.session_state:
    st.session_state.recipes = {
        "Drumsticks SF Style": {
            "Zutaten": ["1.5kg Hühnerbeine", "75ml Sojasauce"],
            "Werkzeuge": ["Backblech", "Topf"],
            "Anleitung": ["Hähnchen marinieren", "Im Ofen backen"]
        }
    }

st.set_page_config(page_title="Rezept-App", layout="wide")
st.title("🍳 Meine Rezept-Verwaltung")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["Rezepte ansehen", "Neues Rezept (PDF Upload)", "Rezept bearbeiten"])

# --- FUNKTION: REZEPTE ANSEHEN ---
if menu == "Rezepte ansehen":
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

# --- FUNKTION: PDF UPLOAD ---
elif menu == "Neues Rezept (PDF Upload)":
    st.subheader("📄 Neues Rezept aus PDF erstellen")
    
    uploaded_file = st.file_uploader("Wähle eine PDF-Datei aus", type="pdf")
    
    if uploaded_file is not None:
        # PDF Text extrahieren
        reader = PdfReader(uploaded_file)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
        
        st.info("Text aus PDF erkannt! Bitte unten kurz sortieren:")
        
        # Eingabemaske für das neue Rezept
        new_name = st.text_input("Name des Rezepts", placeholder="z.B. Omas Apfelkuchen")
        
        col1, col2 = st.columns(2)
        with col1:
            z_text = st.text_area("Zutaten (eine pro Zeile)", value=full_text[:200]) # Zeigt ersten Teil als Hilfe
        with col2:
            w_text = st.text_area("Werkzeuge (kommagetrennt)")
            
        a_text = st.text_area("Anleitung (ein Schritt pro Zeile)")
        
        if st.button("Rezept speichern"):
            if new_name:
                # In Datenbank speichern
                st.session_state.recipes[new_name] = {
                    "Zutaten": z_text.split("\n"),
                    "Werkzeuge": w_text.split(","),
                    "Anleitung": a_text.split("\n")
                }
                st.success(f"Rezept '{new_name}' wurde hinzugefügt!")
            else:
                st.error("Bitte gib einen Namen für das Rezept an.")

# --- FUNKTION: BEARBEITEN ---
elif menu == "Rezept bearbeiten":
    st.info("Hier kannst du bestehende Rezepte bald anpassen.")
