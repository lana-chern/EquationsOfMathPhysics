from gui import entries
from tkinter import *

r_scale_value = DoubleVar()
t_scale_value = DoubleVar()


def init_data_labels(initial_data_frame):
    k_label = Label(initial_data_frame, text="k")
    c_label = Label(initial_data_frame, text="c")
    alpha_label = Label(initial_data_frame, text="α")
    radius_label = Label(initial_data_frame, text="R")
    L_label = Label(initial_data_frame, text="l")
    t_label = Label(initial_data_frame, text="T")
    initial_data_lab = Label(initial_data_frame, text="Начальные данные:")

    k_label.grid(row=1, column=0, padx=5, pady=3)
    c_label.grid(row=2, column=0, padx=5, pady=3)
    alpha_label.grid(row=3, column=0, padx=5, pady=3)
    radius_label.grid(row=4, column=0, padx=5, pady=3)
    L_label.grid(row=5, column=0, padx=5, pady=3)
    t_label.grid(row=6, column=0, padx=5, pady=3)
    initial_data_lab.grid(row=0, column=0, columnspan=2, padx=5, pady=3, sticky="w")
    entries.init_data_entries(initial_data_frame)


def init_fourier_labels(fourier_series_frame):
    N_label = Label(fourier_series_frame, text="N")
    epsilon_label = Label(fourier_series_frame, text="ε")
    fourier_series_label = Label(fourier_series_frame, text="Оценка ряда Фурье:")

    fourier_series_label.grid(row=7, column=0, columnspan=2, padx=5, pady=3, sticky="w")
    N_label.grid(row=8, column=0, padx=5, pady=3)
    epsilon_label.grid(row=9, column=0, padx=5, pady=3)
    entries.init_fourier_entries(fourier_series_frame)


def init_graphic_labels(graphics_r_frame, graphics_t_frame, radius, time):
    graphics1_label = Label(graphics_r_frame, text="График распределения температуры при фиксированном r:")
    r_scale = Scale(graphics_r_frame, length=300, orient=HORIZONTAL, variable=r_scale_value, from_=0,
                    to=radius,
                    tickinterval=float(entries.get_radius()),
                    resolution=0.1)

    graphics2_label = Label(graphics_t_frame, text="График распределения температуры при фиксированном t:")
    t_scale = Scale(graphics_t_frame, length=300, orient=HORIZONTAL, variable=t_scale_value, from_=0,
                    to=time,
                    tickinterval=float(entries.get_time()),
                    resolution=0.05)


    graphics1_label.grid(row=0, column=0, padx=5, pady=3)
    r_scale.grid(row=3, column=0, padx=5, pady=3)

    graphics2_label.grid(row=0, column=0, padx=5, pady=3)
    t_scale.grid(row=2, column=0, padx=5, pady=3)
