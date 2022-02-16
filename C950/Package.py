# Imports
import CSV_Extractor


# Global function that is used to format the time float number to a string.
def format_time(time):
    return '{0:02.0f}:{1:02.0f}'.format(*divmod(time * 60, 60))


# Global function to insert package data into hash table.
def package_data_to_hash_table(hash_table):
    # Loop that loops through all the package data in the csv file. This has a time complexity of O(n). This is
    # because it is reliant on how much package data is in the list. Currently, there are only 40. However, this is
    # scalable.
    for package in CSV_Extractor.import_csv("CSV_Data/packageFile.csv"):
        pkg_id = int(package[0])
        pkg_address = package[1]
        pkg_city = package[2]
        pkg_state = package[3]
        pkg_zipcode = package[4]
        pkg_deadline = package[5]
        pkg_weight = package[6]
        pkg_notes = package[7]
        pkg_status = "At Hub"
        pkg_delivery_time = 0.0

        # Package object crated based on the row in the csv file.
        package_obj = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zipcode, pkg_deadline,
                              pkg_weight,
                              pkg_notes, pkg_status, pkg_delivery_time)

        # Inserts package into hash table. Package ID is the key and the rest is the data associated with said key.
        hash_table.insert(pkg_id, package_obj)


# Package class constructor
class Package:
    def __init__(self, package_id, address, city, state, zipcode, delivery_deadline, weight, special_notes, status,
                 delivery_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.delivery_time = delivery_time

    # This method is used to return string values of package data. This was taken from one of the webinars.
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s %s %s" % \
               (self.package_id, self.address, self.city, self.state, self.zipcode,
                self.delivery_deadline, self.weight, self.special_notes, self.status, self.delivery_time)

    # Getter for package id
    def getID(self):
        return self.package_id

    # Setter for package id
    def set_ID(self, pkg_id):
        self.package_id = pkg_id

    # Getter for address
    def get_address(self):
        return self.address

    # Setter for address
    def set_address(self, address):
        self.address = address

    # Getter for city
    def get_city(self):
        return self.city

    # Setter for city
    def set_city(self, city):
        self.city = city

    # Getter for state
    def get_state(self):
        return self.state

    # Setter for state
    def set_state(self, state):
        self.state = state

    # Getter for zipcode
    def get_zipcode(self):
        return self.zipcode

    # Setter for zipcode
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode

    # Getter for deadline
    def get_delivery_deadline(self):
        return self.delivery_deadline

    # Setter for deadline
    def set_delivery_deadline(self, delivery_deadline):
        self.delivery_deadline = delivery_deadline

    # Getter for weight
    def get_weight(self):
        return self.weight

    # Setter for weight
    def set_weight(self, weight):
        self.weight = weight

    # Getter for special notes
    def get_special_notes(self):
        return self.special_notes

    # Setter for special notes
    def set_special_notes(self, special_notes):
        self.special_notes = special_notes

    # Getter for status
    def get_status(self):
        return self.status

    # Setter for status
    def set_status(self, status):
        self.status = status

    # Getter for time
    def get_delivery_time(self):
        return self.delivery_time

    # Setter for time
    def set_delivery_time(self, time):
        self.delivery_time = time

    # This method with print the package data out "neatly" when called.
    def print_package(self):
        print("||Package ID: " + str(
            self.package_id) + " ||Address: " + self.address + "  " + self.city + ", " + self.state + "  "
            + self.zipcode + " ||Deadline: " + self.delivery_deadline + " ||Weight: " + str(
            self.weight) + " ||Special Notes: " + self.special_notes + " ||Status: " + self.status + " ||Time: " +
            format_time(self.delivery_time) + " ||")
