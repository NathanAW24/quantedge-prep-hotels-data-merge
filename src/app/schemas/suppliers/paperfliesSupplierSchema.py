from typing import List, Optional
from pydantic import BaseModel


class PaperfliesSupplierImageSchema(BaseModel):
    link: Optional[str]
    caption: Optional[str]


class PaperfliesSupplierImagesSchema(BaseModel):
    rooms: Optional[List[PaperfliesSupplierImageSchema]]
    site: Optional[List[PaperfliesSupplierImageSchema]]


class PaperfliesSupplierLocationSchema(BaseModel):
    address: Optional[str]
    country: Optional[str]


class PaperfliesSupplierAmenitiesSchema(BaseModel):
    general: Optional[List[str]]
    room: Optional[List[str]]


class PaperfliesSupplierSchema(BaseModel):
    hotel_id: str
    destination_id: int
    hotel_name: str

    location: Optional[PaperfliesSupplierLocationSchema]
    details: Optional[str]
    amenities: Optional[PaperfliesSupplierAmenitiesSchema]
    images: Optional[PaperfliesSupplierImagesSchema]
    booking_conditions: Optional[List[str]]
