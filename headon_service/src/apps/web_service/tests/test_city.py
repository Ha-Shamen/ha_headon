# test_my_module.py
import unittest
from src.apps.web_service.app.models.city_weather import CityWeather

class TestAddNumbers(unittest.TestCase):
    
    def test_city_weather(self):

        city_weather = CityWeather('name', 1.1, 1.1)
        self.assertIsNone(city_weather.temp)


if __name__ == '__main__':
    unittest.main()
