# Class for generating HashMap dataset
# Citing source: https://www.geeksforgeeks.org/hash-map-in-python/
class Generate:
    def __init__(self, initial_capacity=30):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Known as "remove", deletes value from hash table
    def delete_val(self, key):
        hashed_key = hash(key) % len(self.list)
        destination = self.list[hashed_key]

        if key in destination:
            destination.remove(key)

    # Known as "insert", sets value into hash table
    # Operates in Big O of O(n)
    def set_val(self, key, item):
        hashed_key = hash(key) % len(self.list)
        bucket_list = self.list[hashed_key]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Known as "lookup", get value is a "search" of hash table
    def get_val(self, key):
        hashed_key = hash(key) % len(self.list)
        bucket_list = self.list[hashed_key]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None
