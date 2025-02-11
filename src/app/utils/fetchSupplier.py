from app.schemas.suppliers import (
    AcmeSupplierSchema,
    PatagoniaSupplierSchema,
    PaperfliesSupplierSchema,
)
from pydantic import ValidationError
from enum import Enum
from typing import List, Union
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

SupplierSchemaType = Union[
    List[AcmeSupplierSchema], List[PatagoniaSupplierSchema], List[PaperfliesSupplierSchema]
]


def fetch_supplier(supplier: SupplierChoice) -> SupplierSchemaType:
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
