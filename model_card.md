# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name: Viber 1.0    

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

# Answer Prompt
    - The system reccommends up to five songs based on the user's prefferences from the
    genre, mood, energy lelve, and acoustic preference. It provides a sort of summary for each song like for example: 
        "Desert Wind (Mesa Roads)  —  Score: 1.77
        Because: Energy level is a close match (0.36); Acoustic feel matches your preference"
    - The system assumes that the user already knows what kind of music they enjoy and that they know their preferences specifically like having an energy level of 0.38. The same system also assumes that the music taste remains consitent as it does not factor something like past history.
    - The system is more for an learning enviroment. I do honestly do not think this system can work efficiently in a real-world application.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

# Answer Prompt
    - The system uses the following features: Mood, energy level, genre, and acousticness. These features of a song are used in the scoring system to reccomend to the user.
    - The following preferences of the user are considered: favorite genre, favorite / current mood, energy level, and wether or not the user likes acoustic.
    - The model compares each song in the catalog against the user's profile using these factors and then adds up the points. A genre match is worth at most two points because genre is the strongest signal of taste. A mood match is worth 1.5 points. Energy is scored continuously. For example, a song that is very close to the user's target energy gets almost a full point, while a song that is far off gets close to zero. Finally, if the song's acoustic character matches what the user said they like, it gets an extra 0.8 points. The song with the highest total score is recommended first, and ties are broken by whichever song has the energy level closest to the user's target.
    - Filled out the empty place holder functions. Added the scoring system. Added more songs to the csv file. 

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset 

# Answer Prompt
    - The model uses 18 songs from the csv file.
    - Here is the complete list of the genres being represented:
        - Pop
        - Indie Pop
        - Lofi
        - Rock
        - Ambient
        - Jazz
        - Synthwave
        - Hip-Hop
        - Soul
        - Classical
        - Folk
        - EDM
        - R&B
        - Country
        - Blues
    - Here is the complete list of the moods being represented:
        - Happy
        - Chill
        - Intense
        - Relaxed
        - Focused
        - Moody
        - Energetic
        - Romantic
        - Melancholic
        - Nostalgic
        - Euphoric
        - Sad
        - Peaceful
        - Longing
    - Data was added from the original csv file.
    - There are a other music tastes that were left out like Latin Rock and K-Pop.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
