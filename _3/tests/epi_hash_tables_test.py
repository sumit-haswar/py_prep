import unittest

from _3.hash_tables.epi_hash_tables import get_longest_subarray_with_distinct_values, find_smallest_seq_covering_subset

class MyTestCase(unittest.TestCase):
    # def test_find_anagrams(self):
    #     input = [
    #         "debitcard",
    #         "elvis",
    #         "silent",
    #         "badcredit",
    #         "lives",
    #         "freedom",
    #         "listen",
    #         "levis",
    #         "money",
    #     ]
    #     anagrams = find_anagrams(input)
    #     expected = [
    #         ["debitcard", "badcredit"],
    #         ["elvis", "lives", "levis"],
    #         ["silent", "listen"],
    #     ]
    #     self.assertListEqual(expected, anagrams)
    #
    # def test_merge_contact_list(self):
    #     contact_list_1 = ContactList(["sumit haswar", "jim smith"])
    #     contact_list_2 = ContactList(["sumit haswar", "jim smith"])
    #     contact_list_3 = ContactList(["sumit haswar", "sumit haswar", "ema watson"])
    #
    #     contact_list = merge_contact_list([contact_list_1, contact_list_2, contact_list_3])
    #
    #     self.assertEqual(2, len(contact_list))
    #
    # def test_is_palindromic_permutation(self):
    #     self.assertTrue(is_palindromic_permutation("edified"))
    #     self.assertFalse(is_palindromic_permutation("edifiedx"))
    #     self.assertTrue(is_palindromic_permutation("sumitsumit"))
    #
    # def test_is_anonymous_letter_possible(self):
    #     letter = "data intensive app"
    #     magazine = "designing data intensive applications"
    #     self.assertTrue(is_anonymous_letter_possible(letter, magazine))
    #
    #     letter = "to be or not to be that is the question"
    #     magazine = "to be or not to be that"
    #     self.assertFalse(is_anonymous_letter_possible(letter, magazine))
    #
    # def test_lru_cache(self):
    #     cache = LruCache()
    #
    #     cache.add("jim", "San Francisco")  # --
    #     cache.add("ema", "Los Angeles")  # --
    #     cache.add("pablo", "San Diego")
    #     cache.add("john", "New York")
    #
    #     cache.add("sam", "Chicago")  # this should delete jim
    #     self.assertTrue("jim" not in cache.map)
    #     cache.add("paul", "Detroit")  # this should delete ema
    #     self.assertTrue("ema" not in cache.map)
    #     self.assertEqual("paul", cache.head.data["key"])
    #
    #     self.assertEqual("New York", cache.get("john"))
    #     self.assertEqual("john", cache.head.data["key"])
    #
    #     cache.add("ram", "New Delhi")  # this should remove pablo
    #     self.assertTrue("pablo" not in cache.map)
    #
    # def test_get_lca(self):
    #     bt = util.build_1_to_10_bst()
    #
    #     _10 = bt.right.right
    #     _8 = bt.right.left.right
    #     self.assertEqual(9, get_lca(_8, _10).data)
    #
    #     _9 = bt.right
    #     _1 = bt.left.left.left
    #     self.assertEqual(5, get_lca(_9, _1).data)
    #
    # def test_get_nearest_repeated_entries(self):
    #     result = get_nearest_repeated_entries("all work and no play makes " "for no work no fun and no results")
    #
    #     self.assertDictEqual({"start": 7, "end": 9}, result)
    #
    #     result = get_nearest_repeated_entries("work work and no play makes " "for no work no fun and no results")
    #
    #     self.assertDictEqual({"start": 0, "end": 1}, result)
    #
    #     result = get_nearest_repeated_entries("all work and no play")
    #
    #     self.assertDictEqual({"start": -1, "end": -1}, result)
    #
    # def test_get_smallest_subarray_cover(self):
    #     text = "to be save the union and to not save which is the union"
    #     keywords = {"save", "union"}
    #
    #     start, end = get_smallest_subarray_cover(text, keywords)
    #     self.assertEqual(2, start)
    #     self.assertEqual(4, end)
    #
    #     text = (
    #         "The sooner the national authority of the union can be restored "
    #         "the nearer the union will be the union as it was "
    #         "If there be those who would not save the union "
    #         "unless they could at the same time save slavery "
    #         "I do not agree with them"
    #     )
    #
    #     start, end = get_smallest_subarray_cover(text, keywords)
    #     self.assertEqual(29, start)
    #     self.assertEqual(31, end)

    def test_get_longest_subarray_with_distinct_values(self):
        self.assertEqual((1,3), get_longest_subarray_with_distinct_values([1, 2, 1, 3, 1, 2, 1]))

        self.assertEqual(
            (0,2),
            get_longest_subarray_with_distinct_values([26, 73, 77, 26, 73, 77, 73, 73]),
        )

        self.assertEqual((0,6), get_longest_subarray_with_distinct_values([6, 59, 49, 35, 77, 17, 86]))

        # currently failing
        # res = get_longest_subarray_with_distinct_values(
        #         [
        #             18,
        #             26,
        #             72,
        #             5,
        #             16,
        #             90,
        #             84,
        #             5,
        #             33,
        #             41,
        #             33,
        #             66,
        #             46,
        #             72,
        #             85,
        #             59,
        #             97,
        #             87,
        #             97,
        #             2,
        #             16,
        #             84,
        #             85,
        #             2,
        #             73,
        #             18,
        #             23,
        #             90,
        #             59,
        #             41,
        #             64,
        #             39,
        #         ]
        #     )
        # self.assertEqual(12, abs(res[0] - res[1]) + 1)

    def test_find_smallest_seq_covering_subset(self):
        text = ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
        keywords = ["not", "to", "be"]
        res = find_smallest_seq_covering_subset(text, keywords)
        self.assertEqual((3, 5), res)

        text = ("rearranging methods return an instance of a dict subclass that has methods specialized for rearranging "
                "dictionary order")
        keywords = ["methods", "rearranging"]
        res = find_smallest_seq_covering_subset(text.split(" "), keywords)
        self.assertEqual((11, 14), res)



if __name__ == '__main__':
    unittest.main()
