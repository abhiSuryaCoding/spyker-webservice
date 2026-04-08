from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Location(BaseModel):
    latitude: float
    longitude: float

# store latest location
latest_location = {"lat": 0, "lon": 0}

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/location")
def receive_location(loc: Location):
    global latest_location

    latest_location = {
        "lat": loc.latitude,
        "lon": loc.longitude
    }

    return {"status": "ok"}

@app.get("/location")
def get_location():
    return latest_location