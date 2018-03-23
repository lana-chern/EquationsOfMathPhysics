from tkinter import *
from gui import labels
from gui.graphics import MyGraphics

radius_entry = Entry()
t_entry = Entry()
q_entry = Entry()
c_entry = Entry()
alpha_entry = Entry()
L_entry = Entry()
N_entry = Entry()
epsilon_entry = Entry()
I_entry = Entry()
K_entry = Entry()

radius = StringVar()
t = StringVar()
q = StringVar()
c = StringVar()
alpha = StringVar()
L = StringVar()
N = StringVar()
epsilon = StringVar()
I = StringVar()
K = StringVar()

K.set("100")
I.set("100")


def get_radius():
    return float(radius.get())


def get_time():
    return float(t.get())


def get_q():
    return float(q.get())


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


def get_K():
    return int(K.get())


def get_I():
    return int(I.get())


def init_data_entries(initial_data_frame, graphics_r_frame, graphics_t_frame, graphic):
    q_entry = Entry(initial_data_frame, textvariable=q, width=10)
    c_entry = Entry(initial_data_frame, textvariable=c, width=10)
    alpha_entry = Entry(initial_data_frame, textvariable=alpha, width=10)
    radius_entry = Entry(initial_data_frame, textvariable=radius, width=10)
    L_entry = Entry(initial_data_frame, textvariable=L, width=10)
    t_entry = Entry(initial_data_frame, textvariable=t, width=10)

    q_entry.grid(row=1, column=1)
    c_entry.grid(row=2, column=1)
    alpha_entry.grid(row=3, column=1)
    radius_entry.grid(row=4, column=1)
    L_entry.grid(row=5, column=1)
    t_entry.grid(row=6, column=1)

    q.set("0.59")
    c.set("1.65")
    alpha.set("0.006")
    radius.set("6")
    L.set("0.3")
    t.set("15")

    data = [graphics_r_frame, graphics_t_frame, graphic]
    radius_entry.bind("<FocusOut>",
                      lambda event, arg=data: labels.draw_scale_r(event, arg, graphics_r_frame, graphics_t_frame))
    t_entry.bind("<FocusOut>",
                 lambda event, arg=data: labels.draw_scale_t(event, arg, graphics_r_frame, graphics_t_frame))


def init_fourier_entries(fourier_series_frame):
    N_entry = Entry(fourier_series_frame, textvariable=N, width=10)
    epsilon_entry = Entry(fourier_series_frame, textvariable=epsilon, width=10)
    N_entry.grid(row=8, column=1)
    epsilon_entry.grid(row=9, column=1)

    N.set("1000")
    epsilon.set("0")


def init_numerically_entries(numerically_frame, graphics_r_frame, graphics_t_frame):
    K_entry = Entry(numerically_frame, textvariable=K, width=10)
    I_entry = Entry(numerically_frame, textvariable=I, width=10)
    K_entry.grid(row=1, column=1)
    I_entry.grid(row=2, column=1)

    data = [graphics_r_frame, graphics_t_frame]
    # K_entry.bind("<FocusOut>",
    #                  lambda event, arg=data: labels.draw_scale_t(event, arg, graphics_r_frame, graphics_t_frame))
    # I_entry.bind("<FocusOut>",
    #                  lambda event, arg=data: labels.draw_scale_r(event, arg, graphics_r_frame, graphics_t_frame))
