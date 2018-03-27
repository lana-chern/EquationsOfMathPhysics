from tkinter import *
from gui import graphics
from gui import entries
from gui import labels
import calculation
from gui.graphics import MyGraphics


def init_frames(root):
    initial_data_frame = Frame(root, bd=1)
    fourier_series_frame = Frame(root, bd=1)
    numerically_frame = Frame(root, bd=1)
    graphics_r_frame = Frame(root, bd=1)
    graphics_t_frame = Frame(root, bd=1)

    initial_data_frame.grid(row=0, column=0)
    fourier_series_frame.grid(row=1, column=0)
    numerically_frame.grid(row=2, column=0)
    graphics_r_frame.grid(row=0, column=1, rowspan=8, sticky="n")
    graphics_t_frame.grid(row=0, column=2, rowspan=8, sticky="n")
    return [initial_data_frame, fourier_series_frame, numerically_frame, graphics_r_frame, graphics_t_frame]


def init_buttons(root, graphics_r_frame, graphics_t_frame, graphic):
    but_calculate = Button(root, text="Построить графики")
    but_calculate.grid(row=3, column=0, padx=5, pady=5)
    but_calculate.bind("<Button-1>", print_graph)

    data = [graphics_r_frame, graphics_t_frame, graphic]
    but_calculate.bind("<Button-1>", lambda event, arg=data: print_graph(event, arg))


def print_graph(event, arg):
    N = entries.get_N()
    if entries.get_epsilon() != 0:
        N = calculation.accuracy(entries.get_epsilon(), labels.t_scale_value.get(), entries.get_radius(),
                                 entries.get_c(), entries.get_alpha(), entries.get_q(), entries.get_L())
    #else:
        #calculation.accuracy_e(N, labels.t_scale_value.get(), entries.get_radius(),
         #                      entries.get_c(), entries.get_alpha(), entries.get_q(), entries.get_L())

    graphic = arg[2]
    graphic.print_r_graphic(labels.r_scale_value.get(), N, entries.get_radius(),
                            entries.get_c(), entries.get_alpha(), entries.get_q(),
                            entries.get_L(), entries.get_time(), entries.get_I(), entries.get_K(), arg[0])
    graphic.print_t_graphic(labels.t_scale_value.get(), N, entries.get_radius(),
                            entries.get_c(), entries.get_alpha(), entries.get_q(),
                            entries.get_L(), entries.get_time(), entries.get_I(), entries.get_K(), arg[1])

    max1 = graphic.experiment(entries.get_I(), entries.get_K(), N, entries.get_radius(), entries.get_c(),
                              entries.get_alpha(), entries.get_q(), entries.get_L(), entries.get_time())
    print("max:", max1)
    print("Ready")
