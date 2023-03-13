import os
from pathlib import Path
from unicodedata import name
import lyricsgenius
import sys
"""
the data folder contains txt files with rapper's names, the songs folder contains all of the songs from a single group of artists
wutang.txt (10 members) - > wutang.txt 1 files with all of their songs.
"""
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
#TODO: mulithreaded implemetation
class Genius:
    def __init__(self, client_access_token, timeout, retries, songs_foldername = 'songs'):
        self.songs_foldername = songs_foldername
        self._api_ = lyricsgenius.Genius(client_access_token, timeout=timeout, retries=retries)
    def scrape_artist(self, artist_name: str):
        #you can pass a max_songs (or smth like that) parameter here to stop downloading songs after a certain number
        artist = self._api_.search_artist(artist_name)
        print(f"stvaram file {artist.name.strip()}")
        f = open(Path(self.songs_foldername, f'{artist.name.strip()}.txt'), 'w')  
        for song in artist.songs:
            f.write("\n" + '*'*50 + "\n")
            f.write(song.title)
            f.write(song.lyrics)
        f.close()
        print(f"done with {artist_name}")

#it loads rapper's names from the filename and then downloads all of their songs
filename = 'Lilgpt.txt'
songs_folder = Path(ROOT_DIR, 'songs', filename[:-4])
genius = Genius('2BblA-jJIKZjF4ZbS04pchSYyJ2e7Fyse0RZe9SQMEwVaDFRXfQ42wxzJ4Xpu0dc', songs_foldername = songs_folder, timeout = 15, retries = 30)
try:
    os.makedirs(songs_folder)
except:
    pass #folder already exists irrelevant error tbh
with open(Path(ROOT_DIR, 'data', filename)) as f:
    for rapper in [line.strip() for line in f.readlines()]:
        genius.scrape_artist(rapper)