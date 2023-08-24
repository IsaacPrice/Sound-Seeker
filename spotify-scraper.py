import spotipy
import string
import time
import pickle as pk
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'ad6f915a353c47c7960ef96531a990f8'
client_secret = 'f84b389526234469a208f2a0e40f5063'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
'''
# Alphabet for search queries
alphabet = list(string.ascii_lowercase)

# List to store all tracks
all_tracks = []

for letter in alphabet:
    # Iterate over alphabet for broad search queries
    results = sp.search(q=letter, type='track', limit=50)
    
    tracks = results['tracks']['items']
    for track in tracks:
        all_tracks.append(track)

    # Fetch additional pages of results
    while results['tracks']['next']:
        results = sp.next(results['tracks'])
        tracks = results['tracks']['items']
        
        for track in tracks:
            all_tracks.append(track)

        # Check if we've fetched enough songs for this letter
        if len(all_tracks) >= 10000000:
            break

        # Be nice to the Spotify API and don't hit the rate limit
        time.sleep(0.1)

def remove_duplicates(tracks):
    seen = set()
    unique_tracks = []

    for track in tracks:
        if track['id'] not in seen:
            unique_tracks.append(track)
            seen.add(track['id'])

    return unique_tracks

# Remove duplicates
all_tracks = remove_duplicates(all_tracks)
with open('model_pickle', 'wb') as f:
    pk.dump(all_tracks, f)
'''

with open('music','rb') as f:
    all_tracks = pk.load(f)

'''# Print unique tracks
for idx, track in enumerate(all_tracks):
    print(f"Track #{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
'''

length = len(all_tracks)

# Iterate through all of the songs and get the features of each song and combine them with the name and song artists into a pandas dataframe
# Create the empty dataframe
df = pd.DataFrame(columns=['name', 'artists', 'id', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'speechiness', 'tempo', 'valence'])

# Iterate through all of the songs and get the features of each song and combine them with the name and song artists into a pandas dataframe
for idx, track in enumerate(all_tracks):
    # Get the features of the song
    features = sp.audio_features(track['id'])[0]

    # Append the features to the dataframe
    df.loc[len(df.index)] = [
        track['name'],
        track['artists'][0]['name'],
        track['id'],
        features['acousticness'],
        features['danceability'],
        features['energy'],
        features['instrumentalness'],
        features['key'],
        features['liveness'],
        features['loudness'],
        features['mode'],
        features['speechiness'],
        features['tempo'],
        features['valence']
    ]

    # Be nice to the Spotify API and don't hit the rate limit
    time.sleep(0.1)

    # Show how many songs we've processed as a bar graph that moves
    print(f"Processed {idx + 1} songs: [{'=' * ((idx + 1) // int(length / 100))}{' ' * ((int(length / 100) - ((idx + 1) // (int(length / 100)))))}] {idx + 1}/10834", end='\r')

# Save the dataframe to a pickle file
df.to_pickle('music_w/Features.pkl')
