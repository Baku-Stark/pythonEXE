import phonenumbers
from phonenumbers import geocoder, carrier, timezone


phone_number = str(input("Type a Phone Number (+1234123456789): "))

cell_phone = phonenumbers.parse(phone_number, "BR")
print(f"+{cell_phone.country_code} | {cell_phone.national_number}")
print(f"Location: {geocoder.description_for_number(cell_phone, 'en')} ", end="")
print(f"Timezone: {timezone.time_zones_for_number(cell_phone)}")

cell_phone_country = geocoder.country_name_for_number(cell_phone, "en")
print(cell_phone_country)

cell_phone_name = carrier.name_for_number(cell_phone, "en")
print(cell_phone_name)