

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for s in string:
        hash = (( hash << 5) + hash) + ord(s)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_value = Pair(key, value)
    index_value = hash(key, hash_table.capacity)

    if hash_table.storage[index_value] is None:
        hash_table.storage[index_value] = new_value
        print(f"added {new_value.value} to the hash table")
        return hash_table.storage[index_value].value
    else:
        hash_table.storage[index_value] = new_value
        print(f"{new_value.value} caused a collision")
        return hash_table.storage[index_value].value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    val = hash_table.storage[hash(key, hash_table.capacity)]

    if val is None:
        print("no item remove")
        return None
    else:
        hash_table.storage[hash(key, hash_table.capacity)] = None
        print("item removed")
        return


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    val = hash_table.storage[hash(key, hash_table.capacity)]

    if val is None:
        return None
    else:
        print(f"retrieve a value: {val.value}")
        return val.value

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
