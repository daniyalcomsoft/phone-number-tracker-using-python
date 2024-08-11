import phonenumbers
import opencage
from test import number
import folium

key = "43ebd48729f947d3b0283c52e1df3d07"

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(ch_number, "en")
print(number_location)

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

map_location = folium.Map(location= [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")