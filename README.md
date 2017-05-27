# DJB2 hash function collision generator

This package demonstrates how to generate collision for any given value for djb2 function. Authentic realization is taken from [here](http://www.cse.yorku.ca/~oz/hash.html). You can find Python implementation in `djb2_collision_generator/hash_functions.py` directory - it is pretty straightforward.

High collision rate can lead to hash table exhaustion which will lead to O(n) access complexity. This situation is commonly named as "Hash table DoS attack". So [never ever use](https://bugs.php.net/bug.php?id=70644) this function in hash table.

How to use:

No additional dependencies required.

1. Just clone: `git clone https://github.com/m9psy/DJB2_collision_generator`
2. `cd DJB2_collision_generator/djb2_collision_generator`
3. `python generator.py 0`

`generator.py <target> <length>` accepts 2 params:
1. `target` - target hash value to collide
2. `length` - length of the resulting collision string

By default 32 length is used, which is very long string. For 32-bit `djb` 10 symbols will be more than enough and script will automatically increment length if there are not enough unique collisions left. Also generation speed depends on the length - I expect 1 collision complexity is O(n * 256 * r * c), where `r` - number of rounds, `c` -  is number of attempts. There may be infinite number of attempts, so worst case to generate 1 collision is pretty high (worst case is simply brute-force). Best case is O(256), average O(n * 256) `python generator.py 0 10` - generate 10 symbols strings for 0 hash value. Like this:

```
b'\xe0\xcf^\xaa\x13L\xc1\x01\xe1\xa2'
b'\x9e\xf8\xe9M\xf8\x15 \xbc \x06'
b'g\xbc<\xad\xf4\x0b]8\xb8c'
b'\xd0T\x9d\x07\xfb\x02\x10\xf63]'
b'\xe0yL\xc4\x08\xa9\xf1\x14\xa1{'
b'\xf6H`\xea\xec\x80XZ~\x97'
b'\xa0\x13\r\xdf8\xc9\x90\xbc\xaeA'
b'~Y#\x14\xd9%\xe6\xcf\x1e\x9c'
b'I\xd9\xc8\xad\x8d8\xc0\xd1\xb4Z'
```

Generation speed is _pretty fast_ - actual speed may vary (because the process is mostly random). So you can expect to generate dozens of collisions in a couple of hours/days. No memory needed (couple of Mbs).

Also you can try this generator for other hash functions.
