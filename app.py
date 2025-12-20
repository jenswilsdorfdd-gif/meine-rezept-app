import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Meine Rezepte", page_icon="🥘", layout="wide")

# Verbindung zur Google Tabelle herstellen
conn = st.connection("gsheets", type=GSheetsConnection)

# Daten laden
df = conn.read(worksheet="Rezepte")

st.title("👨‍🍳 Mein digitales Kochbuch (Cloud-Speicher)")

menu = st.sidebar.radio("Navigation", ["Alle Rezepte", "Neues Rezept hinzufügen"])

if menu == "Alle Rezepte":
    if not df.empty:
        selection = st.selectbox("Rezept wählen:", sorted(df["Name"].tolist()))
        # Details zum gewählten Rezept filtern
        r = df[df["Name"] == selection].iloc[0]
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🛒 Zutaten")
            st.write(r["Zutaten"])
        with col2:
            st.subheader("🛠 Hilfsmittel")
            st.write(r["Werkzeuge"])
        
        st.subheader("👨‍🍳 Anleitung")
        st.write(r["Anleitung"])
    else:
        st.info("Deine Datenbank ist noch leer. Füge dein erstes Rezept hinzu!")

elif menu == "Neues Rezept hinzufügen":
    st.header("📝 Neues Rezept anlegen")
    with st.form("recipe_form"):
        name = st.text_input("Name des Rezepts")
        zutaten = st.text_area("Zutaten")
        werkzeuge = st.text_area("Werkzeuge")
        anleitung = st.text_area("Anleitung")
        
        submit = st.form_submit_button("In Google Tabelle speichern")
        
        if submit:
            if name:
                # Neue Zeile erstellen
                new_data = pd.DataFrame([{"Name": name, "Zutaten": zutaten, "Werkzeuge": werkzeuge, "Anleitung": anleitung}])
                # An bestehende Daten anhängen
                updated_df = pd.concat([df, new_data], ignore_index=True)
                # In Google Sheets speichern
                conn.update(worksheet="Rezepte", data=updated_df)
                st.success(f"Rezept '{name}' wurde erfolgreich gespeichert!")
                st.balloons()
            else:
                st.error("Bitte gib mindestens einen Namen ein.")
