from tkinter import Tk, Frame, Label, Button

import subprocess
import platform

system = platform.system()
if system == 'OpenBSD':
    fortune = '/usr/games/fortune'
else:
    fortune = 'fortune'

def get_fortune():
    process = subprocess.Popen([fortune], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output

window = Tk()
frame = Frame(window)
frame.pack(expand=True)

label = Label(frame, text=get_fortune())
label.pack()
def set_fortune():
    label.config(text=get_fortune())

button = Button(frame, text="Get Fortune", command=set_fortune)
button.pack()

window.mainloop()
