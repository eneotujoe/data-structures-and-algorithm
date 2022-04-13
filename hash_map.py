

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.values = [None for _ in range(self.size)]

    def get_hash(self, key):
        hashed_key = 0
        for char in key:
            hashed_key += ord(char)
        
        return hashed_key % self.size

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, val):
        hashed_key = self.get_hash(key)
        self.values[hashed_key] = val

    def __getitem__(self, key):
        hashed_key = self.get_hash(key)
        return self.values[hashed_key]

    def __delitem__(self, key):
        hashed_key = self.get_hash(key)
        self.values[hashed_key] = None


if __name__=='__main__':
    hash_map = HashTable()
    hash_map['name'] = 'John Terry'
    hash_map['age'] = 30
    hash_map['gender'] = 'male'
    print(hash_map.values)
    print(hash_map['age'])