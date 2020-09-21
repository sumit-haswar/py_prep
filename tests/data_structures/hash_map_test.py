import unittest
import string
from data_structures import HashMap
from random import randint


class MyTestCase(unittest.TestCase):

    def test_hash_map_resize(self):
        hs = HashMap()
        py_dict = {}

        for i in range(120):
            key = ''.join([string.ascii_lowercase[randint(0, 25)]
                           for _ in range(10)])
            value = ''.join([string.ascii_lowercase[randint(0, 25)]
                             for _ in range(10)])

            # add to py dict
            py_dict[key] = value

            # add to hash_map
            hs.put(key, value)

        for entry in py_dict.items():
            self.assertEqual(entry[1], hs.get(entry[0]))

    def test_hash_map(self):
        hs = HashMap()

        hs.put('name', 'Sumit Haswar')
        hs.put('city', 'San Francisco')
        hs.put('tel', '716-479-7356')

        self.assertEqual('Sumit Haswar', hs.get('name'))
        self.assertEqual('San Francisco', hs.get('city'))
        self.assertEqual('716-479-7356', hs.get('tel'))


if __name__ == '__main__':
    unittest.main()
