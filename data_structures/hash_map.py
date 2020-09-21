from .ds import Entry

# implement hashmap using python list
class HashMap():

    def __init__(self):
        self._hash_map = [None] * 100
        self._size = 100
        self._count = 0
        self._threshold = 0.8

    def contains_key(self, key):
        try:
            idx = self._get_hash_code(key)
            if self._hash_map[idx]:
                return True
        except Exception as e:
            return False
        return False

    def get(self, key):
        # get hash-code for key
        idx = self._get_hash_code(key)
        # check if hash-code exists in self._hash_map
        entry_list = self._hash_map[idx]
        if entry_list:
            for entry in entry_list:
                if entry.key == key:
                    return entry.val
            return None
        else:
            return None

    def is_empty(self):
        return self._count > 0

    def _resize(self):
        new_map = [None] * (self._size * 2)
        for idx, elem in enumerate(self._hash_map):
            new_map[idx] = self._hash_map[idx]

        self._hash_map = new_map

    def put(self, key, value):

        if (self._count + 1) > (0.8 * self._size):
            self._resize()

        idx = self._get_hash_code(key)
        entry_list = self._hash_map[idx]
        if entry_list:
            entry_list.append(Entry(key, value))
        else:
            entry = Entry(key, value)
            self._hash_map[idx] = [entry]

        self._count += 1

    def remove(self, key):
        pass

    def _get_hash_code(self, key):
        hash = id(key)
        hash = hash % self._size
        return hash
