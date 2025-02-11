
from typing import List, Optional
from app.utils import SupplierChoice, fetch_suppliers_and_filter
from app.schemas.suppliers import AcmeSupplierSchema, PatagoniaSupplierSchema, PaperfliesSupplierSchema
from app.schemas import MergedHotelSchema, MergedHotelLocationSchema


class MergeHotels:
    @staticmethod
    def merge_hotels(hotel_ids: Optional[List[str]], destination_id: Optional[int]) -> Optional[List[MergedHotelSchema]]:
        # fetch the acme supplier
        acme_hotels: List[AcmeSupplierSchema] = fetch_suppliers_and_filter(
            SupplierChoice.ACME, hotel_ids=hotel_ids, destination_id=destination_id)
        patagonia_hotels: List[PatagoniaSupplierSchema] = fetch_suppliers_and_filter(
            SupplierChoice.PATAGONIA, hotel_ids=hotel_ids, destination_id=destination_id)
        paperflies_hotels: List[PaperfliesSupplierSchema] = fetch_suppliers_and_filter(
            SupplierChoice.PAPERFLIES, hotel_ids=hotel_ids, destination_id=destination_id)

        print(acme_hotels)
        print(patagonia_hotels)
        print(paperflies_hotels)  # OK

        merged_hotels = {}

        # if hotel_ids:
        #     for hotel_id in hotel_ids:
        #         acme_hotel = next(
        #             (hotel for hotel in acme_hotels if hotel.id == hotel_id), None)

        return None

    @staticmethod
    def merge_name_data(acme_hotel: AcmeSupplierSchema, patagonia_hotel: PatagoniaSupplierSchema, paperflies_hotel: PaperfliesSupplierSchema) -> Optional[str]:
        return MergeHotels.get_longest_string(acme_hotel.Name, patagonia_hotel.name, paperflies_hotel.hotel_name)

    @staticmethod
    def merge_location_data(acme_hotel: AcmeSupplierSchema, patagonia_hotel: PatagoniaSupplierSchema, paperflies_hotel: PaperfliesSupplierSchema) -> Optional[MergedHotelLocationSchema]:
        lat = acme_hotel.Latitude or patagonia_hotel.lat
        lng = acme_hotel.Longitude or patagonia_hotel.lng
        address = MergeHotels.get_longest_string(
            acme_hotel.Address, patagonia_hotel.address, paperflies_hotel.location.address)
        city = MergeHotels.get_longest_string(acme_hotel.City)
        country = MergeHotels.get_longest_string(
            acme_hotel.Country, paperflies_hotel.location.country)
        return MergedHotelLocationSchema(lat=lat, lng=lng, address=address, city=city, country=country)

    @staticmethod
    def merge_description_data(acme_hotel: AcmeSupplierSchema, patagonia_hotel: PatagoniaSupplierSchema, paperflies_hotel: PaperfliesSupplierSchema) -> Optional[str]:
        return MergeHotels.get_longest_string(acme_hotel.Description, patagonia_hotel.info, paperflies_hotel.details)
    
    @staticmethod
    

    @staticmethod
    def get_longest_string(*args: Optional[str]) -> Optional[str]:
        stripped_args = [arg.strip() for arg in args if arg]
        if not stripped_args:
            return None

        return max(stripped_args, key=len)
