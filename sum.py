import scipy.special as sc
import numpy


def psi_i(R, zero, bessel):
    return numpy.power(R, 3) / (2 * numpy.power(zero, 2)) * bessel


def calculate(r, t, N, R, c, a, k, l):
    BESSEL_FIRST_ORDER = sc.jn(1, R / 2)
    result = 0
    zeros = sc.jn_zeros(0, N)
    for i in range(N - 1):
        result += psi_i(R, zeros[i], BESSEL_FIRST_ORDER)
        result += numpy.exp(-t / c * (2 * a / l + k * (numpy.power(zeros[i] / R, 2))))
        result += sc.jn(0, zeros[i] / R * r)
    return result
