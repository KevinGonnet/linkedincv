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
        prompt_text = f"""Tu t'adresses à un étudiant en bachelor qui a environ 18 ans. Adresse toi à lui/elle comme si tu le connaissais. Tu le tutoie.
        Ton but c'est de faire le lien tordu entre le thème n°1 suivant et un thème n°2 de ton choix (ses études, la vie d'étudiant, les choses qui concernent 
        un jeune de 18 ans, la culture rap, le rappeur booba, devenir célèbre). Tu utilise des expressions très street.
        Voici donc le thème n°1 : {theme}. génère la réponse en 400 caractères maximum, qui doit rester juste structurellement et grammaticalement.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.write(generated_pitch)
