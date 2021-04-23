import string


class Base64Converter():

    def __init__(self):
        self.lookup = string.digits + string.ascii_lowercase + string.ascii_uppercase + "-_"
        self.base = 64

    def encode(self, value):
        """convert a decimal value to base-64 value """
        key = []
        curr_val = value
        while curr_val >= 64:
            rem = curr_val % 64
            key.append(self.lookup[rem])
            curr_val = curr_val // 64
        if curr_val > 0:
            key.append(self.lookup[curr_val])
        return "".join(reversed(key))

    def decode(self, key):
        """convert a base 64 number to base-10 number"""
        result = 0
        pow = 1
        for idx in range(len(key) - 1, -1, -1):
            ch = key[idx]
            lookup_idx = self.lookup.index(ch)
            result += lookup_idx * pow
            pow = pow * 64

        return result