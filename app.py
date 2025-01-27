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
        Ton but c'est de faire le lien tordu entre le thème suivants et ses études.
        Dans ta réponse tu utilise 3 expressions issues de la liste suivante, sans les guillemets : 
        1. Définition Boomer
On l'a souvent entendu associé à "Ok boomer" pour faire remarquer à quelqu'un qu'il est réactionnaire, plus à la page.
Mise en situation : “Ça, c'est une expression de boomer !”

‍

2. Définition Glow up
Signifie embellir/évoluer. On voit fréquemment ce terme sur les réseaux sociaux dans les vidéos avant/après.
Mise en situation : “Tu as grave glow up depuis l’année dernière !”

‍

3. Définition Flex  
Se vanter ou se montrer, généralement à propos de ses possessions, de ses réalisations ou de ses capacités.
Mise en situation : “Arrête de flex avec tes nouvelles chaussures” 

‍

4. Définition Faire crari 
Signifie "faire genre", soit faire semblant.
Mise en situation : “Arrête de faire crari”

‍

5. Définition Aesthethic
Le fait de trouver quelque chose de beau dans son ensemble. L'aesthetic a gagné en popularité, en particulier sur les plateformes telles que Tumblr, Pinterest, Instagram et TikTok.
Mise en situation : “C’est super aesthetic ce que la team Studio a fait”

‍

6. Définition Pépite
Désigne quelqu’un ou quelque chose d’incroyable.
Mise en situation : “C’est une pépite cette femme, vraiment”

‍

7. Définition Cringe
Signifie être gênant. Pour la Gen Z tout est perçu comme cringe. Cela peut être lié à une situation ou bien une façon de faire.
Mise en situation : “Mettre de l’eye-liner, c’est super cringe” 

‍

8. Définition Incr
Contraction de “c’est incroyable”. Expression qui a été popularisée par le rap et les réseaux sociaux.
Mise en situation : “Cet endroit est vraiment incr”

‍

9. Définition Dinguerie
Signifie que c’est incroyable. Mais aussi faire une bêtise.
Mise en situation : “C’est une dinguerie ce qui t’es arrivée aujourd’hui”
“Je crois que j’ai fait une dinguerie” 

‍

10. Définition Slay
Signifie rayonner/ être très beau. Souvent utilisée pour inspirer son admiration à une personne. 
Mise en situation : “Ta tenue slay aujourd’hui”

‍

11. Définition Ick 
Expression de dégoût ou de répulsion à l’égard de quelque chose de désagréable ou de mauvais goût. S’utilise comme une onomatopée.
Mise en situation : “Ick, ça me dégoute”

‍

12. Définition C’est trop 
Signifie que c’est très drôle. On comprend que c’est trop pour la personne, car elle est morte de rire. 
Mise en situation : “Non mais c’est trop cette histoire !”

‍

13. Définition Carré 
Signifie “C’est ok” ou “C’est bien”. 
Mise en situation : “C’est carré ce que tu as fait”

‍

14. Définition Cheugy
Signifie que quelque chose est désuet, démodé ou pas cool, en particulier en termes de mode, de tendances ou d’esthétique. Les Gen Z l’utilisent beaucoup pour se moquer des habitudes des Millenials. 
Mise en situation : “Son style est grave cheugy, on est plus en 2012”

‍

15. Définition GOAT
Vient de l’anglais “the Greatest of All Time”, désigne quelqu’un d’indétrônable.
Mise en situation : “Brad Pitt, c’est le GOAT”

‍

16. Définition Chiller
Souvenez-vous de l’expression Netflix and Chill ! Vient de l’anglais “chill”, signifie se détendre.
Mise en situation : “J’aime trop chiller après le travail”

‍

17. Définition En despi
Signifie rapidement. Expression popularisée par le rap.
Mise en situation : “Il faut que tu me le valides en despi” 

‍

18. Définition Choke
Signifie rater quelque chose qui était à sa portée dans l’univers du gaming.
Mise en situation : “Il a choke cette game sérieux !”


19. Définition Chockbar
Signifie être choqué, on peut rajouter “de bz” pour accentuer l’effet. 
Mise en situation : “Je suis chockbar de ce que tu viens de me dire”


20. Définition POV
Vient de l’anglais “Point of vue” signifie “de mon point de vue”. Il sert à exprimer un sentiment en mettant le spectateur à notre place.
Mise en situation : “POV : tu es community manager chez MO&JO”

‍

21. Définition Red Flag
Traduction de “Drapeau Rouge” en anglais. Signifie qu’une personne serait problématique. À l’origine, le drapeau rouge était utilisé au 17e siècle comme signe d’avertissement pour signaler un danger à l’armée.
Mise en situation : “Non mais [prénom] c’est grave un red flag”


22. Définition Banger
Désigne quelque chose d’incroyable. Expression qui tient son origine du monde de la musique.
Mise en situation : “C’est un banger ce que tu écoutes”


23. Définition Crush 
Signifie avoir un coup de cœur pour une personne. 
Mise en situation : “Je t’avoue, [prénom] c’est mon crush”


24. Définition Dead ça
Désigne avoir réussi quelque chose.
Mise en situation : “Elle a dead ça avec sa présentation”


25. Définition Bail
Ne signifie plus “depuis longtemps” mais quelque chose. Il peut aussi signifier une relation entre deux personnes.
Mise en situation : “Ce bail-là est trop bizarre”

‍
26. Définition Pelo
Désigne un homme/une personne. Terme popularisé par la région lyonnaise.
Mise en situation : “Il y a trois pelos sur la place”

‍

27. Définition Déter
Contraction du mot "déterminé". La Gen Z aime raccourcir les mots avec plus de 2 syllabes. 
Mise en situation : “Je suis grave déter ce matin”

‍
28. Définition Cheum 
Autrefois, cela signifiait “un petit copain”. Maintenant, cela désigne quelque chose ou quelqu’un de moche. 
Mise en situation : “C’est super cheum ce que tu as fait”

‍

29. Définition Pick me
Désigne spécifiquement une femme qui changerait ses manières pour attirer l’attention des hommes. Expression qui s’est généralisée pour désigner une femme problématique.
Mise en situation : “[prénom], je ne peux pas me la voir, c’est une pick me”


30. Définition C’est Gucci
Lié au prestige de la marque, désigne quelque chose de positif. Ce serait comme avoir gagné au loto. 
Mise en situation : “C’est Gucci ce que tu as fait”
        Voici donc le thème n°1 : {theme}. génère la réponse en 400 caractères maximum, qui doit rester juste structurellement et grammaticalement.
        """
        # Appel à l'API Gemini
        response = model.generate_content(prompt_text)
        
        # Extrais le texte de la 1ère candidate
        generated_pitch = response.candidates[0].content.parts[0].text
        
    st.write(generated_pitch)
