import scipy.special as sc
import numpy


def psi_i(R, zero, bessel):
    return sc.jn(1, zero / 2) / (zero * numpy.power(sc.jn(1, zero), 2))


def calculate(r, t, N, R, c, a, k, l):  # TODO check for T
    BESSEL_FIRST_ORDER = sc.jn(1, R / 2)
    result = 0
    zeros = sc.jn_zeros(0, N )
    for i in range(N):
        result += psi_i(R, zeros[i], BESSEL_FIRST_ORDER) * numpy.exp(-t * (2 * a / l + k *
                                                                           (numpy.power(zeros[i] / R, 2))) / c) * \
                  sc.jn(0, zeros[i] / R * r)
    return result


def accurancy(epsilon):
    return 100  # TODO
