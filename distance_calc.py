# Distance Calculator
# Calculate distance between 2 places
# We use module called "geopy"
# https://geopy.readthedocs.io/en/stable/#module-geopy.distance
# We calculate the distance by getting the latitude and longitude of the source and destination address
# Lets check the distance with predefined lat and long
from geopy import distance;
from geopy.geocoders import Nominatim;
from geopy.distance import geodesic;

# Below works when you have the lat and log
#newport_ri = (41.49008, -71.312796);
#cleveland_oh = (41.499498, -81.695391);
#print(distance.distance(newport_ri,cleveland_oh).miles," Miles");
locator = Nominatim(user_agent="mylocator"); # mylocator is app name
location = locator.geocode("175 5th Avenue NYC"); # Input Address
print(location.address); # Print Address based on the location.
#print(location.latitude, location.longitude);
location = locator.reverse("40.741059199999995, -73.98964162240998"); # Based on lat and long
print(location.address);
# https://geopy.readthedocs.io/en/stable/
