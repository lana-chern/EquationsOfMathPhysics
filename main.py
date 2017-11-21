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
    t = 5
    # r = 3
    N = 1000
    r = numpy.linspace(0, R, 1000)
    result = sum.calculate(r, t, N, R, c, a, k, l)
    pl.plot(r, result)
    pl.grid()
    pl.show()
