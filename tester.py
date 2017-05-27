# coding: utf-8

from djb2_collision_generator.generator import GreedyGenerator
from djb2_collision_generator.hash_functions import djb2_32, djb2_64

# gen = GreedyGenerator(djb2_64, 1180004904744509286)
gen = GreedyGenerator(djb2_32, 744509286, 10)

collisions = set()

for collision in gen:
    print(collision)
    print(gen._paste_to_c(collision))
    collisions.add(bytes(collision))
    print(len(collisions))
