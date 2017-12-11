import scipy.special as sc
import numpy
import math


def psi_i(zero):
    return sc.jn(1, zero / 2) / (zero * numpy.power(sc.jn(1, zero), 2))


def calculate(r, t, N, R, c, a, k, l):
    result = 0
    zeros = sc.jn_zeros(0, N)
    for i in range(N):
        result += psi_i(zeros[i]) * numpy.exp(-t * (2 * a / l + k *
                                                    (numpy.power(zeros[i] / R, 2))) / c) * \
                  sc.jn(0, zeros[i] / R * r)
    return result


def accuracy(epsilon, t, R, c, a, k, l):
    current_accuracy = 100000
    n = 2
    while current_accuracy > epsilon:
        current_accuracy = numpy.sqrt(math.pi / 2) * numpy.exp(
            -2 * a * t / (l * c) - k * numpy.power(n - 1, 2) * math.pi * math.pi * t / (R * R * c)) * R * R * c / (
                               numpy.sqrt(math.pi * n * (n - 1)) * k * math.pi * math.pi * t)
        if current_accuracy < epsilon:
            break
        n += 1
    print(current_accuracy, epsilon)
    print(n)
    return n


def accuracy_e(n, t, R, c, a, k, l):
    n_t = 2
    current_accuracy = 0
    while n_t < n:
        current_accuracy = numpy.sqrt(math.pi / 2) * numpy.exp(
            -2 * a * t / (l * c) - k * numpy.power(n_t - 1, 2) * math.pi * math.pi * t / (R * R * c)) * R * R * c / (
                               numpy.sqrt(math.pi * n_t * (n_t - 1)) * k * math.pi * math.pi * t)
        n_t += 1
    print(current_accuracy)
