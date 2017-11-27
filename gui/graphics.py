import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import calculation


def print_r_graphic(r, N, R, c, a, k, l, T, graphics_r_frame):
    f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
    plot = f.add_subplot(111)
    t = numpy.linspace(0, T, T * 100)
    plot.plot(t, calculation.calculate(r, t, N, R, c, a, k, l))
    plot.set_xlabel("t")
    plot.set_ylabel("u(r, t)")
    canvas = FigureCanvasTkAgg(f, graphics_r_frame)
    canvas.get_tk_widget().grid(row=1, column=0)  # позиция
    canvas.draw()
    canvas.show()


def print_t_graphic(t, N, R, c, a, k, l, T, graphics_t_frame):
    f = Figure(figsize=(10, 5), dpi=60)  # изменения размеров
    plot = f.add_subplot(111)
    r = numpy.linspace(0, R, R * 100)
    plot.plot(r, calculation.calculate(r, t, N, R, c, a, k, l))
    plot.set_xlabel("r")
    plot.set_ylabel("u(r, t)")
    canvas = FigureCanvasTkAgg(f, graphics_t_frame)
    canvas.get_tk_widget().grid(row=1, column=0)  # позиция
    canvas.draw()
    canvas.show()


