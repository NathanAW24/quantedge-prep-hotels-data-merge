from app.utils import fetch_supplier, SupplierChoice, fetch_suppliers_and_filter


# print(fetch_supplier(supplier=SupplierChoice.ACME))
# print(fetch_supplier(supplier=SupplierChoice.PATAGONIA))
# print(fetch_supplier(supplier=SupplierChoice.PAPERFLIES))
# print(fetch_suppliers_hotel_ids_destination_id(
#     supplier=SupplierChoice.ACME, hotel_ids=["iJhz", "SjyX"], destination_id=5432))
# print(fetch_suppliers_hotel_ids_destination_id(
#     supplier=SupplierChoice.PATAGONIA, hotel_ids=["iJhz", "SjyX"], destination_id=5432))
print(fetch_suppliers_and_filter(
    supplier=SupplierChoice.PAPERFLIES, hotel_ids=["iJhz", "SjyX"], destination_id=5432))
