# Imports
import CSV_Extractor

# Extracts the address data from the csv file
addresses_list = CSV_Extractor.import_csv("CSV_Data/addressTable.csv")


# This function gets the location index to use in order to find the distance data for said location.
# It takes the address name and checks the addresses_list. It will then return the first index for the address item.
# This index value matches to the row/column to look at in the distances list.
def get_location_index(address_name):
    # Loop has a time complexity of O(n) It is based off of how many addresses are in the address list. Arguably, you
    # could assume it is no more than O(40) = O(1) since each package cannot have multiple addresses.
    for index in range(len(addresses_list)): # Loops as many times as there are addresses in the addresses_list
        # If the address name matches the current indexes address name, it will return the addresses index ("ID/Key")
        # to map to the the distances in the distances list.
        if address_name == addresses_list[index][2]:
            # Returns the "key" number that is used to map the address to the list of distances in the distances_list.
            return addresses_list[index][0] # Returns only that "key" number.
    # Returns error if Address is not found.
    return "Error: Address not Found"
