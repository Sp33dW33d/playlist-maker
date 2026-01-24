from dotenv import load_dotenv
import os

from src import api 
from src import files

def get_api_keys():
    global CLIENT_ID, CLIENT_SECRET
    load_dotenv()
    CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET") 

if __name__ == "__main__":
    get_api_keys()

    link = "https://open.spotify.com/playlist/6vAVp8M1el9CLRe251q9Mg"
    PLAYLIST_ID = api.get_playlist_id(link)
    ACCESS_TOKEN = api.get_token(CLIENT_ID, CLIENT_SECRET)

    tracks = api.get_tracklist(PLAYLIST_ID, ACCESS_TOKEN)
    print(tracks)

    # playlist_name = pm.sanitize_filename(get_playlist_name(PLAYLIST_ID, ACCESS_TOKEN))
    # if generate_playlist_file(playlist_name, tracks):
    #     print("Playlist file generated successfully")
