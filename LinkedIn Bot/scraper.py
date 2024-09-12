import os
from time import sleep
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for File I/O
OUTPUT_FILE = 'output1.csv'
HEADERS = ['Name', 'Job Title', 'Location', 'URL']

# Abstract Factory Pattern: ProfileFactory for creating profile parsers
class ProfileFactory:
    @staticmethod
    def create_profile_parser(driver):
        return ProfileParser(driver)

# Singleton Pattern: WebDriverManager controls WebDriver's singleton instance
class WebDriverManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = webdriver.Chrome()
        return cls._instance

# ProfileParser handles profile data extraction
class ProfileParser:
    def __init__(self, driver):
        self.driver = driver

    def parse_profiles(self, urls):
        profiles_data = []
        for url in urls:
            self.driver.get(url)
            sleep(2)
            page_source = BeautifulSoup(self.driver.page_source, "html.parser")
            profile_data = self.extract_profile_data(page_source)
            if profile_data:
                profiles_data.append(profile_data)
        return profiles_data

    def extract_profile_data(self, page_source):
        try:
            name = self.get_text(page_source, 'h1', 'text-heading-xlarge')
            title = self.get_text(page_source, 'div', 'text-body-medium')
            location = self.get_text(page_source, 'span', 'text-body-small')
            return {'Name': name, 'Title': title, 'Location': location, 'URL': self.driver.current_url}
        except Exception:
            return None

    @staticmethod
    def get_text(page_source, tag, class_name):
        element = page_source.find(tag, class_=class_name)
        return element.get_text(strip=True) if element else 'N/A'

# LinkedInScraper orchestrates the login and scraping process
class LinkedInScraper:
    def __init__(self):
        self.driver = WebDriverManager()
        self.login()

    def login(self):
        self.driver.get('https://www.linkedin.com/home')
        sleep(3)
        email_field = self.driver.find_element('id', 'session_key')
        email_field.send_keys(os.getenv('LINKEDIN_EMAIL'))
        sleep(3)
        password_field = self.driver.find_element('name', 'session_password')
        password_field.send_keys(os.getenv('LINKEDIN_PASSWORD'))
        sleep(3)
        login_field = self.driver.find_element('xpath', '//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button')
        login_field.click()
        sleep(3)

    def search_profiles(self, search_query):
        search_field = self.driver.find_element('xpath', '//*[@id="global-nav-typeahead"]/input')
        search_field.send_keys(search_query)
        sleep(3)
        search_field.send_keys(Keys.RETURN)
        sleep(3)
        people_link = self.driver.find_element('xpath', '//a[contains(@href, "/search/results/people/") and contains(text(), "See all people results")]')
        people_link.send_keys(Keys.RETURN)
        sleep(4)

    def get_profile_urls(self, pages):
        profile_list = []
        for _ in range(pages):
            profile_urls = self.extract_profile_urls()
            profile_list.extend(profile_urls)
            self.scroll_to_next()
        return profile_list

    def extract_profile_urls(self):
        page_source = BeautifulSoup(self.driver.page_source, "html.parser")
        profiles = page_source.find_all('a', class_='app-aware-link')
        return [profile['href'] for profile in profiles if "/in/" in profile['href']]

    def scroll_to_next(self):
        sleep(2)
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        next_button = self.driver.find_element('xpath', '//button[@aria-label="Next"]')
        self.driver.execute_script("arguments[0].click();", next_button)
        sleep(2)

def main():
    search_query = input('What profile you want to scrape? ')
    number_of_pages = int(input("Enter number of pages you want to scrape: "))
    
    scraper = LinkedInScraper()
    scraper.search_profiles(search_query)
    
    url_all_page = scraper.get_profile_urls(number_of_pages)

    parser = ProfileFactory.create_profile_parser(scraper.driver)

    # Write profiles to CSV
    with open(OUTPUT_FILE, 'w', newline='') as file_output:
        writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n', fieldnames=HEADERS)
        writer.writeheader()
        profiles_data = parser.parse_profiles(url_all_page)
        for profile in profiles_data:
            writer.writerow(profile)
            print('--- Profile:', profile)

    print('Mission Completed!')

if __name__ == '__main__':
    main()
