import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from layout1 import create_layout_1
from layout2 import create_layout_2
from layout4 import create_layout_4
from modules import get_time


# Tạo cửa sổ chính
root = ttk.Window( themename = "yeti")
root.title(f"[{get_time('1')}] Game Mễ Trì")
root.attributes('-topmost', True)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)




notebook = ttk.Notebook(root,bootstyle="dark")

# Tạo các frame cho từng giao diện
frame1 = create_layout_1(notebook)
frame2 = create_layout_2(notebook, './data.json')
frame3 = create_layout_2(notebook,'data2.json' )
frame4 = create_layout_4(notebook)

notebook.add(frame1, text="Công cụ")
notebook.add(frame2, text="Ghi chú sáng")
notebook.add(frame3, text="Ghi chú đêm")
notebook.add(frame4, text="Khuyến mãi")
notebook.pack(expand=True, fill='both')


# Chạy ứng dụng
root.mainloop()