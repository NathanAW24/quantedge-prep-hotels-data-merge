from typing import List
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
    address: str
    info: str
    amenities: List[str]
    images: PatagoniaSupplierImagesSchema
