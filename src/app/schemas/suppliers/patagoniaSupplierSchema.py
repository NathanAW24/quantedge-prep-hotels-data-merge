from typing import List, Optional
from pydantic import BaseModel


class PatagoniaSupplierImageSchema(BaseModel):
    url: Optional[str]
    description: Optional[str]


class PatagoniaSupplierImagesSchema(BaseModel):
    rooms: Optional[List[PatagoniaSupplierImageSchema]]
    amenities: Optional[List[PatagoniaSupplierImageSchema]]


class PatagoniaSupplierSchema(BaseModel):
    id: str
    destination: int
    name: str
    lat: Optional[float]
    lng: Optional[float]
    address: Optional[str]
    info: Optional[str]
    amenities: Optional[List[str]]
    images: Optional[PatagoniaSupplierImagesSchema]
