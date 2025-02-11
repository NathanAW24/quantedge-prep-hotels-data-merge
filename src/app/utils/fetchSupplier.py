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


def fetch_supplier(supplier: SupplierChoice):
    supplier_url = f"{BASE_URL}/{supplier.value}"
    # why is this like this? https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers/SupplierChoice.PATAGONIA
    print(supplier_url)

    response = httpx.get(supplier_url)
    response.raise_for_status()

    data = response.json()

    return data
