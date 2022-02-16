# Imports
import csv
import CSV_Extractor
import Location

# Global variable to bring in the extracted CSV data for use.
distances_list = CSV_Extractor.import_csv("CSV_Data/distanceTable.csv")


# This will take the current location of the truck and determine, based on the locations it needs to go, the closest
# destination each time. It does this by taking the current location of the truck and going through the
# delivery locations list to see which one is the closest to where the truck currently is. With each location, it looks
# at the distance data to see how far away it is from the current location. If the distance is smaller than the last,
# it will update the closest distance and the next_destination_index. Once it goes through all the destinations, it
# takes the closest destination data and updates the truck mileage and truck current location. Then finally, it will
# remove the destination from the trucks delivery_Locations list because it does not need to go there.
# This algorithm has a time complexity of O(n^2) because it relies on the size of the delivery_locations list. We do not
# necessarily know how many locations the truck needs to go to. It also calls the Location.get_location_index function.
# The time complexity of this function is O(n) because it relies on the length of the addresses_list.
def find_closest(current_locale, truck):
    closest = 100.0  # Sets closest value to be something that will get overwritten after first loop execution.
    next_destination_index = -1  # Set to an invalid index
    index_to_delete = -1  # Set to an invalid index

    # This loop has a time complexity of O(n). It is dependent on the amount of locations the truck needs to go to.
    # It loops through that list and determines which of the locations is the closest.
    for index in range(len(truck.delivery_locations)):  # Loops through each index in the trucks delivery_locations list

        # Sets the destination to be that of the index value in the locations list for the current index being looked at
        destination = int(Location.get_location_index(truck.delivery_locations[index]))

        # This calls the get_distance function to find the distance between where the truck is and the current index
        # location.
        distance = float(get_distance(current_locale, destination))

        # Checks to see if the current location is the closest. if the location is the closest, it will update the
        # distance the truck will need to travel as well as the the next_destination_index. This is used to update the
        # trucks current location once the closest destination has been found.
        if (distance != 0.0) & (distance <= closest):
            closest = distance  # Updates closest distance if current location is closer.
            # Updates the next_destination_index if the current destination is closer than previous.
            next_destination_index = destination
            # This is to keep track of the index location in the delivery_locations list. This is needed in order
            # to determine what destination needs to be removed so the truck does not go to the same place twice.
            index_to_delete = index

    # Removes the location where the truck is going to go to next from the delivery locations list.
    truck.delivery_locations.remove(truck.delivery_locations[index_to_delete])

    # Adds the closest destinations distance away to the current truck mileage.
    truck.mileage += closest

    # Updates the trucks time by determining how long it will take the truck to go that distance at the specified
    # speed. It stores as a float to be converted to actual time later.
    truck.time += (closest / truck.speed)

    # Returns the Location data for the closest destination the truck needs to go to next.
    return Location.addresses_list[next_destination_index]


# This function takes two inputs. The current location of the truck and the proposed destination. It will then look
# At the distance data to find how close they are to each other. It will return that value.
def get_distance(current_locale, destination):
    # If there is a blank space in the list that will get returned, this flips the values so the value is returned.
    if distances_list[current_locale][destination] == '':
        # Returns the value where the row is the destination and the current location of the truck is the row to look at
        # This is needed because some items in the data sheet are blank. Switching them will return the correct distance
        return distances_list[destination][current_locale]
    else:

        # The distance value was found the first time so it just needs to return the found value.
        return distances_list[current_locale][destination]
