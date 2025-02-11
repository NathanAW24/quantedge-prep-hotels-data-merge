from typing import List, Optional, Union
from pydantic import BaseModel


class AcmeSupplierSchema(BaseModel):
    Id: str
    DestinationId: int
    Name: str
    Latitude: Optional[Union[str, float]]
    Longitude: Optional[Union[str, float]]
    Address: str
    City: str
    Country: str
    PostalCode: str
    Description: str
    Facilities: List[str]
