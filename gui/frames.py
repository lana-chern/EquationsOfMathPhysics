from tkinter import *
from gui import graphics
from gui import entries
from gui import labels


def init_frames(root):
    initial_data_frame = Frame(root, bd=1)
    fourier_series_frame = Frame(root, bd=1)
    graphics_r_frame = Frame(root, bd=1)
    graphics_t_frame = Frame(root, bd=1)

    initial_data_frame.grid(row=0, column=0)
    fourier_series_frame.grid(row=1, column=0)
    graphics_r_frame.grid(row=0, column=1, rowspan=8, sticky="n")
    graphics_t_frame.grid(row=8, column=1, rowspan=8, sticky="n")
    return [initial_data_frame, fourier_series_frame, graphics_r_frame, graphics_t_frame]


def init_buttons(root, graphics_r_frame, graphics_t_frame):
    but_calculate = Button(root, text="Построить графики")
    but_calculate.grid(row=2, column=0, padx=5, pady=5)
    but_calculate.bind("<Button-1>", graphics.print_r_graphic(labels.t_scale_value.get(), entries.get_N(), entries.get_radius(),
                                                              entries.get_c(), entries.get_alpha(), entries.get_k(),
                                                              entries.get_L(), graphics_r_frame))
#    but_calculate.bind("<Button-1>", graphics.print_t_graphic(entries.get_radius(), entries.get_N(), entries.get_time(),
#                                                              entries.get_c(), entries.get_alpha(), entries.get_k(),
#                                                              entries.get_L(), graphics_t_frame))

# def print_graph(event):
#    graphics.print_r_graphic(entries.get_time(), entries.get_N(), entries.get_radius(),
#                    entries.get_c(), entries.get_alpha(), entries.get_k(),
#                    entries.get_L(), root)
