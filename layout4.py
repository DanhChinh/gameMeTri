import ttkbootstrap as ttk
import tkinter as tk
from baoCaoV2 import showMess


def create_layout_4(container):
    def onClick():
        text =  showMess()
        label.config(text = text)
    arr = [i for i in range(100)]
    frame = ttk.Frame(container)
    label = ttk.Label(frame, bootstyle='dark', font = ("Arial",10))
    label.pack(pady = 10)
    button = ttk.Button(frame,bootstyle='success', text = "Pictures/a.pdf", command=onClick)
    button.pack()
    return frame
    