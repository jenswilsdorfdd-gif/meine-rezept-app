import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Meine Rezepte", page_icon="🥘", layout="wide")

# Verbindung zur Google Tabelle
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    # ttl=0 sorgt dafür, dass wir immer die neuesten Daten sehen
    df = conn.read(worksheet="Rezepte", ttl=0)
except Exception as e:
    st.error(f"Verbindung zu Google fehlgeschlagen. Fehler: {e}")
    st.stop()

st.title("👨‍🍳 Mein digitales Kochbuch")

# Navigation in der Seitenleiste
menu = st.sidebar.radio("Navigation", ["Rezepte durchsuchen", "Neues Rezept hinzufügen"])

if menu == "Rezepte durchsuchen":
    if not df.empty:
        # Suchfeld
        search_query = st.text_input("🔍 Welches Rezept suchst du? (z.B. Chili oder Kuchen)")
        
        # Filter-Logik: Wir suchen im Namen, in den Zutaten und in der Anleitung
        filtered_df = df[
            df['Name'].str.contains(search_query, case=False, na=False) |
            df['Zutaten'].str.contains(search_query, case=False, na=False) |
            df['Anleitung'].str.contains(search_query, case=False, na=False)
        ]
        
        if not filtered_df.empty:
            selection = st.selectbox("Gefundene Rezepte:", sorted(filtered_df["Name"].unique().tolist()))
            r = filtered_df[filtered_df["Name"] == selection].iloc[0]
            
            st.divider()
            st.header(f"📖 {r['Name']}")
            
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
            st.warning("Kein Rezept mit diesem Namen oder dieser Zutat gefunden.")
    else:
        st.info("Deine Datenbank ist noch leer.")

elif menu == "Neues Rezept hinzufügen":
    st.header("📝 Neues Rezept anlegen")
    with st.form("recipe_form"):
        name = st.text_input("Name des Rezepts")
        zutaten = st.text_area("Zutaten (untereinander schreiben)")
        werkzeuge = st.text_area("Hilfsmittel / Werkzeuge")
        anleitung = st.text_area("Schritt-für-Schritt Anleitung")
        submit = st.form_submit_button("Speichern")
        
        if submit:
            if name:
                new_line = pd.DataFrame([{"Name": name, "Zutaten": zutaten, "Werkzeuge": werkzeuge, "Anleitung": anleitung}])
                updated_df = pd.concat([df, new_line], ignore_index=True)
                conn.update(worksheet="Rezepte", data=updated_df)
                st.success(f"'{name}' wurde gespeichert! Lade die Seite neu, um es zu sehen.")
                st.balloons()
            else:
                st.error("Bitte gib einen Namen ein.")
