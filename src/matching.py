import rapidfuzz
import os
import re

def normalize_name(name: str) -> str:
    NOISE_WORDS = {
        "official", "audio", "video", "lyrics", "lyric",
        "remastered", "remaster", "hq", "hd", "320kbps",
        "explicit", "clean"}

    name = name.lower()
    name = re.sub(r'\.[a-z0-9]{2,4}$', '', name)   # remove extension
    name = re.sub(r'[\[\(].*?[\]\)]', '', name)    # remove brackets
    name = re.sub(r'[_\-]+', ' ', name)            # unify separators
    
    words = []
    for word in name.split():
        cleaned = ''.join(ch for ch in word if ch.isalnum())
        if cleaned and cleaned not in NOISE_WORDS and not cleaned.isdigit():
            words.append(cleaned)

    return " ".join(words)

def normalize_audio_files(audio_files: list[AudioFile]) -> list[AudioFile]:
    """adds normalized_name to the AudioFile objs"""

    normalized_audio_files = []
    
    for audio_file in audio_files:
        audio_file.normalized_name = normalize_name(audio_file.original_name)
        normalized_audio_files.append()
    return [normalize_name(file) for file in audio_files]

def normalize_tracks(tracks: list[dict]) -> list[dict]:
    for track in tracks:
        track["artist"] = normalize_name(track["artist"])
        track["name"] = normalize_name(track["name"])
    return tracks    

def score_title_similarity(song_name: str, file_name: str) -> float:
    return rapidfuzz.partial_ratio(song_name, file_name)

# since im only using normalization for now, artist_similarity assumes the artist's name is also present in the file_name
# ideal behaviour should be to default to tag based similarity calculation, but resorting to file_name based search if tag doesnt exist
# will add tags based searching later
def score_artist_similarity(artist_name: str, file_name: str) -> float:
    return rapidfuzz.partial_ratio(artist_name, file_name)

def score_duration_similarity(song_duration: int, file_duration: int) -> float:
    MAX_TOLERANCE = 10
    return 1.0 - abs(song_duration - file_duration)/MAX_TOLERANCE

def compute_match_score(track, audio_file, 
                        weights={"title": 0.5,
                                "artist": 0.3,
                                "duration": 0.2}):

    title_similarity = score_title_similarity(track["name"], audio_file)
    artist_similarity = score_title_similarity(track["artist"], audio_file)
    # need to do something about the duration
    duration_similarity = score_title_similarity(track["duration"], audio_file.info.length)
    
    final_score = ((weights["title"] * title_similarity) + 
                  (weights["artist"] * artist_similarity) + 
                  (weights["duration"] * duration_similarity)) 

    return final_score

def find_best_match(tracks: list[dict], audio_file: str, SCORE_CUTOFF = 0.80):
    candidates = []

    # after i do find the best match. i need to get the original audio_file_name so i can rename it
    # but how am i supposed to get the original audio_file_name from the normalized_file_name...?
    # ugh i guess i need to make a Track class, and a File class

    for track in tracks:
        if compute_match_score(track, audio_files) >= SCORE_CUTOFF:
            candidates.append[track]
    return candidates[-1] if candidates else None

    # what the fuck??? ternary operator AND list comprehension? 
    # return [track if compute_match_score(track, audio_file) >= SCORE_CUTOFF][-1] if [track if compute_match_score(track, audio_file) >= SCORE_CUTOFF] else None

if __name__ == "__main__":
    song_name = "City Girl - HEARTBREAKER CLUB.mp3"
    audio_files = ['Cement City - Here Comes a Thought.mp3', 'Chevy - UWU (Band Version).mp3', 'Chevy - UWU.mp3', 'City Girl - HEARTBREAKER CLUB.mp3', 'Claire Rosinkranz - Backyard Boy.mp3', "Hyper_Potions_K_K_Cruisin'_From__Animal_Crossing_.mp3", 'Lilypichu - dreamy night.mp3', 'Makzo - Blossom.mp3', 'Mindy Gledhill - I Do Adore.mp3', 'mxmtoon - fever dream (Shawn Wasabi remix).mp3', 'potsu - just friends.mp3', 'Wave Racer - Higher.mp3', '달콤한꿈 - 꽃날 (황진이 OST).mp3']
    
    audio_files = normalize_audiofiles(audio_files)
    print(audio_files)