class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value
        raise KeyError("Key not found")

    def display(self):
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")

# Creating a hash table with size 10
my_hash_table = HashTable(10)

# Inserting key-value pairs
my_hash_table.insert("apple", 5)
my_hash_table.insert("banana", 8)
my_hash_table.insert("grape", 12)

# Displaying the hash table
my_hash_table.display()

# Retrieving values
print("Value for 'apple':", my_hash_table.get("apple"))  # Output: Value for 'apple': 5
print("Value for 'banana':", my_hash_table.get("banana"))  # Output: Value for 'banana': 8
