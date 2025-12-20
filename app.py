import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("🔌 Verbindungs-Test")

try:
    # Nur die Verbindung aufbauen
    conn = st.connection("gsheets", type=GSheetsConnection)
    # Nur die erste Spalte lesen
    df = conn.read(worksheet="Rezepte", ttl=0)
    
    st.success("Die Leitung steht!")
    st.write("Gefundene Rezepte in deiner Liste:")
    st.table(df[["Name"]]) # Zeigt nur die Namen an

except Exception as e:
    st.error("❌ Google lehnt die Verbindung ab.")
    st.write("Hier ist der technische Grund:")
    st.code(str(e))
