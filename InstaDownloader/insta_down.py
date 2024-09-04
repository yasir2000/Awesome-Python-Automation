import os
import instaloader
import requests
import sys
from instaloader import Post
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class ConnectionManager:
    @staticmethod
    def check_connection(url='http://www.google.com/', timeout=5):
        """ Check if there is an internet connection. """
        try:
            req = requests.get(url, timeout=timeout)
            req.raise_for_status()
            print("You're connected to the internet\n")
            return True
        except requests.HTTPError as e:
            print(f"Checking internet connection failed, status code {e.response.status_code}.")
        except requests.ConnectionError:
            print("No internet connection available.")
        return False


class InstaLoaderFactory:
    @staticmethod
    def create_instaloader():
        """ Create an instance of Instaloader. """
        return instaloader.Instaloader()


class PostDownloader:
    def __init__(self, loader):
        self.loader = loader

    def download_post(self, target_username, post_code):
        """ Download the specified Instagram post. """
        profile = instaloader.Profile.from_username(self.loader.context, target_username)
        post = Post.from_shortcode(self.loader.context, post_code)
        self.loader.download_post(post, target=target_username)


class UserInterface:
    @staticmethod
    def display_menu():
        """ Display the menu options to the user. """
        menu_text = (
            "Press 'A' to download an Instagram post from a private profile.\n"
            "Press 'B' to download an Instagram post from a public profile.\n"
            "Press 'Q' to exit."
        )
        print(menu_text)

    @staticmethod
    def get_user_selection():
        """ Get selection from the user. """
        return str(input("\nInstaSave > ")).upper()


class App:
    def __init__(self, connection_manager, loader_factory, downloader, ui):
        self.connection_manager = connection_manager
        self.loader_factory = loader_factory
        self.downloader = downloader
        self.ui = ui
        self.loader = loader_factory.create_instaloader()

    def run(self):
        if self.connection_manager.check_connection():
            try:
                while True:
                    self.ui.display_menu()
                    select = self.ui.get_user_selection()
                    self.process_selection(select)
            except KeyboardInterrupt:
                print("\nProgramme Interrupted")
        else:
            sys.exit()

    def process_selection(self, select):
        if select == 'A':
            username = os.getenv('IG_USERNAME')
            password = os.getenv('IG_PASSWORD')
            self.loader.login(username, password)
            target_username = input("Enter the target insta username: ")
            post_code = input("Enter the post code for the media (Please don't enter the URL - only code): ")
            self.downloader.download_post(target_username, post_code)
            print("Post downloaded successfully")
        elif select == 'B':
            target_username = input("Enter the target insta username: ")
            post_code = input("Enter the post code for the media (Please don't enter the URL - only code): ")
            self.downloader.download_post(target_username, post_code)
            print("Post downloaded successfully")
        elif select == 'Q':
            sys.exit()
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    connection_manager = ConnectionManager()
    loader_factory = InstaLoaderFactory()
    downloader = PostDownloader(loader_factory.create_instaloader())
    ui = UserInterface()
    app = App(connection_manager, loader_factory, downloader, ui)
    app.run()
