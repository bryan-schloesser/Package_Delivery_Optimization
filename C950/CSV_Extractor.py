# Imports
import csv


# This function is used to import the data from the other two csv files.
# The time complexity of this is O(n) due to the for loop running n times
# based on the amount of rows in each csv file. This looks at each row in the
# csv files and adds the row to a list. Once done, it returns the list of data.
def import_csv(csv_file):
    data_list = []  # New List
    # Opens CSV file. Encoding parameter I found was required due to
    # always having extra data at the beginning of each list that should
    # not have been there. This was because it didn't know what encoding
    # to use.
    with open(csv_file, "r", encoding='utf-8-sig') as csv_file:
        # Creates reader to read the csv file.
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Once it hits the end of the row, it appends the data to the
        # list and goes down to the next row until none remain.
        for row in csv_reader:
            data_list.append(row)  # Appends to list

    return data_list  # Returns list
