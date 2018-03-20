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


def TDMA(a, b, c, f, I):
    """
    Данный код работает при предположении, что a[0] = 0, b[n-1] = 0
    *b - диагональ, лежащая над главной(нумеруется: [0; n - 2])
    *c - главная диагональ матрицы A(нумеруется: [0; n - 1])
    *a - диагональ, лежащая под главной(нумеруется: [1; n - 1])
    *f - правая часть(столбец)
    *x - решение, массив x будет содержать ответ
    """

    #a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = I
    x = [0 for i in range(n)]

    for i in range(n - 1):
        alpha.append(-b[i] / (a[i] * alpha[i] + c[i]))
        beta.append((f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i]))

    x[n - 1] = (f[n - 1] - a[n - 2] * beta[n - 1]) / (c[n - 1] + a[n - 2] * alpha[n - 1])

    for i in reversed(range(n - 1)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x


def calculate_numerically(I, K, R, T, cc, alpha, q, l):
    hr = R / I
    ht = T / K
    gamma = q * ht / (cc * hr * hr)
    b = []
    c = []
    a = []
    f = []

    v = [0] * K
    for i in range(K):
        v[i] = [0] * I

    for j in range(I):
        if j < I / 2:
            v[0][j] = 1
        else:
            v[0][j] = 0

    b.append(2 * gamma)
    c.append(-2 * gamma + 4 * alpha * ht / (l * cc))
    a.append(0)
    for j in range(1, I):
        b.append(-gamma * (1 + 1 / (2 * j)))
        c.append(1 + 2 * gamma + 2 * alpha * ht / (l * cc))
        a.append(-gamma * (1 - 1 / (2 * j)))
    b[I - 1] = 0

    for k in range(1, K):
        for j in range(I):
            f.append(v[k - 1][j])
        v[k] = TDMA(a, b, c, f, I)
        f = []
    return v
