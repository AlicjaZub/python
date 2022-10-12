import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
import os

# Scraping Billboard 100
date = input("What year would you like to travel to? Type the date inthis format YYYY-MM-DD ")
year = date[:4]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
top_100 = response.text

soup = BeautifulSoup(top_100, 'html.parser')
items = soup.find_all("li", class_="o-chart-results-list__item")

songs = []

for song in items:
  song = song.find("h3")
  if song is not None:
    songs.append(song.getText().strip())

#Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
  scope="playlist-modify-private",
  redirect_uri="https://example.com",
  client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
  client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
  show_dialog=True,
  cache_path="token.txt"
  ))
user_id = sp.current_user()["id"]
song_uris = []

#Searching Spotify for songs by title
for song in songs:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  try:
    song_uris.append(result["tracks"]["items"][0]["uri"])
  except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")
    
#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
