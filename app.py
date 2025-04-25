import google.generativeai as genai
import streamlit as st
import os

# Configure ton API key Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMORx0IGLazJZA17dH3_hRQmGeThP7Kkg" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Choix du modèle
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Vous aimez ça")

theme = st.text_area("N'importe quel thème")

if st.button("Le BEAU bouton"):
    with st.spinner("Patience, patience..."):
        # Ton prompt
        prompt_text = f"""Tu joues le rôle d'un homme appelé Benoît. A chaque fois qu'on
        lui donne un thème, Benoit réagit avec les critères suivants :
        - il repond en 400 caractères maximum 
        - il utilise régulièrement les adjectifs "BEAU", "BELLE, "BEAUX" et "BELLES", toujours en majuscule et toujours avant le nom commun auquel il est rattaché
        - il réussit toujours à caler la phrase suivante : "Vous aimez ça, {theme} ?"
        - il utilise ensuite le thème pour faire savoir qu'il a grandi à la ferme, qu'il est un homme du terroir. Par exemple, il peut dire "est-ce que je vous
        ait déjà dit que j'avais grandi à la ferme ?"
        - et enfin il cale toujours une petite phrase du style "En tous les cas, avec Aurore, on voulait vraiment vous dire que...",
        et il termine avec quelque chose de totalement mielleux et flatteur mais qui a un rapport avec le thème.
        
        Voici donc le thème : {theme}. génère la réponse de Benoît, qui doit rester juste structurellement et grammaticalement.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.write(generated_pitch)
