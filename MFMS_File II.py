import csv
class Station:
    """
    Representation of T stations

    Attributes:
    "stop_id","stop_code","stop_name","stop_desc","platform_code",
    "platform_name","stop_lat","stop_lon","stop_address","zone_id",
    "stop_url","level_id","location_type","parent_station","wheelchair_boarding"

    This class is used to organize all Stations so that they
    can easily be used to form the network nodes
    """

    def __init__(self, stop_id, stop_name, lat, lon, bus, tram, subway, centroid):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.lat = float(lat)
        self.lon = float(lon)
        self.bus = bus
        self.tram = tram
        self.subway = subway
        self.centroid = centroid


        # figure out if station is for subways
        if 'Line' in self.centroid:
            self.munich_stop = True
        else:
            self.munich_stop = False


    def get_name(self):
        return self.stop_name

    def get_id(self):
        return self.identifier

    def get_parent_station(self):
        return self.parent_station

    def get_coordinates(self):
        return (self.lon, self.lat)



def create_stations(filename='stations_csv.csv'):
    """
    Reads in lines of stops GTFS file and creates stops objects
    parameters: 
        filename - string, the filename of the GTFS stops file
    returns:
        list of stations in the file, as Station objects
    """
    with open(filename, newline='') as stops:
        station_info = csv.reader(stops)
        # skip first line, which is just attribute names
        next(station_info)
        # empty list to hold stations
        stations = []
        # parse all the lines and create stations
        for row in station_info:
            # assign each attribute of Station based on line in file
            (stop_id, stop_name, lat, lon, bus, tram, subway, centroid) = tuple(row)
            # create Station instance with those attributes
            stations.append(Station(stop_id, stop_name, lat, lon, bus, tram, subway, centroid))

    return stations
print(stop_id