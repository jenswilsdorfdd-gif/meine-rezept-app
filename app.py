import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Fehlersuche", page_icon="🕵️")
st.title("🕵️ Detektiv-Modus")

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    # Wir lassen 'worksheet' weg, damit er das erste Blatt nimmt
    df = conn.read(ttl=0) 
    
    st.success("Die Leitung steht endlich!")
    st.write("Ich habe folgendes Blatt gefunden:")
    st.dataframe(df.head(2)) # Zeigt die ersten zwei Zeilen
    
except Exception as e:
    st.error("❌ Google blockiert immer noch (400 Bad Request)")
    st.write("Prüfe bitte folgendes:")
    st.info("Ist die Google-Tabelle wirklich für 'Jeden mit dem Link' als 'Editor/Mitarbeiter' freigegeben?")
    st.code(str(e))
