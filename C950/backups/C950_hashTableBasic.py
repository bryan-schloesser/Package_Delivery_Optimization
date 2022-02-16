# E.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that
# takes the following components as input and inserts the components into the hash table: •   package ID number •
# delivery address •   delivery deadline •   delivery city •   delivery zip code •   package weight •   delivery
# status (e.g., delivered, en route)


# Hash Table Insertion Function - Input: Package ID Number, Delivery Address, Deliver deadline
# , delivery city, zip, packiage eight, delivery status

# Hashing function

class HashMap:
    def __init__(self):
        self.size = 7
        self.map = [None] * self.size  # constructs array with fixed length

    # Private function that takes a key and calculates the index for it and returns the index
    def _get_hash(self, key):  # key to find the index of
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]  # What we want to insert into cell

        # Checks for empty cell
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])  # adds if empty
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print('---Packages List---')
        for item in self.map:
            if item is not None:
                print(str(item))


hash_table = HashMap()

hash_table.add('1234', '262-9578')
hash_table.add('4445', '342-4294')
hash_table.add('6433', '988-4632')
hash_table.add('6334', '888-tits')

hash_table.print()
print(hash_table.get('Bob'))
hash_table.delete('Bob')
hash_table.print()

hash_table.get('Bryan')
