from typing import List, Optional, Union
from pydantic import BaseModel


class AcmeSupplierSchema(BaseModel):
    Id: str
    DestinationId: int
    Name: str
    Latitude: Optional[Union[str, float]]
    Longitude: Optional[Union[str, float]]
    Address: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    PostalCode: Optional[str]
    Description: Optional[str]
    Facilities: Optional[List[str]]
