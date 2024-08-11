import tkinter as tk
import tkinter.font as tkFont

# Dữ liệu font
font_data = [
    {"name": "Arial", "size": 12},
    {"name": "Courier", "size": 14},
    {"name": "Times New Roman", "size": 16}
]

def apply_font(font_name, font_size):
    """Cập nhật font cho tất cả các widget trong cửa sổ chính."""
    custom_font = tkFont.Font(family=font_name, size=font_size)
    # Áp dụng font cho tất cả các widget
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.config(font=custom_font)

def on_font_change():
    """Xử lý sự kiện khi người dùng chọn một radio button."""
    selected_font = font_var.get()
    font_name, font_size = selected_font.split(',')
    apply_font(font_name, int(font_size))

def main():
    global root, font_var

    # Khởi tạo cửa sổ chính
    root = tk.Tk()
    root.title("Font Selector")

    # Tạo biến để lưu font đã chọn
    font_var = tk.StringVar(value="Arial,12")

    # Tạo các radio button cho các font
    for font in font_data:
        font_str = f"{font['name']},{font['size']}"
        radio_button = tk.Radiobutton(
            root,
            text=f"{font['name']} {font['size']}",
            variable=font_var,
            value=font_str,
            command=on_font_change
        )
        radio_button.pack(padx=10, pady=5)
    
    # Tạo các widget để kiểm tra font
    label = tk.Label(root, text="This is a label with default font.")
    label.pack(padx=20, pady=20)

    button = tk.Button(root, text="This is a button with default font.")
    button.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
