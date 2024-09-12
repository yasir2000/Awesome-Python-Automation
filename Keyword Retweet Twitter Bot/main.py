# Import necessary libraries
import os
import time
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TwitterAPI:
    """Facade class to interact with the Twitter API."""
    def __init__(self):
        self.api = self.authenticate()

    def authenticate(self):
        """Authenticate and return the tweepy API object."""
        apic = os.getenv('API_CODE')
        apisc = os.getenv('API_SECRET_CODE')
        acc = os.getenv('ACCOUNT_CODE')
        acsc = os.getenv('ACCOUNT_SECRET_CODE')

        auth = tweepy.OAuthHandler(apic, apisc)
        auth.set_access_token(acc, acsc)
        return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class RetweetManager:
    """Handles retweeting functionality."""
    def __init__(self, api):
        self.api = api
        self.count = 0
        self.bot_file = "bot.txt"

    def load_count(self):
        """Load the current retweet count from a file."""
        if os.path.exists(self.bot_file):
            with open(self.bot_file, "r") as f:
                self.count = int(f.read().strip())
        else:
            self.count = 0
        
    def save_count(self):
        """Save the current retweet count to a file."""
        with open(self.bot_file, "w") as f:
            f.write(str(self.count))

    def retweet(self, search_term, nrtweets):
        """Retweet tweets that match the search term."""
        for tweet in tweepy.Cursor(self.api.search, search_term).items(nrtweets):
            try:
                print(f"Tweet number {self.count} retweeted")
                tweet.retweet()
                self.count += 1
                time.sleep(30)
                print(f"RETWEETED: {self.count}")
                self.save_count()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def main():
    """Main executable function."""
    twitter_api = TwitterAPI()
    retweet_manager = RetweetManager(twitter_api.api)

    retweet_manager.load_count()
    search_term = input("Enter the keyword to be searched: ")
    nrtweets = 500
    retweet_manager.retweet(search_term, nrtweets)

if __name__ == '__main__':
    main()
