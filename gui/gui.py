from tkinter import *
import gui.labels as labels
import gui.frames as frames
import gui.entries as entries


class Application(Frame):
    initial_data_frame = None
    fourier_series_frame = None
    graphics_r_frame = None
    graphics_t_frame = None

    def set_frames(self, frames):
        self.initial_data_frame = frames[0]
        self.fourier_series_frame = frames[1]
        self.graphics_r_frame = frames[2]
        self.graphics_t_frame = frames[3]

    def __init__(self):
        super().__init__()
        self.set_frames(frames.init_frames(self.master))
        labels.init_data_labels(self.initial_data_frame)
        labels.init_fourier_labels(self.fourier_series_frame)
        labels.init_graphic_labels(self.graphics_t_frame, self.graphics_r_frame)

