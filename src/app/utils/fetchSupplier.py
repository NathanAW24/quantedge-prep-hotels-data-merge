from app.schemas.suppliers import (
    AcmeSupplierSchema,
    PatagoniaSupplierSchema,
    PaperfliesSupplierSchema,
)
from pydantic import ValidationError
from enum import Enum
from typing import List, Optional, Union
import httpx
from app.schemas.suppliers import AcmeSupplierSchema, PatagoniaSupplierSchema, PaperfliesSupplierSchema


class SupplierChoice(str, Enum):
    ACME = "acme"
    PATAGONIA = "patagonia"
    PAPERFLIES = "paperflies"


BASE_URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers"

# ACME_URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/acme"
# PATAGONIA_URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/patagonia"
# PAPERFLIES_URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/paperflies"


class SupplierChoice(str, Enum):
    ACME = "acme"
    PATAGONIA = "patagonia"
    PAPERFLIES = "paperflies"


BASE_URL = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers"

SupplierSchemasType = Union[
    List[AcmeSupplierSchema], List[PatagoniaSupplierSchema], List[PaperfliesSupplierSchema]
]


def fetch_supplier(supplier: SupplierChoice) -> SupplierSchemasType:
    supplier_url = f"{BASE_URL}/{supplier.value}"
    print(f"Fetching data from: {supplier_url}")

    response = httpx.get(supplier_url)
    response.raise_for_status()

    data = response.json()

    # Mapping supplier choice to the correct schema
    schema_map = {
        SupplierChoice.ACME: AcmeSupplierSchema,
        SupplierChoice.PATAGONIA: PatagoniaSupplierSchema,
        SupplierChoice.PAPERFLIES: PaperfliesSupplierSchema,
    }

    schema = schema_map.get(supplier)

    if not schema:
        raise ValueError(f"Unsupported supplier: {supplier}")

    try:
        # Validate each item using the schema
        return [schema(**item) for item in data]
    except ValidationError as e:
        print(f"Validation error for {supplier.value}: {e}")
        print("ERROR DATA", data)
        return []  # Or handle errors differently


def fetch_suppliers_and_filter(supplier: SupplierChoice, hotel_ids: Optional[List[str]], destination_id: Optional[int]) -> SupplierSchemasType:
    unfiltered_hotels = fetch_supplier(supplier)

    match supplier.value:
        case SupplierChoice.ACME:
            filtered_hotels = [
                item for item in unfiltered_hotels
                if (hotel_ids is None or item.Id in hotel_ids) and
                (destination_id is None or item.DestinationId == destination_id)
            ]
            return filtered_hotels
        case SupplierChoice.PATAGONIA:
            filtered_hotels = [
                item for item in unfiltered_hotels
                if (hotel_ids is None or item.id in hotel_ids) and
                (destination_id is None or item.destination == destination_id)
            ]
            return filtered_hotels
        case SupplierChoice.PAPERFLIES:
            filtered_hotels = [
                item for item in unfiltered_hotels
                if (hotel_ids is None or item.hotel_id in hotel_ids) and
                (destination_id is None or item.destination_id == destination_id)
            ]
            return filtered_hotels
        case _:
            return unfiltered_hotels
