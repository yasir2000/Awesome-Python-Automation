import requests
import os

class UrlShortener:
    def shorten_url(self, long_url):
        pass

class TinyUrlShortener(UrlShortener):
    def shorten_url(self, long_url):
        url = f'http://tinyurl.com/api-create.php?url={long_url}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

class UrlShorteningServiceFactory:
    @staticmethod
    def get_url_shortening_service():
        # Depending on the configuration or environment, this method can return different URL shortening services.
        return TinyUrlShortener()

class HttpClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance

def main():
    long_url = os.getenv("LONG_URL")
    
    url_shortener = UrlShorteningServiceFactory.get_url_shortening_service()
    short_url = url_shortener.shorten_url(long_url)

    if short_url:
        print(f'Shortened URL: {short_url}')
    else:
        print('Error shortening URL')

if __name__ == "__main__":
    main()
