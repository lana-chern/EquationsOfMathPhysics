from gui import gui
from gui import frames as frame
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title("Course Work")
    root.resizable(False, False)
    frames = frame.init_frames(root)
    buttons = frame.init_buttons(root)
    app = gui.Application(root, frames)

    # app.set_frames(frames)
    app.mainloop()
