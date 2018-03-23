from gui import entries, frames
from tkinter import *

r_scale_value = DoubleVar()
t_scale_value = DoubleVar()


def init_data_labels(initial_data_frame, graphics_r_frame, graphics_t_frame, graphic):
    q_label = Label(initial_data_frame, text="q")
    c_label = Label(initial_data_frame, text="c")
    alpha_label = Label(initial_data_frame, text="α")
    radius_label = Label(initial_data_frame, text="R")
    L_label = Label(initial_data_frame, text="L")
    t_label = Label(initial_data_frame, text="T")
    initial_data_lab = Label(initial_data_frame, text="Начальные данные:")

    q_label.grid(row=1, column=0, padx=5, pady=3)
    c_label.grid(row=2, column=0, padx=5, pady=3)
    alpha_label.grid(row=3, column=0, padx=5, pady=3)
    radius_label.grid(row=4, column=0, padx=5, pady=3)
    L_label.grid(row=5, column=0, padx=5, pady=3)
    t_label.grid(row=6, column=0, padx=5, pady=3)
    initial_data_lab.grid(row=0, column=0, columnspan=2, padx=5, pady=3, sticky="w")
    entries.init_data_entries(initial_data_frame, graphics_r_frame, graphics_t_frame, graphic)


def init_fourier_labels(fourier_series_frame):
    N_label = Label(fourier_series_frame, text="N")
    epsilon_label = Label(fourier_series_frame, text="ε")
    fourier_series_label = Label(fourier_series_frame, text="Оценка ряда Фурье:")

    fourier_series_label.grid(row=7, column=0, columnspan=2, padx=5, pady=3, sticky="w")
    N_label.grid(row=8, column=0, padx=5, pady=3)
    epsilon_label.grid(row=9, column=0, padx=5, pady=3)
    entries.init_fourier_entries(fourier_series_frame)


def init_numerically_frame(numerically_frame, graphics_r_frame, graphics_t_frame):
    K_Label = Label(numerically_frame, text="K")
    I_Label = Label(numerically_frame, text="I")
    numerically_label = Label(numerically_frame, text='Параметры сетки:')

    numerically_label.grid(row=0, column=0, columnspan=2, padx=5, pady=3, sticky="w")
    K_Label.grid(row=1, column=0, padx=5, pady=3)
    I_Label.grid(row=2, column=0, padx=5, pady=3)
    entries.init_numerically_entries(numerically_frame, graphics_r_frame, graphics_t_frame)


def init_graphic_labels(graphics_r_frame, graphics_t_frame, radius, time, hr, ht):
    graphics1_label = Label(graphics_r_frame, text="График распределения температуры при фиксированном r:")
    r_scale = Scale(graphics_r_frame, length=300, orient=HORIZONTAL, variable=r_scale_value, from_=0,
                    to=radius,
                    tickinterval=float(entries.get_radius()),
                    resolution=hr)

    graphics2_label = Label(graphics_t_frame, text="График распределения температуры при фиксированном t:")
    t_scale = Scale(graphics_t_frame, length=300, orient=HORIZONTAL, variable=t_scale_value, from_=0,
                    to=time,
                    tickinterval=float(entries.get_time()),
                    resolution=ht)
    graphics1_label.grid(row=0, column=0, padx=5, pady=3)
    r_scale.grid(row=3, column=0, padx=5, pady=3)
    graphics2_label.grid(row=0, column=0, padx=5, pady=3)
    t_scale.grid(row=2, column=0, padx=5, pady=3)


def draw_scale_r(event, arg, graphics_r_frame, graphics_t_frame):
    hr = entries.get_radius()/entries.get_I()
    ht = entries.get_time()/entries.get_K()
    list = graphics_r_frame.grid_slaves()
    for l in list:
        l.destroy()
    init_graphic_labels(graphics_r_frame, graphics_t_frame, float(entries.get_radius()), float(entries.get_time()), hr, ht)
    frames.print_graph(event, arg)


def draw_scale_t(event, arg, graphics_r_frame, graphics_t_frame):
    hr = entries.get_radius() / entries.get_I()
    ht = entries.get_time() / entries.get_K()
    list = graphics_t_frame.grid_slaves()
    for l in list:
        l.destroy()
    init_graphic_labels(graphics_r_frame, graphics_t_frame, float(entries.get_radius()), float(entries.get_time()), hr, ht)
    frames.print_graph(event, arg)
