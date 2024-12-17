import tkinter as tk
from tkinter import filedialog
 
def select_folder():
    # 创建一个Tkinter窗口
    root = tk.Tk()
    # 隐藏根窗口，只显示对话框
    # root.withdraw()
 
    # 打开文件夹选择对话框，并获取选择的文件夹路径
    folder_selected = filedialog.askdirectory()
 
    # 如果用户选择了文件夹，则打印路径
    if folder_selected:
        print("Selected folder:", folder_selected)
 
    # 结束程序
    root.destroy()
 
# 调用函数
select_folder()