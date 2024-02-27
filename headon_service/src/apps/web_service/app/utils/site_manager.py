
from typing import List
import yaml
from src.apps.web_service.app.models.city_weather import CityWeather
from src.apps.web_service.app.utils.open_weather_service import get_weather


class SiteManager():
    def __init__(self) -> None:
        self._sites: List[CityWeather] = []

    def add_site(self, name: str, lat: float, lon: float) -> List[CityWeather]:
        result = any(city.name == name and city.lat == lat and city.lon == lon for city in self._sites)
        if not result:
            self._sites.append(CityWeather(name=name, lat=lat, lon=lon))
        return self.refresh_sites()
    
    @property
    def sites(self) -> List[CityWeather]:
        return [site.geojson_describe for site in self._sites]

    def refresh_sites(self) -> List[CityWeather]:
        try:
            self._sites = list(map(lambda city: self.update_city(city), self._sites))
            return self._sites
        except Exception as e:
            return False
    
    def update_city(self, city: CityWeather) -> CityWeather:
        city.temp = get_weather(lat=city.lat, lon=city.lon)
        return city

    def load_config(self, config_file_path: str) -> None:
        with open(config_file_path, 'r') as file:
            config = yaml.safe_load(file)

            # Access configuration values
            CITY_1_NAME = config['CITY_1']['name']
            CITY_1_LAT = config['CITY_1']['lat']
            CITY_1_LON = config['CITY_1']['lon']
            self.add_site(name=CITY_1_NAME, lat=CITY_1_LAT, lon=CITY_1_LON)

            CITY_2_NAME = config['CITY_2']['name']
            CITY_2_LAT = config['CITY_2']['lat']
            CITY_2_LON = config['CITY_2']['lon']
            self.add_site(name=CITY_2_NAME, lat=CITY_2_LAT, lon=CITY_2_LON)

            CITY_3_NAME = config['CITY_3']['name']
            CITY_3_LAT = config['CITY_3']['lat']
            CITY_3_LON = config['CITY_3']['lon']
            self.add_site(name=CITY_3_NAME, lat=CITY_3_LAT, lon=CITY_3_LON)

            CITY_4_NAME = config['CITY_4']['name']
            CITY_4_LAT = config['CITY_4']['lat']
            CITY_4_LON = config['CITY_4']['lon']
            self.add_site(name=CITY_4_NAME, lat=CITY_4_LAT, lon=CITY_4_LON)

            CITY_5_NAME = config['CITY_5']['name']
            CITY_5_LAT = config['CITY_5']['lat']
            CITY_5_LON = config['CITY_5']['lon']
            self.add_site(name=CITY_5_NAME, lat=CITY_5_LAT, lon=CITY_5_LON)

    