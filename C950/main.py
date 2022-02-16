# Name: Bryan Schloesser - Student ID: #001103177

# Imports
import Package
import Truck
import Hash_Table


# Function that will take a time in float form. It will return it in the converted time format based on the float value.
# This is only used to display information to the user.
def format_time(time):
    return '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))


# Function that will take a time string (e.g "11:30") and convert it into the float form for use.
def convert_string_to_time(string):
    string = string.split(":")  # Creates an Array of two numbers
    return float(string[0]) + ((float(string[1])) / 60.0)  # This converts the 2nd num to minutes and adds the two.


# Function that will print the truck completion times and total mileage.
def print_truck_results(truck):
    print(truck.name + " completion time: " + format_time(truck.time))
    print(truck.name + " total mileage: ", truck.mileage)
    print("\n")


# Function used to create the "complete" results. It calls the print_truck_results function for each truck and then also
# provides the conjoined total mileage of all trucks.
def print_results():
    print("============Completion Results============")
    print_truck_results(truck1)
    print_truck_results(truck2)
    print_truck_results(truck3)
    print("Total Mileage for all Trucks: ", truck1.mileage + truck2.mileage + truck3.mileage)
    print("==========================================")


# This function requires the user input time with the truck leave time and packages for each truck. This is the logic
# used to determine the status packages should have based on the time the user input.
def print_packages(time, truck_leave_time, packages):
    # This loops through all packages determine how they are presented to the user. This loops runtime complexity would
    # technically be O(40) = O(1) since we know exactly how many times it will run. However, this can be scaled up if
    # the average number of packages every gets higher.
    for i in range(1, 40):  # Range of Package IDs
        pkg = hash_table.search(i)  # Variable to hold current package being checked
        save_time_data = pkg.get_delivery_time()  # Saves the delivery time of the package so it can get put back later.

        # This checks to see if the package is in the list of packages for the truck. It also checks to see if the
        # package delivery time is greater than both the inputted time and the leave time. If the truck has left
        # already (before user inputted time), but the package delivery time is later on in the day compared to the
        # inputted time, the package would not be delivered yet. However, it would be "en route".
        if pkg.getID() in packages and (truck_leave_time < time < pkg.get_delivery_time()):
            pkg.set_status("En Route")  # Sets the package status to "En Route"
            pkg.set_delivery_time(0)  # Sets value of delivery time to 0 since there is no delivery time yet.

        # This checks to see if the packages are in the truck and that the user inputted time is less than the truck
        # departure time. If these conditions are met, the package would be "At Hub" still.
        if pkg.getID() in packages and (time < truck_leave_time):
            pkg.set_status("At Hub")  # Sets the package status to "En Route"
            pkg.set_delivery_time(0)  # Sets the delivery time to 0 since there is no delivery time yet.

        # If neither condition is met, the package would then be delivered. This also makes sure that the package
        # is then printed no matter what.
        if pkg.getID() in packages:
            pkg.print_package()  # Prints the package.
        pkg.set_status("Delivered")  # Resets the package to Delivered status.
        pkg.set_delivery_time(save_time_data)  # Resets the delivery time to the original time.


# Creates instance of a hash table
hash_table = Hash_Table.HashTable(15)

# Loads package data into hash table
Package.package_data_to_hash_table(hash_table)

# Manually Loading Trucks. No more than 16 per truck. There are only two drivers, but both trucks finish their route
# Before truck 3 will leave. Either truck driver can drive the third truck.
truck1_packages = [40, 1, 37, 14, 31, 30, 29, 20, 19, 16, 13, 15, 12, 34, 33]
truck2_packages = [3, 6, 18, 28, 32, 36, 38, 17, 21, 25, 39, 23]
truck3_packages = [2, 4, 5, 7, 8, 9, 10, 11, 22, 24, 26, 35, 27]

# Creates the truck object and loads the truck with the packages specified in the above lists.
# This also sets the departure time.
truck1 = Truck.Truck('Truck 1')   # Name of truck. Irrelevant to how it runs. Just adds additional customization.
truck1_leave_time = 8.0           # Truck leave time is customizable. This constant does not change.

# Calls the load_truck method. This takes the packages, loads up the truck, and leaves at the specified time.
truck1.load_truck(truck1_packages, hash_table, truck1_leave_time)

# Creates the truck object and loads the truck with the packages specified in the above lists.
# This also sets the departure time.
truck2 = Truck.Truck('Truck 2')    # Name of truck. Irrelevant to how it runs. Just adds additional customization.
truck2_leave_time = 9.08           # Truck leave time is customizable. This constant does not change.

# Calls the load_truck method. This takes the packages, loads up the truck, and leaves at the specified time.
truck2.load_truck(truck2_packages, hash_table, truck2_leave_time)

# Changing package information for package 9. This package is on truck 3 since the information will not
# get updated until 10:20. Truck 3 will leave at 11AM
hash_table.search(9).set_address("410 S State St")
hash_table.search(9).set_city("Salt Lake City")
hash_table.search(9).set_state("UT")
hash_table.search(9).set_zipcode("84111")
hash_table.search(9).set_special_notes("Address Corrected at 10:20 - To be Delivered on Truck 3")

# Creates the truck object and loads the truck with the packages specified in the above lists.
# This also sets the departure time.
truck3 = Truck.Truck('Truck 3')    # Name of truck. Irrelevant to how it runs. Just adds additional customization.
truck3_leave_time = 11.0           # Truck leave time is customizable. This constant does not change.

# Calls the load_truck method. This takes the packages, loads up the truck, and leaves at the specified time.
truck3.load_truck(truck3_packages, hash_table, truck3_leave_time)

# Begins the route for each truck
truck1.begin_route(hash_table)
truck2.begin_route(hash_table)
truck3.begin_route(hash_table)

# Prints the Completion Time and Total Mileage of each Truck.
# Also prints the overall total mileage of the trucks combined.
print_results()

# This is the beginning of what the user sees when running the application.

# User is prompted for a specific time in the format HH:MM.
print("To quit, type 'quit'")
user_input = ''
while user_input != 'quit':
    user_input = input("Please Enter in a Specific Time (Format: HH:MM): ")
    user_input = convert_string_to_time(user_input)    # converts the user_input to a float for use.

    # Calls the print_packages method for each truck and displays the packages with the correct statuses depend on
    # the time entered.
    print_packages(user_input, truck1_leave_time, truck1_packages)
    print_packages(user_input, truck2_leave_time, truck2_packages)
    print_packages(user_input, truck3_leave_time, truck3_packages)
