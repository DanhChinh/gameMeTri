from tkinter import Tk, Toplevel, Entry, StringVar, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from modules import read_data_from_json,get_time,get_total,write_data_to_json



def create_layout_2(container, path):

    def update_table(data):
        tree.delete(*tree.get_children())
        len_ = len(data)
        counter =0
        for item in data:
            tree.insert("", "end", values=(len_-counter,item["time"], item["name"], item["content"], item["total"]))
            counter+=1

    def edit_item(event):
        selected_item = tree.selection()
        if not selected_item:
            # messagebox.showwarning("[Lỗi] Sửa thông tin", "Chưa có lựa chọn")
            return

        selected_item = selected_item[0]
        values = tree.item(selected_item, "values")
        
        edit_window = ttk.Toplevel(container)
        edit_window.attributes("-topmost",True)
        edit_window.geometry("300x150")
        edit_window.geometry(f'{300}x{130}+{800}+{460}')
        edit_window.resizable(False, False)
        edit_window.title("Sửa thông tin")
        edit_window.grab_set()
        edit_window.protocol("WM_DELETE_WINDOW", edit_window.destroy)
        frame_info = ttk.Frame(edit_window)
        frame_btn = ttk.Frame(edit_window)
        frame_info.pack(side=TOP)
        frame_btn.pack(side=TOP)
        ttk.Label(frame_info, text="Tên").grid(row=0, column=0)
        ttk.Label(frame_info, text="Nội dung").grid(row=1, column=0)
        
        time_var = get_time()
        name_var = StringVar(frame_info, value=values[2])
        content_var = StringVar(frame_info, value=values[3])
        
        name_entry = ttk.Entry(frame_info, textvariable=name_var, width=37)
        name_entry.grid(row=0, column=1)
        content_entry = ttk.Entry(frame_info, textvariable=content_var,  width=37)
        content_entry.grid(row=1, column=1)
        content_entry.focus_set()
        content_entry.icursor('end')
        
        def save_changes():
            item_index = tree.index(selected_item)
            data[item_index] = {"time": time_var, "name": name_var.get(), "content": content_var.get(),"total":get_total(content_var.get())}
            update_table(data)
            write_data_to_json(path, data)
            edit_window.destroy()
        def delete_item():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Xóa ghi chú", "Chưa lựa chọn ghi chú muốn xóa")
                messagebox.grab_set()
                return
            
            for item in selected_item:
                item_index = tree.index(item)
                item_values = data[item_index]["name"]
                confirm = messagebox.askyesno("Xóa ghi chú", f"Bạn có muốn xóa: {item_values}?")
                if confirm:
                    del data[item_index]
                    update_table(data)
                    write_data_to_json(path, data)
                edit_window.destroy()
        
        save_button = ttk.Button(frame_btn, text="Lưu", command=save_changes, bootstyle='info')
        save_button.grid(row=0, columnspan=2, pady=10, column=1, padx=5)
        delete_button = ttk.Button(frame_btn, text="Xóa", command=delete_item,bootstyle='danger')
        delete_button.grid(row=0, columnspan=2, pady=10, column=3)


    def handle_addbtn():
        name = inputName.get()
        content = inputContent.get()
        if not name or not content:
            messagebox.showerror("Thông báo", "Vui lòng nhập đầy đủ tên và nội dung")
            return
        new_item = {
            "name": name, 
            "time":get_time(),
            "content": content,
            "total": get_total(content)
            }
        data.insert(0,new_item)
        update_table(data)
        write_data_to_json(path, data)
        inputName.delete(0, 'end')
        inputContent.delete(0, 'end')
    data = read_data_from_json(path)
    frame = ttk.Frame(container)
    frameControl = ttk.Frame(frame,padding=3)
    frameTable = ttk.Frame(frame, padding=5)

    
    frameControl.pack(side=TOP)
    frameTable.pack(side=TOP)

    # ttk.Label(frameControl, text="Tên", bootstyle="default").pack(side=LEFT)
    inputName = ttk.Entry(frameControl,bootstyle = 'info')
    inputName.pack(side=LEFT)

    # ttk.Label(frameControl, text="Nội dung", bootstyle="default").pack(side=LEFT)
    inputContent = ttk.Entry(frameControl,bootstyle = 'info')
    inputContent.pack(side=LEFT)


    addButton = ttk.Button(frameControl, bootstyle = 'danger', text = "Thêm", command = handle_addbtn)
    addButton.pack(side=LEFT, padx=5)



    # Tạo bảng Treeview
    tree = ttk.Treeview(frameTable, columns=("Id","Time", "Name", "Content","Total"), show='headings',height=10)
    tree.pack(fill="both", expand=True)

    # Định nghĩa các cột
    tree.heading("Id", text="#",anchor="e")
    tree.heading("Time", text="Thời gian",anchor="e")
    tree.heading("Name", text="Tên", anchor="w")
    tree.heading("Content", text="Nội dung",anchor="w")
    tree.heading("Total", text="Tổng",anchor="e")

    tree.column("Id", anchor="e", width=10)
    tree.column("Time", anchor="e", width=70)
    tree.column("Name", anchor="w", width=70)
    tree.column("Content", anchor="w", width=130)
    tree.column("Total", anchor="e", width=60)
    tree.bind("<Double-1>", edit_item)
    # Cập nhật bảng với dữ liệu từ file JSON
    update_table(data)

    # Tạo các nút Edit và Delete
    # frameButton = ttk.Frame(frame2, padding=10)
    # frameButton.pack(fill="x")

    # delete_button = ttk.Button(frameDelete, text="Xóa", command=delete_item, bootstyle='danger')
    # delete_button.pack( padx=5)

    # edit_button = ttk.Button(frameDelete, text="Sửa", command=edit_item, bootstyle='warning')
    # edit_button.pack( padx=5)
    return frame