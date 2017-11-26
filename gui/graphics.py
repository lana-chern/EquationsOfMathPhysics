import numpy
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from gui import entries
import calculation


def print_r_graphic(t, N, R, c, a, k, l, root):
    f = Figure(figsize=(10, 5), dpi=50)  # изменения размеров
    plot = f.add_subplot(111)
    r = numpy.linspace(0, R, R * 100)
    plot.plot(r, calculation.calculate(r, t, N, R, c, a, k, l))
    plot.set_xlabel("r")
    plot.set_ylabel("u(r, t)")
    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().grid(row=1, column=1)  # позиция
    canvas.draw()


def print_t_graphic(r, N, R, c, a, k, l, T, root):
    f = Figure(figsize=(10, 5), dpi=50)  # изменения размеров
    plot = f.add_subplot(111)
    t = numpy.linspace(0, T, T * 100)
    plot.plot(r, calculation.calculate(r, t, N, R, c, a, k, l))
    plot.set_xlabel("r")
    plot.set_ylabel("u(r, t)")
    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().grid(row=1, column=1)  # позиция
    canvas.draw()



