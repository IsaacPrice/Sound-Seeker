import spotipy
import string
import time
import pickle as pk
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

with open('model_pickle','rb') as f:
    all_tracks = pk.load(f)

# Print unique tracks
for idx, track in enumerate(all_tracks):
    print(f"Track #{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
