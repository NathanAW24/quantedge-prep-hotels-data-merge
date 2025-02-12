from typing import List, Union
from fastapi import FastAPI

from app.schemas import MergedHotelSchema, MergedHotelRequest
from app.services import MergeHotels
from app.utils import HotelCache

app = FastAPI()
hotel_cache = HotelCache()


@app.get("/hotels", response_model=Union[List[MergedHotelSchema]])
async def get_filtered_hotels(request: MergedHotelRequest):
    hotel_ids = request.hotels if request.hotels else None
    destination = request.destination if request.destination else None

    # Try to get from cache first # DROPS DOWN TO 3 milliseconds after caching
    cached_result = hotel_cache.get(hotel_ids, destination)
    if cached_result:
        return cached_result

    # If not in cache, fetch and merge hotels
    result = await MergeHotels.merge_hotels(hotel_ids=hotel_ids, destination_id=destination)

    # Cache the result
    hotel_cache.set(hotel_ids, destination, result)

    return result
