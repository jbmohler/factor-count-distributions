#!/usr/bin/env python
import sys
import math
import collections
import random
import sympy.ntheory as ntheory


def is_prime(n):
    return ntheory.isprime(n)

def count_factors(n):
    ff = ntheory.factorint(n)
    return sum([mult for _, mult in ff.items()])


range_max = 10
range_min = 1
mult = 2.
ratio = 1.
while True:
    scount = int((range_max - range_min) * ratio)

    print('{:,} - {:,} samples {:,}'.format(range_min, range_max, scount))

    if True:
        samples = random.sample(range(range_min, range_max), scount)

        iter = (count_factors(n) for n in samples)
        cc = collections.Counter(iter)

        for line, count in sorted(cc.items()):
            print('{:>8} {:>8}'.format(line, count))

        print('*' * 40)
        sys.stdout.flush()

    range_max *= 10
    range_min *= 10
    ratio /= mult
    mult = (6.*mult + 10.)/7.

    if range_min > 1e30:
        break
