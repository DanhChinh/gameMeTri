import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip
from modules import read_data_from_json, get_time

def sayHello(time):
    if time<10:
        return "sáng"
    if time<13:
        return "trưa"
    if time<18:
        return "chiều"
    return "tối"
def create_layout_1(container):
    def handle_click_btn(btn, value, label1):
        pyperclip.copy(value)
        label1.config(text=value)
        # btn_old = btn_new
        # btn_new = btn
        # if btn_old:
        #     st = btn_old.cget('bootstyle')
        #     print(st)
    btns_json = read_data_from_json("./btn.json")
    frame1 = ttk.Frame(container)
    frame11 = ttk.Frame(frame1)
    frame12 = ttk.Frame(frame1)
    frame11.pack(side=TOP)
    frame12.pack(side=TOP)
    time = int(get_time("hour"))
    text = f"Chào buổi {sayHello(time)}"
    label1 = ttk.Label(frame11, text=text, font=("Helvetica", 18),bootstyle="success",width=20)
    label1.pack()
    counter = 0
    # btn_old = ttk.Button()
    # btn_new = ttk.Button()
    for btn in btns_json:
        row = counter//4
        column = counter%4
        counter+=1
        name = btn['name']
        value = btn['value']
        style = btn['style']
        btn = ttk.Button(
            frame12, 
            text = name, 
            command = lambda value=value, label1=label1: handle_click_btn(btn, value, label1),
            bootstyle = style,
            width = 8
            )
        btn.grid(row=row, column=column,padx=1,pady=2)
    return frame1
