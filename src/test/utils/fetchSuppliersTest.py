from app.utils import fetch_supplier, SupplierChoice
# python -m test.utils.fetchSuppliersTest

print(fetch_supplier(supplier=SupplierChoice.ACME))
print(fetch_supplier(supplier=SupplierChoice.PATAGONIA))
print(fetch_supplier(supplier=SupplierChoice.PAPERFLIES))
