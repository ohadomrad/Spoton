from ytmusicapi import YTMusic
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv
import os

def get_config(env_file_path=find_dotenv()):
    load_dotenv(env_file_path)
    api_key = os.getenv("GOOGLE_API_KEY")
    return api_key


def init_apis(api_key):
    # Initialize YTMusic client
    ytmusic = YTMusic()

    # Initialize YouTube Data API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    return ytmusic, youtube
# List of track names to search
track_names = ['Blinding Lights', 'Shape of You', 'Someone You Loved']

ytmusic, youtube = init_apis(get_config())

# Function to fetch track details
def fetch_track_data(track_name):
    search_results = ytmusic.search(track_name, filter='songs')
    if search_results:
        track_info = search_results[0]
        video_id = track_info['videoId']
        # Fetch video statistics from YouTube Data API
        video_response = youtube.videos().list(part='statistics', id=video_id).execute()
        if video_response['items']:
            stats = video_response['items'][0]['statistics']
            data = {
                'track_title': track_info['title'],
                'artist_name': track_info['artists'][0]['name'],
                'album_title': track_info['album']['name'] if 'album' in track_info else None,
                'duration': track_info['duration'],
                'video_id': video_id,
                'is_explicit': track_info.get('isExplicit', False),
                'view_count': int(stats.get('viewCount', 0)),
                'like_count': int(stats.get('likeCount', 0)),
                'dislike_count': int(stats.get('dislikeCount', 0))  # Note: YouTube has deprecated public dislike counts
            }
            return data
    return None

# Collect data for each track
dataset = []
for track_name in track_names:
    data = fetch_track_data(track_name)
    if data:
        dataset.append(data)

# Convert to DataFrame
df = pd.DataFrame(dataset)
print(df)

# Save to CSV
#df.to_csv('ytmusic_tracks.csv', index=False)
