# Name: Bryan Schloesser - Student ID: #001103177

# Imports capability to interact with csv files
import csv
from math import sqrt


class Package:
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes

    def getEverything(self):
        return self.package_id, self.address, self.city


class Truck:
    def __init__(self, package_list):
        self.package_list = package_list
        self.load_truck(self.package_list)

    def load_truck(self, package_id_list):
        converted_list = []
        for item in self.package_list:
            converted_list.append(hash_table.search(item))
        self.package_list = converted_list


# Imports distance data from csv file
def import_distance_data():
    distances_list = []  # Array where the data is stored
    with open("distanceTable.csv", "r", encoding='utf-8-sig') as csv_file:
        # Instantiating the csv reader
        csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

        # Loops through the rows in the csv file and adds the whole row into one index in the list.
        for row in csv_reader:
            distances_list.append(row)

    return distances_list  # Returns the list with the data


# Imports package data from csv file
def import_package_data():
    package_list = []  # Array where the data is stored
    with open("packageFile.csv", "r", encoding='utf-8-sig') as csv_file:
        # Instantiating the csv reader
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Loops through the rows in the csv file and adds the whole row into one index in the list.
        for row in csv_reader:
            package_list.append(row)

    return package_list  # Returns the list with the data


# HashTable class using chaining.
class HashTable:

    # Initializes the HashTable
    def __init__(self):
        self.size = 20  # Hardcoded capacity of the list
        self.table = [[]] * self.size  # creates list with self.size amount of buckets.

    # Hashing Method
    def get_hash(self, package_id):  # takes the package id and creates the hash using it.
        return package_id % self.size  # returns the hash location (package_id mod size_of_list)

    # Inserts package into hash table
    def insert(self, package_id, package):
        # Determine bucket for placement into has table
        bucket = self.get_hash(package_id)
        # List of the contents of the hash location
        bucket_list = self.table[bucket]

        for pair in bucket_list:
            if pair[0] == package_id:
                pair[1] = package
                print("This is not getting called")
                return True

        key_value = [package_id, package]
        bucket_list.append(key_value)
        return True

    def search(self, package_id):
        # get the bucket list where this key would be.
        bucket = self.get_hash(package_id)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == package_id:
                return item[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, package_id):
        # get the bucket list where this item will be removed from.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if package_id in bucket_list:
            bucket_list.remove(package_id)

    def print(self):
        print('---Packages List---')
        for i in range(self.size + 1):
            print("key: {} and Package: {}".format(i + 1, self.search(i + 1)))


def package_data_to_hash_table():
    for package in import_package_data():
        pkg_id = int(package[0])
        pkg_address = package[1]
        pkg_city = package[2]
        pkg_state = package[3]
        pkg_zipcode = package[4]
        pkg_deadline = package[5]
        pkg_weight = package[6]
        pkg_notes = package[7]

        package_obj = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zipcode, pkg_deadline, pkg_weight,
                              pkg_notes)

        hash_table.insert(pkg_id, package_obj)


# calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


# Instantiates the hash table
hash_table = HashTable()

# Loads package data into hash table
package_data_to_hash_table()

# Loads distance data into a list
distance_list = import_distance_data()

# Loads address data into a list

# Specifies what packages go on what trucks
truck1_packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2_packages = [3, 6, 18, 25, 28, 32, 36, 38]
truck3_packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]

# Creates the truck objects and loads the trucks with the packages specified in the above lists
truck1 = Truck(truck1_packages)
truck2 = Truck(truck2_packages)
truck3 = Truck(truck3_packages)
print(distance_list)

hash_table.print()

