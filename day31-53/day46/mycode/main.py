import requests
from bs4 import BeautifulSoup
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

date = input("whch your you want to travel!(enter in YYYY-MM-DD FORMAT)")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

resp = requests.get(url=URL)
website_text = resp.text
website_data = BeautifulSoup(website_text, "html.parser")
# print(website_data)
print(website_data("title"))

ALL_RESULTS_TABLE_CLASS = "chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max"

# all_results = website_data.find_all(name="div", class_= ALL_RESULTS_TABLE_CLASS)
# print(all_results)
all_list_class = "o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max"
all_names_of_songs = website_data.find_all(name="li",class_ =all_list_class)
# print(all_names_of_songs)

names_of_songs =[]
singers_of_songs = []
i =0;
with open("top100songs_ofyear.txt", "w") as file:
    file.write("song number:songname::song_singer\n")

for each_song in all_names_of_songs:
    song_name = each_song.find("h3").getText().strip()
    song_singer = each_song.find("span").getText().replace("\n","").replace("\t","")
    names_of_songs.append(song_name)
    singers_of_songs.append(song_singer)
    try:
        with open("top100songs_ofyear.txt", "a") as file:
            file.write(f"{i}:{song_name}::{song_singer}\n")
    except Exception as e:
        print("execption is"+ e)
    finally:
        pass
    i=i+1;
# print(names_of_songs)
# print(singers_of_songs)


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = names_of_songs

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

PLAYLIST_ID = sp.user_playlist_create(user=user_id,public=False,name=f"{date} BillBoard-100")['id']

# sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=song_uris,user=user_id)
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=song_uris)