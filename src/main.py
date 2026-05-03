"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from recommender import load_songs, recommend_songs

_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "songs.csv")


profiles = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.88,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.38,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "likes_acoustic": False,
    },
    "Late Night R&B": {
        "genre": "r&b",
        "mood": "sad",
        "energy": 0.45,
        "likes_acoustic": False,
    },
    "Acoustic Folk Nostalgia": {
        "genre": "folk",
        "mood": "nostalgic",
        "energy": 0.33,
        "likes_acoustic": True,
    },
    "Storm Runner Fan": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.91,
        "likes_acoustic": False,
    },
}


def run_profile(name: str, user_prefs: dict, songs: list) -> None:
    """Print the top 3 recommendations for a single user profile."""
    print(f"\n{'='*50}")
    print(f"Profile: {name}")
    print(f"  genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
          f"energy={user_prefs['energy']}, acoustic={user_prefs['likes_acoustic']}")
    print(f"{'='*50}")
    for song, score, explanation in recommend_songs(user_prefs, songs, k=3):
        print(f"  {song['title']} ({song['artist']})  —  Score: {score:.2f}")
        print(f"  Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs(_DATA_PATH)
    print(f"Loaded songs: {len(songs)}")

    for name, prefs in profiles.items():
        run_profile(name, prefs, songs)


if __name__ == "__main__":
    main()
