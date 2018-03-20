import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as pl
import calculation


def print_r_graphic(r, N, R, c, a, k, l, T, I, K, graphics_r_frame):
    hr = R / I
    f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
    plot = f.add_subplot(111)
    t = numpy.linspace(0, T, K+1)
    v = calculation.calculate_numerically(I, K, R, T, c, a, k, l)
    v1 = [0]*(K+1)
    for j in range(K+1):
        v1[j] = v[j][int(r / hr)]
    plot.plot(t, v1, label='Прогонка')
    plot.plot(t, calculation.calculate(r, t, N, R, c, a, k, l), label='Аналитически')
    plot.set_xlabel("t")
    plot.set_ylabel("u(r, t)")
    plot.set_ylim(-0.1, 1.1)
    plot.legend()
    canvas = FigureCanvasTkAgg(f, graphics_r_frame)
    canvas.get_tk_widget().grid(row=1, column=0)  # позиция
    canvas.draw()
    canvas.show()


def print_t_graphic(t, N, R, c, a, k, l, T, I, K, graphics_t_frame):
    ht = T / K
    f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
    plot = f.add_subplot(111)
    r = numpy.linspace(0, R, I+1)
    v = calculation.calculate_numerically(I, K, R, T, c, a, k, l)
    #r1 = numpy.linspace(0, I, I)
    plot.plot(r, v[int(t / ht)], label='Прогонка')
    plot.plot(r, calculation.calculate(r, t, N, R, c, a, k, l), label='Аналитически')
    plot.set_xlabel("r")
    plot.set_ylabel("u(r, t)")
    plot.set_ylim(-0.1, 1.1)
    plot.legend()
    canvas = FigureCanvasTkAgg(f, graphics_t_frame)
    canvas.get_tk_widget().grid(row=1, column=0)  # позиция
    canvas.draw()
    canvas.show()

    # print(v[20])
    # pl.plot(range(100), v[20])
    # pl.show()
