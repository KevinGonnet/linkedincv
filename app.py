import google.generativeai as genai
import streamlit as st
import os

# Configure ton API key Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMORx0IGLazJZA17dH3_hRQmGeThP7Kkg" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Choix du modèle
model = genai.GenerativeModel("gemini-2.0-flash-exp")

st.title("Oh un étudiant de l'IPAC ! C'est quoi ton thème ?")

theme = st.text_area("Écris ci-dessous")

if st.button("Let's go !"):
    with st.spinner("Patience, patience..."):
        # Ton prompt
        prompt_text = f"""Tu t'adresses à des étudiants en bachelor de management
        du sport à Annecy, ils ont environ 18 ans. Sers toi donc de ces infos pour t'adresser à eux comme si tu les connaissais. Tu les tutoie.
        Ton but c'est de faire le lien entre le thème suivant et leurs études, même si c'est tiré par les cheveux c'est encore plus drôle.
        Voici donc le thème : {theme}. génère la réponse en 300 caractères maximum, qui doit rester juste structurellement et grammaticalement.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.write(generated_pitch)
