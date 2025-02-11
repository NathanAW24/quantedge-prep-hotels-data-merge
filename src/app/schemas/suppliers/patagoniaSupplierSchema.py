from typing import List, Optional
from pydantic import BaseModel


class PatagoniaSupplierImageSchema(BaseModel):
    url: str
    description: str


class PatagoniaSupplierImagesSchema(BaseModel):
    rooms: List[PatagoniaSupplierImageSchema]
    amenities: List[PatagoniaSupplierImageSchema]


class PatagoniaSupplierSchema(BaseModel):
    id: str
    destination: int
    name: str
    lat: float
    lng: float
    address: Optional[str]
    info: Optional[str]
    amenities: Optional[List[str]]
    images: PatagoniaSupplierImagesSchema
