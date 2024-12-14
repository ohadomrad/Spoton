import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

def get_config(env_file_path=find_dotenv()):
    load_dotenv(env_file_path)
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
    return client_id, client_secret, redirect_uri


def init_spotify(client_id, client_secret, redirect_uri):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read"
    ))

sp = init_spotify(*get_config())
track_ids = ['0VjIjW4GlUZAMYd2vXMi3b',
             '7qiZfU4dY1lWllzX7mPBI3',
             '7qEHsqek33rTcFNT9PFqLf']

# Function to fetch track details and audio features
def fetch_track_data(track_id):
    track_info = sp.track(track_id)
    #audio_features = sp.audio_features(track_id)[0]
    data = {
        'track_id': track_id,
        'track_name': track_info['name'],
        'artist': track_info['artists'][0]['name'],
        'album': track_info['album']['name'],
        'release_date': track_info['album']['release_date'],
        'popularity': track_info['popularity'],
        #'danceability': audio_features['danceability'],
        #'energy': audio_features['energy'],
        #'speechiness': audio_features['speechiness'],
        #'acousticness': audio_features['acousticness'],
        #'instrumentalness': audio_features['instrumentalness'],
        #'liveness': audio_features['liveness'],
        #'valence': audio_features['valence'],
        #'tempo': audio_features['tempo']
    }
    return data

# Collect data for each track
dataset = []
for track_id in track_ids:
    data = fetch_track_data(track_id)
    dataset.append(data)

# Convert to DataFrame
df = pd.DataFrame(dataset)
print(df)

# Save to CSV
#df.to_csv('', index=False)

