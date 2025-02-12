from typing import List, Optional
from app.schemas import MergedHotelSchema
from datetime import datetime, timedelta


class HotelCache:
    def __init__(self):
        self._cache = {}
        self._ttl = timedelta(minutes=5)  # Cache TTL of 5 minutes

    def get_cache_key(self, hotel_ids: Optional[List[str]], destination_id: Optional[int]) -> str:
        return f"{'-'.join(hotel_ids) if hotel_ids else ''}-{destination_id if destination_id else ''}"

    def get(self, hotel_ids: Optional[List[str]], destination_id: Optional[int]) -> Optional[List[MergedHotelSchema]]:
        key = self.get_cache_key(hotel_ids, destination_id)
        if key in self._cache:
            result, timestamp = self._cache[key]
            if datetime.now() - timestamp < self._ttl:
                return result
            del self._cache[key]
        return None

    def set(self, hotel_ids: Optional[List[str]], destination_id: Optional[int], value: List[MergedHotelSchema]):
        key = self.get_cache_key(hotel_ids, destination_id)
        self._cache[key] = (value, datetime.now())
