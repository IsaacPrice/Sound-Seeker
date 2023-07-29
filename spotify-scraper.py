import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the session
client_credentials_manager = SpotifyClientCredentials(client_id='ad6f915a353c47c7960ef96531a990f8', client_secret='f84b389526234469a208f2a0e40f5063')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ID of the song for which you want to get the audio features
track_id = '7rbECVPkY5UODxoOUVKZnA'  # Replace with your track's ID

# Get the audio features of the song
features = sp.audio_features(track_id)

# Print the features
print(features)