from tkinter import *

radius_entry = Entry()
radius_entry.insert(0, "12")
t_entry = Entry()
t_entry.insert(0, "15")


def get_radius():
    return radius_entry.get()


def get_time():
    return t_entry.get()


def init_data_entries(initial_data_frame):
    k_entry = Entry(initial_data_frame, width=10)
    c_entry = Entry(initial_data_frame, width=10)
    alpha_entry = Entry(initial_data_frame, width=10)
    radius_entry = Entry(initial_data_frame, width=10)
    L_entry = Entry(initial_data_frame, width=10)
    t_entry = Entry(initial_data_frame, width=10)

    k_entry.grid(row=1, column=1)
    c_entry.grid(row=2, column=1)
    alpha_entry.grid(row=3, column=1)
    radius_entry.grid(row=4, column=1)
    L_entry.grid(row=5, column=1)
    t_entry.grid(row=6, column=1)

    k_entry.insert(0, "0.59")
    c_entry.insert(0, "1.65")
    alpha_entry.insert(0, "0.006")
    radius_entry.insert(0, "12")
    L_entry.insert(0, "0.3")
    t_entry.insert(0, "15")


def init_fourier_entries(fourier_series_frame):
    N_entry = Entry(fourier_series_frame, width=10)
    epsilon_entry = Entry(fourier_series_frame, width=10)
    N_entry.grid(row=8, column=1)
    epsilon_entry.grid(row=9, column=1)
