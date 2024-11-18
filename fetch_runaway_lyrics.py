import lyricsgenius

def fetch_kanye_runaway_lyrics(api_key):
    """Fetch and print the lyrics for Kanye West's 'Runaway'."""
    try:
        genius = lyricsgenius.Genius(api_key)
        song = genius.search_song("Runaway", "Kanye West")
        
        if song:
            print(f"\nLyrics of 'Runaway' by {song.artist}:\n")
            print(song.lyrics)
        else:
            print("Lyrics for 'Runaway' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Fetching Kanye West's 'Runaway' lyrics...")
    api_key = input("Enter your Genius API key: ")
    fetch_kanye_runaway_lyrics(api_key)
