import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        song_dicts = [asdict(s) for s in self.songs]
        scored = [
            (song, score_song(user_prefs, sd))
            for song, sd in zip(self.songs, song_dicts)
        ]
        ranked = sorted(
            scored,
            key=lambda x: (-x[1][0], abs(x[0].energy - user.target_energy))
        )
        return [song for song, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, asdict(song))
        return "; ".join(reasons) if reasons else "No strong match found."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py

    Scoring rules (max 5.3 points):
      Rule 1 — Genre match:       +2.0
      Rule 2 — Mood match:        +1.5
      Rule 3 — Energy proximity:  +0.0 to +1.0
      Rule 4 — Acoustic match:    +0.8
    """
    score = 0.0
    reasons = []

    # Rule 1: Genre match (weight 2.0)
    if song["genre"] == user_prefs.get("genre", ""):
        score += 2.0
        reasons.append(f"Genre matches your favorite: {song['genre']}")

    # Rule 2: Mood match (weight 1.5)
    if song["mood"] == user_prefs.get("mood", ""):
        score += 1.5
        reasons.append(f"Mood matches: {song['mood']}")

    # Rule 3: Energy proximity — penalty grows with distance (weight up to 1.0)
    target_energy = float(user_prefs.get("energy", 0.5))
    energy_diff = abs(song["energy"] - target_energy)
    score += 1.0 - energy_diff
    if energy_diff <= 0.10:
        reasons.append(f"Energy level is a close match ({song['energy']})")
    elif energy_diff >= 0.40:
        reasons.append(
            f"Energy level differs from your preference "
            f"({song['energy']} vs {target_energy})"
        )

    # Rule 4: Acoustic preference — threshold 0.60 splits the catalog cleanly (weight 0.8)
    song_is_acoustic = song["acousticness"] >= 0.60
    if user_prefs.get("likes_acoustic", True) == song_is_acoustic:
        score += 0.8
        reasons.append("Acoustic feel matches your preference")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py

    Ranking rule: sort by score descending; break ties by energy proximity.
    Returns a list of (song_dict, score, explanation) tuples.
    """
    target_energy = float(user_prefs.get("energy", 0.5))

    scored = [
        (song, score, reasons)
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    ranked = sorted(
        scored,
        key=lambda x: (-x[1], abs(x[0]["energy"] - target_energy))
    )

    return [
        (song, score, "; ".join(reasons) if reasons else "Partial match")
        for song, score, reasons in ranked[:k]
    ]
