from typing import List
from pydantic import BaseModel


class AcmeSupplierSchema(BaseModel):
    Id: str
    DestinationId: int
    Name: str
    Latitude: float
    Longitude: float
    Address: str
    City: str
    Country: str
    PostalCode: str
    Description: str
    Facilities: List[str]
