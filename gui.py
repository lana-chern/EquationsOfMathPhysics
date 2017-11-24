from tkinter import *


def initial_data():
    # Inserting default values
    k_entry.insert(0, "0.59")
    c_entry.insert(0, "1.65")
    alpha_entry.insert(0, "0.006")
    radius_entry.insert(0, "12")
    L_entry.insert(0, "0.3")
    t_entry.insert(0, "15")

    N_entry.insert(0, "1000")
    # epsilon_entry.insert(0, "1000")


def calculate(event):
    123


root = Tk()
root.title("Course Work")
root.resizable(False, False)

initial_data_frame = Frame(root, bd=1)

# Initialization
initial_data_lab = Label(initial_data_frame, text="Начальные данные:")

k_label = Label(initial_data_frame, text="k")
c_label = Label(initial_data_frame, text="c")
alpha_label = Label(initial_data_frame, text="α")
radius_label = Label(initial_data_frame, text="R")
L_label = Label(initial_data_frame, text="l")
t_label = Label(initial_data_frame, text="T")

k_entry = Entry(initial_data_frame, width=10)
c_entry = Entry(initial_data_frame, width=10)
alpha_entry = Entry(initial_data_frame, width=10)
radius_entry = Entry(initial_data_frame, width=10)
L_entry = Entry(initial_data_frame, width=10)
t_entry = Entry(initial_data_frame, width=10)

fourier_series_frame = Frame(root, bd=1)

fourier_series_label = Label(fourier_series_frame, text="Оценка ряда Фурье:")
N_label = Label(fourier_series_frame, text="N")
epsilon_label = Label(fourier_series_frame, text="ε")

N_entry = Entry(fourier_series_frame, width=10)
epsilon_entry = Entry(fourier_series_frame, width=10)

but_calculate = Button(root, text="Построить графики")

initial_data()

graphycs_r_frame = Frame(root, bd=1)

graphycs1_label = Label(graphycs_r_frame, text="График распределения температуры при фиксированном r:")
fix_r_frame = Frame(graphycs_r_frame, bd=1)
r_scale = Scale(graphycs_r_frame, length=300, orient=HORIZONTAL, from_=0, to=float(radius_entry.get()), tickinterval=1,
                resolution=0.1)

graphycs_t_frame = Frame(root, bd=1)

graphycs2_label = Label(graphycs_t_frame, text="График распределения температуры при фиксированном t:")
fix_t_frame = Frame(graphycs_t_frame, bd=1)
t_scale = Scale(graphycs_t_frame, length=300, orient=HORIZONTAL, from_=0, to=float(t_entry.get()), tickinterval=5,
                resolution=0.5)

# Packer - its horrible
initial_data_frame.grid(row=0, column=0)
initial_data_lab.grid(row=0, column=0, columnspan=2, padx=5, pady=3, sticky="w")
k_label.grid(row=1, column=0, padx=5, pady=3)
c_label.grid(row=2, column=0, padx=5, pady=3)
alpha_label.grid(row=3, column=0, padx=5, pady=3)
radius_label.grid(row=4, column=0, padx=5, pady=3)
L_label.grid(row=5, column=0, padx=5, pady=3)
t_label.grid(row=6, column=0, padx=5, pady=3)

fourier_series_frame.grid(row=1, column=0)
fourier_series_label.grid(row=7, column=0, columnspan=2, padx=5, pady=3, sticky="w")
N_label.grid(row=8, column=0, padx=5, pady=3)
epsilon_label.grid(row=9, column=0, padx=5, pady=3)

but_calculate.grid(row=2, column=0, padx=5, pady=5)

graphycs_r_frame.grid(row=0, column=1, sticky="n")
graphycs1_label.grid(row=0, column=0, padx=5, pady=3)
fix_r_frame.grid(row=1, column=0, rowspan=7, padx=5, pady=3)
r_scale.grid(row=8, column=0, padx=5, pady=3)

graphycs_t_frame.grid(row=1, column=1, sticky="n")
graphycs2_label.grid(row=0, column=0, padx=5, pady=3)
fix_t_frame.grid(row=1, column=0, rowspan=7, padx=5, pady=3)
t_scale.grid(row=2, column=0, padx=5, pady=3)

k_entry.grid(row=1, column=1)
c_entry.grid(row=2, column=1)
alpha_entry.grid(row=3, column=1)
radius_entry.grid(row=4, column=1)
L_entry.grid(row=5, column=1)
t_entry.grid(row=6, column=1)
N_entry.grid(row=8, column=1)
epsilon_entry.grid(row=9, column=1)

root.mainloop()
