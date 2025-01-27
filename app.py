import google.generativeai as genai
import streamlit as st
import os

# Configure ton API key Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMORx0IGLazJZA17dH3_hRQmGeThP7Kkg" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Choix du modèle
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Oh un étudiant de l'IPAC ! On parle de quoi aujourd'hui ?")

if st.button("Let's go !"):
    with st.spinner("Patience, patience..."):
        # Ton prompt
        prompt_text = f"""Tu joues le rôle du footballeur Kylian Mbappé, qui utilise sa manière de parler et ses
        expressions caractéristiques pour réagir à n'importe quelle thème.        
        Voici donc le thème : {theme}. génère la réponse de Kylian, qui doit rester juste structurellement et grammaticalement.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.write(generated_pitch)
