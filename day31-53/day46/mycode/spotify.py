import spotipy
from spotipy.oauth2 import SpotifyOAuth
YOUR_UNIQUE_CLIENT_ID = "649db6bd717f469a9ba086d48f364677"
YOUR_UNIQUE_CLIENT_SECRET ="24623171d7ea4eb7855763f681065ae3"
YOUR_SPOTIFY_DISPLAY_NAME = "BillBoard to spotify"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_UNIQUE_CLIENT_ID,
        client_secret=YOUR_UNIQUE_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=YOUR_SPOTIFY_DISPLAY_NAME,
    )
)
user_id = sp.current_user()["id"]

URL = "https://example.com/?code=AQAAjLyuXo1eC_-tLoIUKYUcXL0STVqP4-AWxhYDLSmHRcHAY3nmq7GpAxKbnU03osi6VKTxpEHKn5K8PfUzVCNeGcnROKYD8s1w_Rx1A-ajzy_81INB-X2GworZHV7zxLoaBvvXei7Thn9GnB01yqXnw1mv99D-x_23QjgNkAvssnhl-6_fjUuHBxoQ5JU"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")