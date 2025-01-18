import google.generativeai as genai
import streamlit as st
import os

# Configure ton API key Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMORx0IGLazJZA17dH3_hRQmGeThP7Kkg" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Choix du modèle
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Présentation LinkedIn")

theme = st.text_area("C'est quoi ton métier ?")

if st.button("Générer mon pitch"):
    with st.spinner("Patience, patience..."):
        # Ton prompt
        prompt_text = f"""Tu joues le rôle d'un homme appelé Benoît. A chaque fois qu'on
        lui donne un thème, Benoit réagit avec les critères suivants :
        - il repond en 200 caractères maximum 
        - il utilise de manière exagérée les adjectifs "BEAU", "BELLE, et leurs dérivés, et toujours en majuscule
        - il réussit toujours à caler la phrase suivante : "Vous aimez ça, {theme} ?"
        - il réussit toujours à faire un lien entre le thème et le fait qu'il ait grandi à la ferme, qu'il est un homme du terroir, quitte
        à ce que ce soit tiré par les cheveux.
        Voici donc le thème : {theme}. génère la réponse de Benoît.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.subheader("Ton pitch LinkedIn :")
    st.write(generated_pitch)
