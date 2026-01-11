import pickle
import requests as req
import json
import keys

def error_catcher(base_fn):
    def enhanced_fn(*args, **kwargs):
        response = base_fn(*args, **kwargs)
        if response.status_code == 200:
            return response
        else:
            return f"Error:, {response.status_code}, {response.text}"
    return enhanced_fn


def get_token():
    global ACCESS_TOKEN
    
    CLIENT_ID = keys.CLIENT_ID
    CLIENT_SECRET = keys.CLIENT_SECRET
    SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
    HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    DATA = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
    }
    response = req.post(url = SPOTIFY_TOKEN_URL, headers = HEADERS, data = DATA)
    
    if response.status_code == 200:
      ACCESS_TOKEN = response.json()['access_token']
    else:
      print("Error:", response.status_code, response.text)

def get_tracklist(playlist_id = None):
    playlist_id = ""
    playlist = req.get(url = f"https://api.spotify.com/v1/playlists/{playlist_id}", headers = AUTH_TOKEN)
    
    if playlist.status_code == 200:
        print(playlist.json()["name"])
        print(playlist.json()["owner"]["display_name]"])
        print(playlist.json()["description"])
        print(playlist.json()["tracks"])
    else:
        print("Error:", playlist.status_code, playlist.text)


if __name__ == "__main__":
    # get_token()
    # print(ACCESS_TOKEN)
    # AUTH_TOKEN = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    print(keys.CLIENT_ID)