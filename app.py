import google.generativeai as genai
import os

# Configure ton API key Gemini
os.environ["GOOGLE_API_KEY"] = "AIzaSyDMORx0IGLazJZA17dH3_hRQmGeThP7Kkg" 
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Choix du modèle
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("LinkedIn Pitch Booster (Powered by Gemini)")

user_cv = st.text_area("Colle ici ton CV / résumé LinkedIn")

if st.button("Générer mon pitch"):
    with st.spinner("Un instant, je réfléchis..."):
        # Ton prompt
        prompt_text = f"""Analyse ce CV:
        {user_cv}
        Génère un 'À propos' LinkedIn concis, punchy et professionnel, en français.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.subheader("Ton pitch LinkedIn :")
    st.write(generated_pitch)
