# coding: utf-8

from djb2_collision_generator.generator import GreedyGenerator
from djb2_collision_generator.hash_functions import djb2_32, djb2_64

import unittest
import copy


class TestGeneratorIsWorking(unittest.TestCase):
    def setUp(self):
        self.bit32_target = djb2_32("32 bit test. Long string is for purpose. Longer strings better collide?")
        self.bit64_target = djb2_64("64 bit test. Long string is for purpose. Longer strings better collide?")

    def test_32_generation(self):
        print("Running 32 bit collision check. Will take some time.")
        gen = GreedyGenerator(djb2_32, self.bit32_target, 20)
        for i in range(10):
            next_collision = next(gen)
            self.assertEqual(self.bit32_target, djb2_32(next_collision))

    def test_64_generation(self):
        print("Running 64 bit collision check. Will take some time")
        gen = GreedyGenerator(djb2_64, self.bit64_target, 32)
        for i in range(10):
            next_collision = next(gen)
            self.assertEqual(self.bit64_target, djb2_64(next_collision))

    def test_string_length(self):
        gen = GreedyGenerator(djb2_32, self.bit32_target, 20)
        self.assertEqual(self.bit32_target, djb2_32(next(gen)))
        self.assertEqual(len(gen.string_to_guess), 20)

        gen.set_collision_size(24)
        self.assertEqual(self.bit32_target, djb2_32(next(gen)))
        self.assertEqual(len(gen.string_to_guess), 24)

        gen.set_collision_size(64)
        self.assertEqual(self.bit32_target, djb2_32(next(gen)))
        self.assertEqual(len(gen.string_to_guess), 64)

        gen.set_collision_size(128)
        self.assertEqual(self.bit32_target, djb2_32(next(gen)))
        self.assertEqual(len(gen.string_to_guess), 128)

        gen.set_collision_size(256)
        self.assertEqual(self.bit32_target, djb2_32(next(gen)))
        self.assertEqual(len(gen.string_to_guess), 256)

    def test_mutation(self):
        gen = GreedyGenerator(djb2_32, self.bit32_target, 20)
        initial = copy.copy(gen.string_to_guess)
        self.assertNotEqual(initial, gen.mutate_partial(gen.string_to_guess))

        initial_full = copy.copy(gen.string_to_guess)
        self.assertNotEqual(initial_full, gen.mutate_full(gen.string_to_guess))

    def test_hitting_target(self):
        gen = GreedyGenerator(djb2_32, self.bit32_target, 20)
        possible_values = {
            0: 123,
            1: 456,
            3: 666,
            ord(b"A"): self.bit32_target
        }
        gen._check_if_got_it(0, possible_values, self.bit32_target)
        self.assertEqual(gen.string_to_guess[0], ord(b"A"))
