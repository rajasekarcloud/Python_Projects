# Distance Calculator Using Class
from geopy import distance;
from geopy.geocoders import Nominatim;
from geopy.distance import geodesic;

def get_coordinate(home_address):
    agent = Nominatim(user_agent="mylocator");
    coordinate = agent.geocode(home_address);
    return(coordinate.latitude, coordinate.longitude);

def dist_checker(home_cordinate, target_cordinate):
    return distance.distance(home_cordinate,target_cordinate).miles;

def main():
    home_address: str = "3655 Pruneridge Avenue, Santa Clara, California";
    print(f'Home Address: {home_address}');
    # Getting its coordinate
    home_cordinate = get_coordinate(home_address);
    #print(home_cordinate);
    #print(type(home_cordinate)); # Return as Tuple
    target_address: str = input("Enter Targer Address: ");
    print(f'Target Address: {target_address}');
    target_cordinate = get_coordinate(target_address);
    print(f'Distance: {dist_checker(home_cordinate,target_cordinate)} Miles');


if __name__ == '__main__':
    main();
