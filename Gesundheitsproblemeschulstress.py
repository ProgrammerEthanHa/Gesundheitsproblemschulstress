import streamlit as st
import pandas as pd
import altair as alt

st.header("Gesundheitsprobleme durch Schulstress")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [35, 21, 29, 32, 22],
        'Probleme / Krankheit': ['Kopfschmerzen', 'Bauchschmerzen', 'Rückenschmerzen', 'Schlafprobleme', 'Schwindel']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Probleme / Krankheit:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: nicht angegeben")