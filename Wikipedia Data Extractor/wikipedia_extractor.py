# wikipedia_client.py
import os
import wikipedia

class WikipediaClient:
    def __init__(self, language=None):
        self.language = language or os.getenv('DEFAULT_LANGUAGE')
        wikipedia.set_lang(self.language)

    def get_summary(self, topic):
        return wikipedia.summary(topic)

    def get_page_summary(self, page_title):
        page = wikipedia.page(page_title)
        return page.summary
# search_handler.py
class SearchHandler:
    def __init__(self, wikipedia_client):
        self.wikipedia_client = wikipedia_client

    def search_topic(self, topic):
        return self.wikipedia_client.get_summary(topic)

    def search_page_summary(self, page_title):
        return self.wikipedia_client.get_page_summary(page_title)
# main.py

# Load environment variables


def main():
    language = os.getenv('DEFAULT_LANGUAGE')
    
    # Initialize the Wikipedia Client
    wikipedia_client = WikipediaClient(language)
    
    # Initialize the Search Handler
    search_handler = SearchHandler(wikipedia_client)
    
    # User interaction
    search = input("Enter the topic you want: ")
    print(search_handler.search_topic(search))

    print(f"Summary of Open Source in {language}:", search_handler.search_page_summary("Open Source"))

if __name__ == "__main__":
    main()
