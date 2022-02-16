
class HashMap:
    def __init__(self):
        self.size = 1
        self.map = [None] * self.size  # constructs array with fixed length

    # Private function that takes a key and calculates the index for it and returns the index
    def _get_hash(self, package_id):  # key to find the index of
        hash = package_id
        return hash % self.size

    def add(self, package_id, address, deadline, city, zip_code, weight, status):
        key_hash = self._get_hash(package_id)
        key_value = [package_id, address, deadline, city, zip_code, weight, status]  # What we want to insert into cell

        # Checks for empty cell
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])  # adds if empty
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == package_id:
                    pair[1] = package_id, address, deadline, city, zip_code, weight, status
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, package_id):
        key_hash = self._get_hash(package_id)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == package_id:
                    return pair
        return None

    def delete(self, package_id):
        key_hash = self._get_hash(package_id)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == package_id:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('---Packages List---')
        for item in self.map:
            if item is not None:
                print(str(item))


hash_table = HashMap()

hash_table.add(1234, '334 Monroe St', '3/4/2021', 'Fort Atkinson', 53538, 24.34, 'Out for Delivery')
hash_table.add(1331, '1212 Meadowbrook Dr', '9/23/2021', 'Watertown', 53098, 2.30, 'Pending')


hash_table.print()




