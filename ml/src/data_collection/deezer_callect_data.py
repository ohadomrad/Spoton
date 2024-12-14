import deezer
import pandas as pd

# Initialize the Deezer client
client = deezer.Client()

track_names = ['Blinding Lights', 'Shape of You', 'Someone You Loved']

# Function to fetch track details
def fetch_track_data(track_name):
    # Search for the track by name
    search_results = client.search(track_name)
    if search_results:
        # Assume the first result is the desired track
        track = search_results[0]
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
    else:
        print(f"No results found for {track_name}")
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
# df.to_csv('deezer_tracks.csv', index=False)

