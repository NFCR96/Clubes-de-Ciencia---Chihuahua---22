import streamlit as st
st.title('Club 3')
st.write('en este club exploraremos posibilidades alternas para el desarollo de farmacos contra las enfermedades emergentes, basandonos en aproximaciones bioinformaticas')

#Seccion 1: Nuestro Club/Our Club
my_page = st.sidebar.radio("Página de navegación", ["Biologia molecular/ Molecular Biology", "Proteinas/Proteins", "Resistencia antimicrobiana/Antimicrobial resistance", "COVID-19", "Referencias bibliográficas"])
