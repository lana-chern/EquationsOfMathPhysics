import matplotlib.pyplot as pl
import sum
import numpy

if __name__ == '__main__':
    k = 0.59
    c = 1.65
    a = 0.006
    R = 6
    l = 0.3
    T = 15
    r = 3
    N = 100
    t = numpy.linspace(0, T, 100)
    result = sum.calculate(r, t, N, R, c, a, k, l)
    pl.plot(t, result)
    pl.show()
