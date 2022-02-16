# Imports
import CSV_Extractor
import Package


# Hash Table class
class HashTable:

    # Initializes the HashTable
    def __init__(self, size):
        self.table = []  # Table of where the data is going to go
        self.size = size

        # Loop has a time complexity of O(n) this is dependent on the size of the size variable specified.
        for i in range(size):
            self.table.append([])

    # This is method is how hash table determines what bin to place the package in and how it knows what bin a specific
    # package is located in. If the bin is full, it will append the package to the bin.
    def get_hash(self, package_id):  # takes the package id and creates the hash using it.
        return package_id % self.size  # returns the hash location (package_id mod size_of_list)

    # Inserts package into hash table
    def insert(self, package_id, package):
        # Determine bucket for placement into hash table
        bucket = self.get_hash(package_id)
        # List of the contents of the hash location
        bucket_list = self.table[bucket]

        # Loop has a time complexity of O(n). The complexity is dependent on how many packages are in the bucket.
        # The loop checks to see if the package already exists in the bucket. If it does, it returns true.
        for pair in bucket_list:
            if pair[0] == package_id:
                pair[1] = package
                return True
        # If the loop completes and the package is not in the bucket, this will add the package to the bucket.
        key_value = [package_id, package]  # Adds package to bucket.
        bucket_list.append(key_value)  # Appends bucket to the hash table.
        return True  # Returns once added.

    # This method accepts a package id as input. It then calls the get_hash method to determine what bucket to look in.
    # It then loops through the items in the bucket (in case of collisions) and returns the item whose key is equal to
    # the package id.
    def search(self, package_id):
        bucket = self.get_hash(package_id)  # Gets the bucket list where this key would be.
        bucket_list = self.table[bucket]  # creates a list of the contents of the bucket.

        # The loop time complexity is O(n). The time complexity is dependent on how many items are in bucket_list.
        # If there are numerous collisions, it will increase the time complexity.
        for item in bucket_list:
            if item[0] == package_id:  # If the key equals the package ID, a matching package was found.
                return item[1]  # Returns the package data.
        return None  # Returns none if no package was found

    # Removes a package from the hash table.
    def remove(self, package_id):
        # get the bucket list where this item will be removed from.
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if package_id in bucket_list:
            bucket_list.remove(package_id)