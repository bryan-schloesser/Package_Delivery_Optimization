# Imports
import Location
import Distance


# Truck Class
class Truck:
    # Initializes truck object. Name is required
    def __init__(self, name):
        self.package_list = []  # List of packages for the truck
        self.mileage = 0  # Mileage for the truck
        self.delivery_locations = []  # List of all locations the truck needs to visit
        # self.delivery_distances = [] # Not used
        self.current_location = Location.addresses_list[0]  # Current location of the truck. Default is the Hub.
        self.name = name  # Name of Truck.
        self.time = 0  # This is the trucks "clock". Set to zero and will be started once the truck is loaded.
        self.speed = 18  # Speed of truck

    # Takes the list of package ID's and searches the hash table for those packages.
    # It then adds them to the list of packages for the truck. The time is also passed in. This is when the truck
    # departs the hub after the the truck is loaded.
    def load_truck(self, package_id_list, hash_table, time):
        self.time = time  # When the truck leaves

        # The time complexity for this loop is O(n). It is based on how many packages are in the list for the truck to
        # deliver. The loop will look at the list of package IDs and pull the data from the hash_table to insert into
        # the trucks list. It then will look at that packages address and add it to the trucks delivery locations list.
        # My vision for this was that the truck is actually being loaded with packages. The truck package list is the
        # back of the truck filled with packages. The delivery locations, is the drivers list of where they need to go.
        for pkg_id in package_id_list:
            # Searches the hash table for id in hash table to "load truck" with the package.
            self.package_list.append(hash_table.search(pkg_id))
            # Adds the packages address to the delivery locations list.
            self.delivery_locations.append(hash_table.search(pkg_id).get_address())

            # Sets the status of all packages on the truck to "In Transit". This indicates that the truck left and is
            # out for delivery.
            hash_table.search(pkg_id).set_status("En Route")

        # This takes the list of delivery locations, converts it to a set to remove duplicates.
        self.delivery_locations = set(self.delivery_locations)
        # Since it needs to be a list still, it needs to be converted back to a list. Now it is clean of duplicates.
        self.delivery_locations = list(self.delivery_locations)

    # This method checks and sees where the truck is. It will then go through the list of packages to be delivered,
    # looks at the package delivery address, and will "deliver" it if the address matches.
    def update_packages(self, hash_table):
        # Collection of packages to remove. This is used in case of packages with the same address.
        packages_to_remove = []
        # Loop has a time complexity of O(n). The time complexity is based on the size of the package list. Since the
        # trucks can only carry a max of 16 packages (per the requirements), it can be assumed it will be no higher
        # than O(16) = O(1). However, with future growth, trucks could possibly hold more packages.
        for index in range(len(self.package_list)):
            # Creates new package object
            package_to_check = self.package_list[index]
            # if the package address matches the current location of the truck, deliver package and update status/time.
            if package_to_check.get_address() == self.current_location[2]:
                package_to_check.set_status("Delivered")  # Changes packages status to delivered
                package_to_check.set_delivery_time(
                    self.time)  # Sets the delivery time to the current time of the truck.
                packages_to_remove.append(package_to_check)  # appends the delivered package to the removal list.

        # This loop has a time complexity of O(n). Similarly to the explanation above, you could argue that this has the
        # time complexity of O(16) = O(1) since the truck can only hold 16 packages at any given time.
        for item in packages_to_remove:
            if item in self.package_list:  # If the item in the packages_to_remove list is in the package_list, remove.
                self.package_list.remove(item)  # Removes the item from the list since it is delivered.

    # Method to begin the trucks route. It will check each destination it needs to go to and find which one is closest
    # based on the trucks current location. Once it gets to a location, it will deliver the packages and update the
    # status/time of them.
    def begin_route(self, hash_table):
        # Time complexity of the loop is O(n) and is based on the length of the delivery_locations list for the truck.
        # The loop finds the closest delivery location to where it currently is. Then travels there and delivers the
        # packages.
        for item in range(len(self.delivery_locations)):  # Only "travels" to unique locations based on package data.
            # The current location is equal to the next closest location.
            self.current_location = Distance.find_closest(int(self.current_location[0]), self)
            # One next closest location is determined, this will update the package data as delivered with a timestamp.
            self.update_packages(hash_table)
