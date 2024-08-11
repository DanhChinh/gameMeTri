import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("ttkbootstrap Notebook with Custom Sizes")

# Tạo style với ttkbootstrap
style = Style(theme='cosmo')  # Chọn theme phù hợp

# Tạo Notebook
notebook = ttk.Notebook(root)

# Tạo các frame để đặt vào từng tab của Notebook với kích thước cụ thể
frame1 = ttk.Frame(notebook, width=300, height=200, padding="10", relief="sunken")
frame2 = ttk.Frame(notebook, width=400, height=300, padding="10", relief="sunken")

# Thêm nội dung vào các frame
ttk.Label(frame1, text="This is the content of Tab 1\n" * 10).pack(pady=10, padx=10, fill='both', expand=True)
ttk.Label(frame2, text="This is the content of Tab 2\n" * 20).pack(pady=10, padx=10, fill='both', expand=True)

# Thêm các frame vào Notebook
notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")

# Đặt Notebook vào cửa sổ chính
notebook.pack(expand=True, fill='both')

# Đảm bảo kích thước của cửa sổ chính đủ lớn để chứa các tab
root.update_idletasks()  # Cập nhật tất cả các thay đổi giao diện

# Hiển thị cửa sổ
root.mainloop()
