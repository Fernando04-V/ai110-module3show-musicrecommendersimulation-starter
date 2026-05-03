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

# Answer Prompt
- The model yields the most reasonable results when the interest of a user alligns with aleast one song. For example, take for example the Chill lofi profile where the output checks out with the profile's interest:  
    - Profile: Chill Lofi; genre=lofi, mood=chill, energy=0.38, acoustic=True

        Library Rain (Paper Lanterns)  —  Score: 5.27
        Because: Genre matches your favorite: lofi; Mood matches: chill; Energy level is a close match (0.35); Acoustic feel matches your preference

        Midnight Coding (LoRoom)  —  Score: 5.26
        Because: Genre matches your favorite: lofi; Mood matches: chill; Energy level is a close match (0.42); Acoustic feel matches your preference

        Focus Flow (LoRoom)  —  Score: 3.78
        Because: Genre matches your favorite: lofi; Energy level is a close match (0.4); Acoustic feel matches your preference

- I think one the patterns the model captures quite well is the combination between genre and mood. When both of these features of the user match a song it allows for the same song to raise greatly in points. If either of them are missing, then the points does not increase as much. Take for example the Chill Lofi Profile, we can notice how the top two songs are way above the third song most reccommend song in terms of score; the top two songs align with the user's mood and genre while "Focus Flow" the matching mood.
- Cases like chill lofi and Deep Intense Rock matches my intution pretty well. Like discussed above with chill lofi, intense rock having Storm Runner as the number one is reasonable.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

# Answer Prompt
- The model ignores the following features that are present in each song: tempo_bpm,valence,and danceability.
- There are some genres and moods that only appear once as in the cases of blues and longing. 
- Genre carries a weight of 2.0 out of a maximum of 5.3 points. This means a song that matches genre but gets everything else wrong will almost always outrank a song that matches mood, energy, and acousticness but has a different genre. For example, the High-Energy Pop profile, Gym Hero scored 2.87 with only a genre match, while Night Drive Loop, which matched energy almost perfectly at 0.95 energy score, scored only 0.95 because it was synthwave instead of pop. A real listener might actually prefer Night Drive Loop for a pop-energy session, but the genre gate overrules that.
- The model may untitentionally favor some users whose taste aligns exactly with a well-represented genre in the catalog as in the case of lofi. Someone who says "indie" rather than "inde pop" does not get points for an indie pop song despite the obvious match.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

# Answer Prompt
- I made the profile "Storm Runner Fan" to test if the a user having the identical attributes of the song, Storm Runner, yields in a perfect socre and having the song reccomended the most. After testing, it does. 
- What i looked for in the recoomendation is wether or not the top result was obvious. Somone who likes to listen to Storm Runner alot should be reccomended storm runner the most out of all the songs in the catalog. 
- Something the the model suprised me was how detailed it was able to make the gap between the songs being reccomended. In the Chill Lofi profile, we can see how "Library Rain" scored a 5.27 and "Midnight Coding" scored a 5.26. This showed me that there was indeed a difference between similar songs.
- I ran the " Storm Runner Fan" to affirm the model's perfect scoring.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

# Answer Prompt
- Something i would add into the future is something like the model evaluating the user's history or the amount of times they skipped over a song. For instance, Apple Music for some reason keeps on reccomending me the songs that i continusly skip. A feature where where it removes points for the amount of skips a song recives could be interesting for future work. 
- Perhaps providing a reason as to why some songs did not get reccomended even though they either were close to being matched.
- A diversity penalty could be added so that once a genre or mood has already appeared in the top results, the next song from that same category gets a small score deduction, pushing more varied options into the list. 
- I would make the user profile's more dynamic rather than static to accept more complex user tastes.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

# Answer Prompt
- Because of this module, I learned a more in-depth view on reccomender system. Beforehand, i heard or somewhat knew that systems as such use like a sort of points system where the movie, or in this case the song, with the most points gets reccoemnded the most. Now i got to see that not only this is sort of true, but i got to personal work with such system.
- Something that i find interesting upon working with a reccomender system is that how easy it is to made a system so biased towards something. My model awards more points for matching genre, but i can see where i could have tweaked it and awarded more points for matching mood instead. I belive the lesson here is to have a balance and not "over favor" one factor while completly ignoring the rest. 
- I now see why in some days i feel like i keep on being reccomended the same songs. I believe that part of the issue is that i am only giving the system the same data and i do not stop listening to the same ten songs each day.