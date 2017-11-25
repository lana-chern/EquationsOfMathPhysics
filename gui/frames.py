from tkinter import *
from gui import graphics
from gui import entries


def init_frames(root):
    initial_data_frame = Frame(root, bd=1)
    fourier_series_frame = Frame(root, bd=1)
    graphics_r_frame = Frame(root, bd=1)
    graphics_t_frame = Frame(root, bd=1)

    initial_data_frame.grid(row=0, column=0)
    fourier_series_frame.grid(row=1, column=0)
    graphics_r_frame.grid(row=0, column=1, sticky="n")
    graphics_t_frame.grid(row=1, column=1, sticky="n")
    return [initial_data_frame, fourier_series_frame, graphics_r_frame, graphics_t_frame]


def init_buttons(root):
    but_calculate = Button(root, text="Построить графики")
    but_calculate.grid(row=2, column=0, padx=5, pady=5)
    but_calculate.event(graphics.print_r_graphic())  #TODO add event on mouse click


event:
    graphics.print_r_graphic(entries.get_time(), entries.get_alpha(), .........)