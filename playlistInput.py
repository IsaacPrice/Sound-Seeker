import pandas as pd
import pickle as pk

# This function will read a given list of tracks, along with the song the user wants, and return the top ten most relevant song search results
def parse_songs(songs, song):
    pass

# Read the pickle file named 'music' into a pandas dataframe
df = pd.read_pickle('music')

while True:
    # Prompt the user for a song
    song = input("Enter a favorite song: ")

    # Create the list to hold one song's features
    song_features = []

    # Check if

