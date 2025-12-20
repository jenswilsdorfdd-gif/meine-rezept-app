import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Mein digitales Kochbuch", page_icon="🥘", layout="wide")

# Verbindung zur Google Tabelle herstellen
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read(ttl=0)
except Exception as e:
    st.error(f"Verbindung zu Google fehlgeschlagen: {e}")
    st.stop()

st.title("👨‍🍳 Mein digitales Kochbuch")

# Navigation in der Seitenleiste
menu = st.sidebar.radio("Navigation", ["Rezepte durchsuchen", "Neues Rezept hinzufügen", "Rezept bearbeiten"])

if menu == "Rezepte durchsuchen":
    if not df.empty:
        search_query = st.text_input("🔍 Welches Rezept suchst du?")
        mask = (
            df['Name'].str.contains(search_query, case=False, na=False) |
            df['Zutaten'].str.contains(search_query, case=False, na=False)
        )
        filtered_df = df[mask]
        
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
        st.info("Datenbank ist leer.")

elif menu == "Neues Rezept hinzufügen":
    st.header("📝 Neues Rezept anlegen")
    with st.form("add_form"):
        name = st.text_input("Name")
        zutaten = st.text_area("Zutaten")
        werkzeuge = st.text_area("Werkzeuge")
        anleitung = st.text_area("Anleitung")
        if st.form_submit_button("Speichern"):
            if name:
                new_line = pd.DataFrame([{"Name": name, "Zutaten": zutaten, "Werkzeuge": werkzeuge, "Anleitung": anleitung}])
                updated_df = pd.concat([df, new_line], ignore_index=True)
                conn.update(data=updated_df)
                st.success(f"'{name}' wurde gespeichert!")
                st.balloons()
            else:
                st.error("Bitte einen Namen angeben.")

elif menu == "Rezept bearbeiten":
    st.header("✏️ Rezept anpassen")
    if not df.empty:
        edit_selection = st.selectbox("Welches Rezept möchtest du ändern?", sorted(df["Name"].tolist()))
        # Index des gewählten Rezepts finden
        idx = df[df["Name"] == edit_selection].index[0]
        r_to_edit = df.iloc[idx]

        with st.form("edit_form"):
            new_name = st.text_input("Name", value=r_to_edit["Name"])
            new_zutaten = st.text_area("Zutaten", value=r_to_edit["Zutaten"])
            new_werkzeuge = st.text_area("Werkzeuge", value=r_to_edit["Werkzeuge"])
            new_anleitung = st.text_area("Anleitung", value=r_to_edit["Anleitung"])
            
            if st.form_submit_button("Änderungen übernehmen"):
                # DataFrame an der Stelle idx aktualisieren
                df.at[idx, "Name"] = new_name
                df.at[idx, "Zutaten"] = new_zutaten
                df.at[idx, "Werkzeuge"] = new_werkzeuge
                df.at[idx, "Anleitung"] = new_anleitung
                
                conn.update(data=df)
                st.success("Änderungen wurden in Google Sheets gespeichert!")
                st.rerun()
