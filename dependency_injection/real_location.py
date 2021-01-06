import requests

class Location(object):

    def get_location(self, lat, lon):
        try:
            response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}")
            return response.json()['display_name']
        except e:
            print ("Unable to find place")
