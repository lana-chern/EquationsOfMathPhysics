from tkinter import *
import gui.labels as labels
import gui.frames as frames
import gui.entries as entries
from gui.graphics import MyGraphics


class Application(Frame):
    initial_data_frame = None
    fourier_series_frame = None
    numerically_frame = None
    graphics_r_frame = None
    graphics_t_frame = None
    graphic = None

    def set_frames(self, frames, graphic):
        self.initial_data_frame = frames[0]
        self.fourier_series_frame = frames[1]
        self.numerically_frame = frames[2]
        self.graphics_r_frame = frames[3]
        self.graphics_t_frame = frames[4]
        self.graphic = graphic

    def __init__(self):
        super().__init__()
        graphic = MyGraphics([0, 0])
        self.set_frames(frames.init_frames(self.master), graphic)
        labels.init_data_labels(self.initial_data_frame, self.graphics_r_frame, self.graphics_t_frame, self.graphic)
        labels.init_fourier_labels(self.fourier_series_frame)
        labels.init_numerically_frame(self.numerically_frame, self.graphics_r_frame, self.graphics_t_frame)
        hr = entries.get_radius() / entries.get_I()
        ht = entries.get_time() / entries.get_K()
        labels.init_graphic_labels(self.graphics_r_frame, self.graphics_t_frame, entries.get_radius(),
                                   entries.get_time(), hr, ht)
        frames.init_buttons(self.master, self.graphics_r_frame, self.graphics_t_frame, self.graphic)
