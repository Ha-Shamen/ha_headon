import asyncio
import os
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.apps.web_service.app.utils.site_manager import SiteManager


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

site_manager = SiteManager()

# Default sites
# site_manager.add_site(name='Berlin', lat=52.520008, lon=13.404954)
CONFIG_FILE_PATH = os.environ.get("CONFIG")

# Read the configuration
site_manager.load_config(config_file_path=CONFIG_FILE_PATH)


    # site_manager.add_site(name='Tel Aviv', lat=32.109333, lon=34.855499)
    # site_manager.add_site(name='Barcelona', lat=41.390205, lon=2.154007)
    # site_manager.add_site(name='Paris', lat=48.864716, lon=2.349014)
    # site_manager.add_site(name='Cologne', lat=50.935173, lon=6.953101)

async def periodic_task():
    while True:
        # Perform your task here
        print("Performing task every 5 minutes...")
        site_manager.refresh_sites()
        # Sleep for 5 minutes (300 seconds)
        await asyncio.sleep(300)

async def startup_event():
    # Manually create a background task for the periodic task
    asyncio.create_task(periodic_task())

# Attach the asynchronous startup event function
app.add_event_handler("startup", startup_event)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your weather map"}

@app.get("/weather-sites")
def weather_sites():
    return site_manager.sites

@app.post("/refresh-weather")
def refresh_weather():
    return site_manager.refresh_sites()

@app.post("/add-site/")
def add_site(data: dict):
    city_name = data.get('name')
    lat = data.get('lat')
    lon = data.get('lon')
    return site_manager.add_site(name=city_name, lat=lat, lon=lon)
