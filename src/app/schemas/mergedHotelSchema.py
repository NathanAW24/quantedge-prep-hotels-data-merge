from typing import List, Optional
from pydantic import BaseModel


class MergedHotelLocationSchema(BaseModel):
    lat: Optional[float]
    lng: Optional[float]
    address: Optional[float]
    city: Optional[str]
    country: Optional[str]


class MergedHotelAmenitiesSchema(BaseModel):
    general: Optional[List[str]]
    room: Optional[List[str]]


class MergedHotelImageSchema(BaseModel):
    link: Optional[str]
    description: Optional[str]


class MergedHotelImagesSchema(BaseModel):
    rooms: Optional[List[MergedHotelImageSchema]]
    site: Optional[List[MergedHotelImageSchema]]
    amenities: Optional[List[MergedHotelImageSchema]]


class MergedHotelSchema(BaseModel):
    id: str
    destination_id: str
    name: str

    location: Optional[MergedHotelLocationSchema]
    description: Optional[str]
    amenities: Optional[MergedHotelAmenitiesSchema]
    images: Optional[MergedHotelImagesSchema]
    booking_conditions: Optional[List[str]]


class MergedHotelRequest(BaseModel):
    hotels: Optional[List[str]]  # list of hotel ids
    destination: Optional[int]  # destination id
