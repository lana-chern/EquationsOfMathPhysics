from tkinter import *

radius_entry = Entry()
t_entry = Entry()
k_entry = Entry()
c_entry = Entry()
alpha_entry = Entry()
L_entry = Entry()
N_entry = Entry()
epsilon_entry = Entry()

radius = StringVar()
t = StringVar()
k = StringVar()
c = StringVar()
alpha = StringVar()
L = StringVar()
N = StringVar()
epsilon = StringVar()


def get_radius():
    return float(radius.get())


def get_time():
    return float(t.get())


def get_k():
    return float(k.get())


def get_alpha():
    return float(alpha.get())


def get_L():
    return float(L.get())


def get_N():
    return int(N.get())


def get_epsilon():
    return float(epsilon.get())


def get_c():
    return float(c.get())


def init_data_entries(initial_data_frame):
    k_entry = Entry(initial_data_frame, textvariable=k, width=10)
    c_entry = Entry(initial_data_frame, textvariable=c, width=10)
    alpha_entry = Entry(initial_data_frame, textvariable=alpha, width=10)
    radius_entry = Entry(initial_data_frame, textvariable=radius, width=10)
    L_entry = Entry(initial_data_frame, textvariable=L, width=10)
    t_entry = Entry(initial_data_frame, textvariable=t, width=10)

    k_entry.grid(row=1, column=1)
    c_entry.grid(row=2, column=1)
    alpha_entry.grid(row=3, column=1)
    radius_entry.grid(row=4, column=1)
    L_entry.grid(row=5, column=1)
    t_entry.grid(row=6, column=1)

    k.set("0.59")
    c.set("1.65")
    alpha.set("0.006")
    radius.set("12")
    L.set("0.3")
    t.set("15")


def init_fourier_entries(fourier_series_frame):
    N_entry = Entry(fourier_series_frame, textvariable=N, width=10)
    epsilon_entry = Entry(fourier_series_frame, textvariable=epsilon, width=10)
    N_entry.grid(row=8, column=1)
    epsilon_entry.grid(row=9, column=1)

    N.set("1000")
