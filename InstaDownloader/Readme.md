# INSTA DOWNLOADER
### Downloads posts from Private and Public profiles on Instagram

This python code takes user input for private and public profiles to download required posts.

#### Requirements:
* Install instaloader
* run `pip install instaloader` or `pip3 install instaloader`

### Usage
* Clone the repo
* open the `InstaDownloader` folder
##### for windows
* run `python insta_down.py`
##### for linux
* run `python3 insta_down.py`

### Important
* Please enter the post code only for the desired post
* You might face errors if you are downloading from a private profile without logging in
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### .env File Example

```plaintext
# .env file
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

### Explanation

1. **Single Responsibility Principle**: Each class has a single responsibility:
   - `ConnectionManager` checks connection status.
   - `InstaLoaderFactory` creates the `Instaloader` instance.
   - `PostDownloader` handles downloading posts.
   - `UserInterface` manages user interactions.
   - `App` orchestrates the overall application flow.

2. **Open-Closed Principle**: Classes are open for extension (you can add more functionality) but closed for modification.

3. **Liskov Substitution Principle**: Objects of parent class can be replaced with objects from subclasses without affecting the functionality.

4. **Dependency Injection**: The application uses dependency injection to provide instances of classes, making it easier to manage dependencies.

5. **Specific Design Patterns**: 
   - **Factory Pattern**: Used in `InstaLoaderFactory` to create the `Instaloader` instance.
   - **Facade Pattern**: The `App` class works as a facade to simplify interaction among components.
   - **Strategy Pattern**: The `UserInterface` allows different ways of getting user input.
