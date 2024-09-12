from dotenv import load_dotenv
import os
import re
import pandas as pd
import requests
import spotipy
import spotipy.util as util
from fuzzywuzzy import fuzz
from ytmusicapi import YTMusic as yt
import json


# Load environment variables
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SCOPE = os.getenv('SCOPE')
REDIRECT_URI = os.getenv('REDIRECT_URI')

class YTTrackFetcher:
    def __init__(self, ytmusic_instance):
        self.ytmusic = ytmusic_instance

    def get_tracks(self, playlist_yt):
        playlist_yt_details = self.ytmusic.get_playlist(playlist_yt, limit=1000)
        tracks_yt = playlist_yt_details['tracks']
        list_yt_tracks = [{
            'title': re.sub(r'$$[^()]*$$', '', track['title']).strip(),
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'] if track['album'] else 'None',
            'duration': track.get('duration', 'None')
        } for track in tracks_yt]
        return pd.DataFrame(list_yt_tracks)


class SpotifyAuthenticator:
    def __init__(self, username):
        self.username = username
        self.auth_mgr = util.prompt_for_user_token(
            self.username,
            SCOPE,
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=REDIRECT_URI
        )
        self.sp = spotipy.Spotify(auth=self.auth_mgr)

    def create_playlist(self, playlist_name, description):
        new_playlist_info = self.sp.user_playlist_create(self.username, playlist_name, description=description)
        return new_playlist_info['id']

    
class SpotifyTrackMatcher:
    def __init__(self, sp_instance, yt_tracks_df):
        self.sp = sp_instance
        self.yt_tracks_df = yt_tracks_df

    def find_matching_tracks(self):
        spotify_track_ids = []
        for index, track in self.yt_tracks_df.iterrows():
            results = self.sp.search(
                q=f"{track['title']} {track['artist']}",
                limit=5,
                type='track'
            )
            if results['tracks']['total'] > 0:
                for item in results['tracks']['items']:
                    item_name = re.sub(r'$$[^()]*$$', '', item['name']).strip()
                    if fuzz.partial_ratio(item_name, track['title']) > 90 and \
                       fuzz.partial_ratio(item['artists'][0]['name'], track['artist']) > 60:
                        spotify_track_ids.append(item['id'])
                        break
        return spotify_track_ids


class SpotifyPlaylistManager:
    def __init__(self, sp_instance):
        self.sp = sp_instance

    def add_tracks_to_playlist(self, playlist_id, track_ids):
        while track_ids:
            self.sp.user_playlist_add_tracks(
                self.sp.current_user()['id'],
                playlist_id,
                track_ids[:90]
            )
            track_ids = track_ids[90:]

def main():
    ytmusic = yt('headers_auth.json')

    user_profile = input("Enter the Library link of your profile: \n")
    user_yt = user_profile.split('/')[-1]

    playlist_link = input("Enter the Playlist link of your profile: \n")
    playlist_yt = playlist_link.split("=")[-1]

    yt_fetcher = YTTrackFetcher(ytmusic)
    df_yt_tracks = yt_fetcher.get_tracks(playlist_yt)

    spotify_username = input("Please enter your Spotify username url/uri/shareable link:\n").split('/')[-1]
    sp_auth = SpotifyAuthenticator(spotify_username)

    playlist_name = input("Give a name to your newly created playlist:\n")
    description = input("Please provide a description if any:\n")
    playlist_id = sp_auth.create_playlist(playlist_name, description)

    print("Finding the most accurate songs in Spotify Library\nIt might take a few minutes... Please wait :)")
    matcher = SpotifyTrackMatcher(sp_auth.sp, df_yt_tracks)
    spotify_songs_list = matcher.find_matching_tracks()

    playlist_manager = SpotifyPlaylistManager(sp_auth.sp)
    playlist_manager.add_tracks_to_playlist(playlist_id, spotify_songs_list)

    print("Songs added successfully! :)")


if __name__ == "__main__":
    main()
