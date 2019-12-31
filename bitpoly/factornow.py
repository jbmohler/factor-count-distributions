import collections
import sympy


def factor_ofdeg(ofdeg):
    x = sympy.var('x')
    pow2 = [2**i for i in range(ofdeg)]
    for i in range(2**ofdeg):

        coefficients = [(i&p2) // p2 for p2 in pow2[:ofdeg]]
        if ofdeg == -3:
            print(i, coefficients)

        f = x**ofdeg+sum([c*x**i for i, c in enumerate(coefficients)])

        facs = sympy.factor_list(f, modulus=2)
        if ofdeg == -3:
            print(f, ' = ', facs)
        #for x135 in facs:
        #    print(x135)

        yield sum([ff[1] for ff in facs[1]])

for ofdeg in range(1, 13):
    print('degree {}'.format(ofdeg))
    cc = collections.Counter(factor_ofdeg(ofdeg))
    elts = [cc[x] for x in range(1, ofdeg+1)]
    print('  '.join([str(kk) for kk in elts]))
