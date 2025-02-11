
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
    def merge_amenities_data(acme_hotel: AcmeSupplierSchema, patagonia_hotel: PatagoniaSupplierSchema, paperflies_hotel: PaperfliesSupplierSchema) -> Optional[MergedHotelAmenitiesSchema]:
        # general taken from acme Facilities, and paperflies.amenities.general

        general = set()
        for gn in acme_hotel.Facilities:
            general.add(MergeHotels.camel_to_spaces(gn.strip()))
        for gn in paperflies_hotel.amenities.general:
            general.add(MergeHotels.camel_to_spaces(gn.strip()))

        # room taken from patagonia amenities and paerflies.amenities.room
        room = set()
        for rm in patagonia_hotel.amenities:
            room.add(MergeHotels.camel_to_spaces(rm.strip()))
        for rm in paperflies_hotel.amenities.room:
            room.add(MergeHotels.camel_to_spaces(rm.strip()))

        return MergedHotelAmenitiesSchema(general=list(general), room=list(room))

    @staticmethod
    def merge_images_data(acme_hotel: AcmeSupplierSchema, patagonia_hotel: PatagoniaSupplierSchema, paperflies_hotel: PaperfliesSupplierSchema) -> Optional[MergedHotelImagesSchema]:
        rooms = []  # from patagonia and paperflies
        for room in patagonia_hotel.images.rooms:
            rooms.append(MergedHotelImageSchema(
                link=room.url, description=room.description))
        for room in paperflies_hotel.images.rooms:
            rooms.append(MergedHotelImageSchema(
                link=room.link, description=room.caption))
        # print(rooms)

        sites = []  # from paperflies
        for site in paperflies_hotel.images.site:
            sites.append(MergedHotelImageSchema(
                link=site.link, description=site.caption))

        # print(sites)

        amenities = []  # from patagonia
        for amenity in patagonia_hotel.images.amenities:
            amenities.append(MergedHotelImageSchema(
                link=amenity.url, description=amenity.description))
        # print(amenities)

        # return MergedHotelImagesSchema(rooms=[], images=[], amenities=[])
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
