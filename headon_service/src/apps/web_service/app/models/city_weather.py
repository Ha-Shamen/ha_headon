import typing


class CityWeather():
    def __init__(self, name: str, lat: float, lon: float) -> None:
        self.name = name
        self.lat = lat
        self.lon = lon
        self.temp = None
        
    @property
    def coordinates(self):
        return {'lat': self.lat, 'lon': self.lon}
    
    @property
    def geojson_describe(self) -> dict:
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [self.lat, self.lon]
            },
            "properties": {
                "name": self.name,
                "temp": self.temp if self.temp or self.temp == 0 else "Unavailable"
            }
        }

    def set_temp(self, temp: float) -> None:
        self.temp = temp