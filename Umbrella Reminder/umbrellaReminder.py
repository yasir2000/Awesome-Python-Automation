from abc import ABC, abstractmethod
import os

class WeatherProvider(ABC):
    @abstractmethod
    def get_weather_info(self) -> dict:
        pass

class GoogleWeatherProvider(WeatherProvider):
    def __init__(self, city):
        self.city = city

    def get_weather_info(self) -> dict:
        url = f"https://www.google.com/search?q=weather+{self.city}"
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        sky = time_sky.split('\n')[1]
        return {'temperature': temperature, 'sky': sky}

class WeatherProviderFactory:
    def get_provider(self, city):
        return GoogleWeatherProvider(city)
