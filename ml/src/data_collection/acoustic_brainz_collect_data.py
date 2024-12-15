import requests
import pandas as pd
# Base URL for MusicBrainz API
BASE_URL = "https://musicbrainz.org/ws/2/"


track_names = ['Blinding Lights', 'Shape of You', 'Someone You Loved']


# Search for a track (recording)
def search_track(track_name, artist_name=None):
    endpoint = "recording"  # The specific endpoint for recordings (tracks)
    query = f'"{track_name}"'  # Enclose track name in quotes for exact match

    if artist_name:
        query += f' AND artist:"{artist_name}"'  # Add artist name if provided

    params = {
        "query": query,  # Search query
        "fmt": "json"  # Response format (json or xml)
    }
    headers = {
        "User-Agent": "YourAppName/1.0 (your-email@example.com)"
    }

    response = requests.get(BASE_URL + endpoint, params=params, headers=headers)
    data = response.json()
    recordings = data.get("recordings", [])  # Get the list of recordings
    if recordings:  # Check if there are results
        return recordings[0]  # Return the first result
    else:
        return {"error": "No recordings found"}

    # if response.status_code == 200:
    #     return response.json()  # Return JSON response
    # else:
    #     return {"error": f"Request failed with status code {response.status_code}"}


# Collect data for each track
def build_dataset():
    dataset = []
    for track_name in track_names:
        data = search_track(track_name)
        if data:
            dataset.append(data)

    # Convert to DataFrame
    df = pd.DataFrame(dataset)
    return df


# Save to CSV
# df.to_csv('deezer_tracks.csv', index=False)

