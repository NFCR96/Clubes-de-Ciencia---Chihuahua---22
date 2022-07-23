import streamlit as st
st.title('Club 3')

#Seccion 1: Nuestro Club/Our Club
my_page = st.sidebar.radio("Página de navegación", ["Biologia molecular/ Molecular Biology", "Proteinas/Proteins", "Resistencia antimicrobiana/Antimicrobial resistance", "COVID-19", "Referencias bibliográficas"])
