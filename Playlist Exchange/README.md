<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spotify-Youtube-Music-Exchange</title>
</head>

<body>

  <h1>Spotify-Youtube-Music-Exchange</h1>

  <p>This Python script allows you to exchange songs and playlists between Spotify and YouTube Music.</p>

  <h2>Requirements</h2>

  <p>Make sure you have the following libraries installed:</p>

  <ul>
    <li><a href="https://pypi.org/project/fuzzywuzzy/" target="_blank">fuzzywuzzy==0.18.0</a></li>
    <li><a href="https://pandas.pydata.org/" target="_blank">pandas==1.3.2</a></li>
    <li><a href="https://docs.python-requests.org/en/master/" target="_blank">requests==2.31.0</a></li>
    <li><a href="https://spotipy.readthedocs.io/en/2.23.0/" target="_blank">spotipy==2.23.0</a></li>
    <li><a href="https://ytmusicapi.readthedocs.io/en/stable/" target="_blank">ytmusicapi==1.3.2</a></li>
  </ul>

  <p>You can install these libraries using the following command:</p>

  <pre><code>pip install fuzzywuzzy==0.18.0 pandas==1.3.2 requests==2.31.0 spotipy==2.23.0 ytmusicapi==1.3.2</code></pre>

  <h2>Setup "header_auth.json" (Browser Authentication) on local system:</h2>

  <ol>
    <li>Follow the <a href="https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html" target="_blank">documentation link</a> to set up "header_auth.json" for Browser Authentication.</li>
    <li>Save the generated "header_auth.json" file in the root directory of this project.</li>
  </ol>

  <h2>Usage</h2>

  <ol>
    <li>Clone the repository:</li>
  </ol>

  <pre><code>git clone https://github.com/yourusername/Spotify-Youtube-Music-Exchange.git
cd Spotify-Youtube-Music-Exchange</code></pre>

  <ol start="2">
    <li>Install the required libraries:</li>
  </ol>

  <pre><code>pip install -r requirements.txt</code></pre>

  <ol start="3">
    <li>Run the script:</li>
  </ol>

  <pre><code>python playlistexchange.py</code></pre>

  <p>Follow the on-screen instructions to exchange songs and playlists between Spotify and YouTube Music.</p>

  <h2>Contributing</h2>

  <p>If you'd like to contribute to this project, please fork the repository and submit a pull request. Issues and feature requests are welcome!</p>

  <h2>License</h2>

  <p>This project is licensed under the MIT License - see the <a href="LICENSE" target="_blank">LICENSE</a> file for details.</p>

</body>

</html>

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### Refactored Code

We'll include environmental variables, proper class definitions, and incorporate relevant design patterns.

#### .env file Example
```plaintext
SPOTIFY_CLIENT_ID=f23579cc015b4e518158755fd63d46fc
SPOTIFY_CLIENT_SECRET=9dd9fb72962e4c3f9d42474c0142313a
SCOPE=playlist-modify-public
REDIRECT_URI=http://localhost:8080
```

### Explanation of the Refactor
1. **Single Responsibility Principle**: Each class has a single responsibility:
   - `YTTrackFetcher` fetches tracks from YouTube Music.
   - `SpotifyAuthenticator` handles Spotify authentication and playlist creation.
   - `SpotifyTrackMatcher` finds matching Spotify tracks based on input tracks.
   - `SpotifyPlaylistManager` handles the addition of tracks to the Spotify playlist.

2. **Open-Closed Principle**: The current design allows for easy extension without modifying existing classes, e.g., if additional features are required.

3. **Liskov Substitution Principle**: Any subclasses of the above classes could be created without breaking the function of the program, as they follow the same interface.

4. **Inversion of Control**: Dependencies are passed via constructors, which allows for easier testing and modifications.

5. **Dependency Injection**: Dependencies such as `YTMusic`, `Spotify` instances are injected into the classes, allowing for greater flexibility.

6. **GoF Design Patterns**: The refactor leverages design patterns like:
   - **Factory Method** in `SpotifyAuthenticator` for creating a Spotify instance.
   - **Adapter Pattern** is implied in the matching process using fuzzy matching.
   - Encapsulation of different responsibilities into different classes corresponds to **Facade**, providing a simplified access point.

This modular structure makes the code easier to maintain, test, and extend. 