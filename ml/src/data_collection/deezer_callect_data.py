import deezer
import pandas as pd

# Initialize the Deezer client
client = deezer.Client()

# List of track IDs to fetch
track_ids = [3135556, 1111111, 2222222]  # Replace with actual track IDs

# Function to fetch track details
def fetch_track_data(track_id):
    track = client.get_track(track_id)
    data = {
        'track_id': track.id,
        'track_title': track.title,
        'artist_name': track.artist.name,
        'album_title': track.album.title,
        'duration': track.duration,
        'explicit_lyrics': track.explicit_lyrics,
        'rank': track.rank,
        'release_date': track.release_date,
        'bpm': track.bpm,
        'gain': track.gain,
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
#df.to_csv('deezer_tracks.csv', index=False)
