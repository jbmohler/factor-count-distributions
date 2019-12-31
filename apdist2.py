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

def exhaustive_check():
    range_max = 2
    range_min = 1
    while True:
        print('{:,} - {:,}'.format(range_min, range_max))

        iter = (count_factors(n) for n in range(range_min, range_max))
        cc = collections.Counter(iter)

        for line, count in sorted(cc.items()):
            print('{:>8} {:>8}'.format(line, count))

        print('*' * 40)
        sys.stdout.flush()

        range_max *= 2
        range_min *= 2

        if range_min > 2e8:
            break

def exhaustive_check_odd():
    range_max = 2
    range_min = 1
    while True:
        print('{:,} - {:,}'.format(range_min, range_max))

        iter = (count_factors(n) for n in range(range_min+1, range_max, 2))
        cc = collections.Counter(iter)

        for line, count in sorted(cc.items()):
            print('{:>8} {:>8}'.format(line, count))

        print('*' * 40)
        sys.stdout.flush()

        range_max *= 2
        range_min *= 2

        if range_min > 2**26:
            break

def spot_check_1mm(exp):
    range_max = 2*2**exp
    range_min = 2**exp
    while True:
        print('{:,} - {:,}'.format(range_min, range_max))

        #print(random.randint(range_min, range_max))
        #print(random.randint(range_min, range_max))
        #print(random.randint(range_min, range_max))
        #print(random.randint(range_min, range_max))
        iter = (count_factors(random.randint(range_min, range_max)) for n in range(1000000))
        cc = collections.Counter(iter)

        for line, count in sorted(cc.items()):
            print('{:>8} {:>8}'.format(line, count))

        print('*' * 40)
        sys.stdout.flush()

        range_max *= 2
        range_min *= 2

        if range_min > 2e8:
            break

sampling = False
odd = True
if sampling:
    import sys
    exp = int(sys.argv[1])
    #print(exp)
    spot_check_1mm(exp)
elif odd:
    exhaustive_check_odd()
