
import re
from typing import List, Optional
from app.utils import SupplierChoice, fetch_suppliers_and_filter
from app.schemas.suppliers import AcmeSupplierSchema, PatagoniaSupplierSchema, PaperfliesSupplierSchema
from app.schemas import MergedHotelSchema, MergedHotelLocationSchema, MergedHotelAmenitiesSchema, MergedHotelImagesSchema, MergedHotelImageSchema


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

        if hotel_ids:
            for hotel_id in hotel_ids:
                acme_hotel = next(
                    (hotel for hotel in acme_hotels if hotel.Id == hotel_id), None)
                patagonia_hotel = next(
                    (hotel for hotel in patagonia_hotels if hotel.id == hotel_id), None)
                paperflies_hotel = next(
                    (hotel for hotel in paperflies_hotels if hotel.hotel_id == hotel_id), None)

                # # sometimes values can be None
                # print(acme_hotel)
                # print(patagonia_hotel)
                # print(paperflies_hotel)

                

        return None

    @staticmethod
    def merge_name_data(acme_hotel: Optional[AcmeSupplierSchema], patagonia_hotel: Optional[PatagoniaSupplierSchema], paperflies_hotel: Optional[PaperfliesSupplierSchema]) -> Optional[str]:
        return MergeHotels.get_longest_string(
            acme_hotel.Name if acme_hotel else None,
            patagonia_hotel.name if patagonia_hotel else None,
            paperflies_hotel.hotel_name if paperflies_hotel else None
        )

    @staticmethod
    def merge_location_data(acme_hotel: Optional[AcmeSupplierSchema], patagonia_hotel: Optional[PatagoniaSupplierSchema], paperflies_hotel: Optional[PaperfliesSupplierSchema]) -> Optional[MergedHotelLocationSchema]:
        lat = acme_hotel.Latitude if acme_hotel else (
            patagonia_hotel.lat if patagonia_hotel else None)
        lng = acme_hotel.Longitude if acme_hotel else (
            patagonia_hotel.lng if patagonia_hotel else None)
        address = MergeHotels.get_longest_string(
            acme_hotel.Address if acme_hotel else None,
            patagonia_hotel.address if patagonia_hotel else None,
            paperflies_hotel.location.address if paperflies_hotel else None
        )
        city = MergeHotels.get_longest_string(
            acme_hotel.City if acme_hotel else None)
        country = MergeHotels.get_longest_string(
            acme_hotel.Country if acme_hotel else None,
            paperflies_hotel.location.country if paperflies_hotel else None
        )
        return MergedHotelLocationSchema(lat=lat, lng=lng, address=address, city=city, country=country)

    @staticmethod
    def merge_description_data(acme_hotel: Optional[AcmeSupplierSchema], patagonia_hotel: Optional[PatagoniaSupplierSchema], paperflies_hotel: Optional[PaperfliesSupplierSchema]) -> Optional[str]:
        return MergeHotels.get_longest_string(
            acme_hotel.Description if acme_hotel else None,
            patagonia_hotel.info if patagonia_hotel else None,
            paperflies_hotel.details if paperflies_hotel else None
        )

    @staticmethod
    def merge_amenities_data(acme_hotel: Optional[AcmeSupplierSchema], patagonia_hotel: Optional[PatagoniaSupplierSchema], paperflies_hotel: Optional[PaperfliesSupplierSchema]) -> Optional[MergedHotelAmenitiesSchema]:
        general = set()
        if acme_hotel:
            for gn in acme_hotel.Facilities:
                general.add(MergeHotels.camel_to_spaces(gn.strip()))
        if paperflies_hotel:
            for gn in paperflies_hotel.amenities.general:
                general.add(MergeHotels.camel_to_spaces(gn.strip()))

        room = set()
        if patagonia_hotel:
            for rm in patagonia_hotel.amenities:
                room.add(MergeHotels.camel_to_spaces(rm.strip()))
        if paperflies_hotel:
            for rm in paperflies_hotel.amenities.room:
                room.add(MergeHotels.camel_to_spaces(rm.strip()))

        return MergedHotelAmenitiesSchema(general=list(general), room=list(room))

    @staticmethod
    def merge_images_data(acme_hotel: Optional[AcmeSupplierSchema], patagonia_hotel: Optional[PatagoniaSupplierSchema], paperflies_hotel: Optional[PaperfliesSupplierSchema]) -> Optional[MergedHotelImagesSchema]:
        rooms = []
        if patagonia_hotel:
            for room in patagonia_hotel.images.rooms:
                rooms.append(MergedHotelImageSchema(
                    link=room.url, description=room.description))
        if paperflies_hotel:
            for room in paperflies_hotel.images.rooms:
                rooms.append(MergedHotelImageSchema(
                    link=room.link, description=room.caption))

        sites = []
        if paperflies_hotel:
            for site in paperflies_hotel.images.site:
                sites.append(MergedHotelImageSchema(
                    link=site.link, description=site.caption))

        amenities = []
        if patagonia_hotel:
            for amenity in patagonia_hotel.images.amenities:
                amenities.append(MergedHotelImageSchema(
                    link=amenity.url, description=amenity.description))

        return MergedHotelImagesSchema(rooms=rooms, site=sites, amenities=amenities)

    @staticmethod
    def camel_to_spaces(s: str):
        return re.sub(r'([a-z])([A-Z])', r'\1 \2', s).lower()

    @staticmethod
    def get_longest_string(*args: Optional[str]) -> Optional[str]:
        stripped_args = [arg.strip() for arg in args if arg]
        if not stripped_args:
            return None

        return max(stripped_args, key=len)
