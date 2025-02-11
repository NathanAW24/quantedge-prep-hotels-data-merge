from typing import List, Union
from fastapi import FastAPI

from app.schemas import MergedHotelSchema, MergedHotelRequest
from app.services import MergeHotels

app = FastAPI()


@app.get("/hotels", response_model=Union[List[MergedHotelSchema]])
async def get_filtered_hotels(request: MergedHotelRequest):
    hotel_ids = request.hotels if request.hotels else None
    destination = request.destination if request.destination else None
    return MergeHotels.merge_hotels(hotel_ids=hotel_ids, destination_id=destination)
