from real_location import Location as RealLocation
from mock_location import Location as MockLocation

class LocationFinder(object):
    def __init__(self, location_instance):
        self.location_instance = location_instance
    
    def findLocationName(self, lat, lon):
        return self.location_instance.get_location(lat, lon)


realInstance = LocationFinder(RealLocation())
print(realInstance.findLocationName(50.0, 50.0))

mockInstance = LocationFinder(MockLocation())
print(mockInstance.findLocationName(50.0, 50.0))
