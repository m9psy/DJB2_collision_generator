# coding: utf8

"""Values to test was generated with authentic C version from http://www.cse.yorku.ca/~oz/hash.html"""

from djb2_collision_generator.hash_functions import djb2_32, djb2_64
import unittest


# Copy it here
# unsigned long
# hash(unsigned char *str)
# {
#     unsigned long hash = 5381;
#     int c;
#
#     while (c = *str++)
#         hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
#
#     return hash;
# }

# 64 bit is absolutely same, except hash type is unsigned long long

class Bit32DJB2Tester(unittest.TestCase):
    def setUp(self):
        self.values = {
            "yolo": 2090946536,
            "hurr-durr": 2474838256,
            "\x01\x02\x03\x04\x05": 135413428,
            "": 5381
        }

    def test_hash_is_correct(self):
        for target_string, target_hash in self.values.items():
            self.assertEqual(target_hash, djb2_32(target_string))


class Bit64DJB2Tester(unittest.TestCase):
    def setUp(self):
        self.values = {
            "yolo & yolo64": 14349964537028866779,
            "hurr-durr & hurr-durr64": 6692487194679278219,
            "\x01\x02\x03\x04\x05\x64\x05\x04\x03\x02\x01": 13714286920460930471
        }

    def test_hash_is_correct(self):
        for target_string, target_hash in self.values.items():
            self.assertEqual(target_hash, djb2_64(target_string))
