from typing import List
from pydantic import BaseModel


class PaperfliesSupplierImageSchema(BaseModel):
    link: str
    caption: str


class PaperfliesSupplierImagesSchema(BaseModel):
    rooms: List[PaperfliesSupplierImageSchema]
    site: List[PaperfliesSupplierImageSchema]


class PaperfliesSupplierLocationSchema(BaseModel):
    address: str
    country: str


class PaperfliesSupplierAmenitiesSchema(BaseModel):
    general: List[str]
    room: List[str]


class PaperfliesSupplierSchema(BaseModel):
    hotel_id: str
    destination_id: int
    hotel_name: str

    location: PaperfliesSupplierLocationSchema
    details: str
    amenities: PaperfliesSupplierAmenitiesSchema
    images: PaperfliesSupplierImagesSchema
    booking_conditions: List[str]
