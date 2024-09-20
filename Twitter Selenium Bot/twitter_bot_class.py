from selenium import webdriver
from selenium import common
from selenium.webdriver.common import keys
from webdriver_manager.firefox import GeckoDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

class WebDriver:
    """
    Singleton class to manage a single WebDriver instance.
    """
    _instance = None

    @staticmethod
    def get_driver():
        if WebDriver._instance is None:
            WebDriver._instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return WebDriver._instance

class TwitterAuthenticator:
    """
    Handles logging in and logging out of Twitter.
    Implements the Template Method pattern.
    """
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def login(self):
        self.driver.get('https://twitter.com/')
        time.sleep(4)
        self._perform_login()

    def logout(self):
        self.driver.get('https://twitter.com/home')
        time.sleep(4)
        self._perform_logout()

    def _perform_login(self):
        try:
            email = self.driver.find_element_by_name('session[username_or_email]')
            password = self.driver.find_element_by_name('session[password]')
            email.clear()
            password.clear()
            email.send_keys(self.email)
            password.send_keys(self.password)
            password.send_keys(keys.Keys.RETURN)
            time.sleep(10)
        except common.exceptions.NoSuchElementException:
            print("Login elements not found.")

    def _perform_logout(self):
        try:
            self.driver.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
            time.sleep(3)
        except common.exceptions.NoSuchElementException:
            print("Logout elements not found.")


class TwitterActions:
    """
    Abstract class offering Twitter actions.
    """
    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        """
        Search for a provided query.
        """
        searchbox = self.driver.find_element_by_xpath("//input[@data-testid='SearchBox_Search_Input']")
        searchbox.clear()
        searchbox.send_keys(query)
        searchbox.send_keys(keys.Keys.RETURN)
        time.sleep(10)

    def post_tweet(self, tweet_body):
        """
        Post a tweet.
        """
        self.driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
        time.sleep(4)
        tweet_box = self.driver.find_element_by_xpath("//div[@role='textbox']")
        tweet_box.send_keys(tweet_body)
        time.sleep(4)
        self.driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        time.sleep(4)


class LikeTweetHandler:
    """
    Handles liking tweets.
    """
    def __init__(self, driver):
        self.driver = driver

    def like_tweets(self, cycles=10):
        """
        Loop over a number of cycles to like tweets.
        """
        for _ in range(cycles):
            try:
                self.driver.find_element_by_xpath("//div[@data-testid='like']").click()
            except common.exceptions.NoSuchElementException:
                self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)')
                time.sleep(3)
                self.driver.find_element_by_xpath("//div[@data-testid='like']").click()
            time.sleep(1)
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)')
            time.sleep(5)


class TwitterBot:
    """
    Facade for easy interaction with Twitter bot functionalities.
    """
    def __init__(self, email, password):
        self.driver = WebDriver.get_driver()
        self.authenticator = TwitterAuthenticator(self.driver, email, password)
        self.actions = TwitterActions(self.driver)
        self.like_handler = LikeTweetHandler(self.driver)

    def login(self):
        self.authenticator.login()

    def logout(self  
