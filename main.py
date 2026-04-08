from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Location(BaseModel):
    latitude: float
    longitude: float

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/location")
def receive_location(loc: Location):
    print(f"Received: {loc.latitude}, {loc.longitude}")
    return {
        "status": "success",
        "lat": loc.latitude,
        "lon": loc.longitude
    }