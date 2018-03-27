import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import calculation


class MyGraphics:
    def __init__(self, param):
        self.__dict__['v'] = [[0], [0]]
        self.__dict__['param'] = param

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__[item]

    def print_r_graphic(self, r, N, R, c, a, q, l, T, I, K, graphics_r_frame):
        hr = R / I
        f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
        plot = f.add_subplot(111)
        t = numpy.linspace(0, T, K + 1)
        param = [R, c, a, q, l, T]
        if (len(self.v) != (K + 1)) | (len(self.v[0]) != (I + 1)) | (not (numpy.array_equal(self.param, param))):
            self.v = calculation.calculate_numerically(I, K, R, T, c, a, q, l)
            self.param = param
        v1 = [0] * (K + 1)
        for j in range(K + 1):
            v1[j] = self.v[j][int(r / hr)]
        plot.plot(t, v1, label='Прогонка')
        plot.plot(t, calculation.calculate(r, t, N, R, c, a, q, l), label='Аналитически')
        plot.set_xlabel("t")
        plot.set_ylabel("u(r, t)")
        plot.set_ylim(-0.1, 1.1)
        plot.legend()
        canvas = FigureCanvasTkAgg(f, graphics_r_frame)
        canvas.get_tk_widget().grid(row=1, column=0)  # позиция
        canvas.draw()
        canvas.show()

    def print_t_graphic(self, t, N, R, c, a, q, l, T, I, K, graphics_t_frame):
        ht = T / K
        f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
        plot = f.add_subplot(111)
        r = numpy.linspace(0, R, I + 1)
        # v = calculation.calculate_numerically(I, K, R, T, c, a, k, l)
        param = [R, c, a, q, l, T]
        if (len(self.v) != (K + 1)) | (len(self.v[0]) != (I + 1)) | (not (numpy.array_equal(self.param, param))):
            self.v = calculation.calculate_numerically(I, K, R, T, c, a, q, l)
            self.param = param
        # r1 = numpy.linspace(0, I, I)
        plot.plot(r, self.v[int(t / ht)], label='Прогонка')
        plot.plot(r, calculation.calculate(r, t, N, R, c, a, q, l), label='Аналитически')
        plot.set_xlabel("r")
        plot.set_ylabel("u(r, t)")
        plot.set_ylim(-0.1, 1.1)
        plot.legend()
        canvas = FigureCanvasTkAgg(f, graphics_t_frame)
        canvas.get_tk_widget().grid(row=1, column=0)  # позиция
        canvas.draw()
        canvas.show()

    def experiment(self, I, K, N, R, c, a, q, l, T):
        #hr = R / I
        #ht = T / K
        t = numpy.linspace(0, T, K + 1)
        r = numpy.linspace(0, R, I + 1)
        v1 = numpy.zeros((K + 1, I + 1))
        for i in range(len(t)):
            for j in range(len(r)):
                v1[i][j] = calculation.calculate(r[j], t[i], N, R, c, a, q, l)
        max = -numpy.inf
        for i in range(K + 1):
            for j in range(I + 1):
                temp = numpy.abs(self.v[i][j] - v1[i][j])
                if temp > max:
                    max = temp
        return max
