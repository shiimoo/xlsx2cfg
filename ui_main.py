"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""

import cfg

import random
from tkinter import *
from tkinter.ttk import *


"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_m4m4hijk = self.__tk_label_m4m4hijk(self)
        self.tk_select_box_select_cfg = self.__tk_select_box_select_cfg(self)
        self.tk_frame_m4m4me4q = self.__tk_frame_m4m4me4q(self)
        self.tk_label_m4m4qkun = self.__tk_label_m4m4qkun(self.tk_frame_m4m4me4q)
        self.tk_button_choose_src_path = self.__tk_button_choose_src_path(
            self.tk_frame_m4m4me4q
        )
        self.tk_label_src_path = self.__tk_label_src_path(self.tk_frame_m4m4me4q)
        self.tk_table_out_list = self.__tk_table_out_list(self.tk_frame_m4m4me4q)
        self.tk_label_m4s8b8pm = self.__tk_label_m4s8b8pm(self.tk_frame_m4m4me4q)
        self.tk_select_box_choose_code_type = self.__tk_select_box_choose_code_type(
            self.tk_frame_m4m4me4q
        )
        self.tk_label_m4s8cqjt = self.__tk_label_m4s8cqjt(self.tk_frame_m4m4me4q)
        self.tk_label_show_out_path = self.__tk_label_show_out_path(
            self.tk_frame_m4m4me4q
        )
        self.tk_button_choose_out_path = self.__tk_button_choose_out_path(
            self.tk_frame_m4m4me4q
        )
        self.tk_button_save_out = self.__tk_button_save_out(self.tk_frame_m4m4me4q)
        self.tk_label_m4m827cv = self.__tk_label_m4m827cv(self)
        self.tk_frame_m4m7rum7 = self.__tk_frame_m4m7rum7(self)
        self.tk_progressbar_out_progress = self.__tk_progressbar_out_progress(
            self.tk_frame_m4m7rum7
        )
        self.tk_table_out_log = self.__tk_table_out_log(self.tk_frame_m4m7rum7)

    def __win(self):
        self.title("xlsx2cfg")
        # 设置窗口大小、居中
        width = 500
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar:
                vbar.lift(widget)
            if hbar:
                hbar.lift(widget)

        def hide():
            if vbar:
                vbar.lower(widget)
            if hbar:
                hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Enter>", lambda e: show())
        if vbar:
            vbar.bind("<Leave>", lambda e: hide())
        if hbar:
            hbar.bind("<Enter>", lambda e: show())
        if hbar:
            hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor="ne")

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor="sw")

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_label_m4m4hijk(self, parent):
        label = Label(
            parent,
            text="配置选择 ：",
            anchor="center",
        )
        label.place(x=130, y=15, width=70, height=30)
        return label

    def __tk_select_box_select_cfg(self, parent):
        cb = Combobox(
            parent,
            state="readonly",
        )
        cb.place(x=220, y=15, width=150, height=30)
        return cb

    def __tk_frame_m4m4me4q(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=0, y=50, width=500, height=180)
        return frame

    def __tk_label_m4m4qkun(self, parent):
        label = Label(
            parent,
            text="xlsx路径：",
            anchor="center",
        )
        label.place(x=10, y=10, width=60, height=30)
        return label

    def __tk_button_choose_src_path(self, parent):
        btn = Button(
            parent,
            text="选择",
            takefocus=False,
        )
        btn.place(x=80, y=10, width=50, height=30)
        return btn

    def __tk_label_src_path(self, parent):
        label = Label(
            parent,
            text="...",
            anchor="center",
        )
        label.place(x=140, y=10, width=350, height=30)
        return label

    def __tk_table_out_list(self, parent):
        # 表头字段 表头宽度
        columns = {"导出类型": 95, "输出路径": 383}
        tk_table = Treeview(
            parent, show="headings", columns=list(columns), selectmode="browse"
        )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor="center")
            tk_table.column(
                text, anchor="center", width=width, stretch=False
            )  # stretch 不自动拉伸

        tk_table.place(x=10, y=95, width=480, height=80)
        self.create_bar(parent, tk_table, True, True, 10, 95, 480, 80, 500, 180)
        return tk_table

    def __tk_label_m4s8b8pm(self, parent):
        label = Label(
            parent,
            text="输出类型：",
            anchor="center",
        )
        label.place(x=10, y=55, width=70, height=30)
        return label

    def __tk_select_box_choose_code_type(self, parent):
        cb = Combobox(
            parent,
            state="readonly",
        )
        cb["values"] = ("列表框", "Python", "Tkinter Helper")
        cb.place(x=80, y=55, width=80, height=30)
        return cb

    def __tk_label_m4s8cqjt(self, parent):
        label = Label(
            parent,
            text="输出路径：",
            anchor="center",
        )
        label.place(x=180, y=55, width=70, height=30)
        return label

    def __tk_label_show_out_path(self, parent):
        label = Label(
            parent,
            text="",
            anchor="w",
        )
        label.place(x=250, y=55, width=80, height=30)
        return label

    def __tk_button_choose_out_path(self, parent):
        btn = Button(
            parent,
            text="choose",
            takefocus=False,
        )
        btn.place(x=330, y=55, width=60, height=30)
        return btn

    def __tk_button_save_out(self, parent):
        btn = Button(
            parent,
            text="添加",
            takefocus=False,
        )
        btn.place(x=420, y=55, width=50, height=30)
        return btn

    def __tk_label_m4m827cv(self, parent):
        label = Label(
            parent,
            text="数 据 导 出",
            anchor="center",
        )
        label.place(x=210, y=235, width=80, height=30)
        return label

    def __tk_frame_m4m7rum7(self, parent):
        frame = Frame(
            parent,
        )
        frame.place(x=0, y=270, width=500, height=320)
        return frame

    def __tk_progressbar_out_progress(self, parent):
        progressbar = Progressbar(
            parent,
            orient=HORIZONTAL,
        )
        progressbar.place(x=10, y=10, width=480, height=30)
        return progressbar

    def __tk_table_out_log(self, parent):
        # 表头字段 表头宽度
        columns = {"LV": 71, "msg": 407}
        tk_table = Treeview(
            parent,
            show="headings",
            columns=list(columns),
        )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor="center")
            tk_table.column(
                text, anchor="center", width=width, stretch=False
            )  # stretch 不自动拉伸

        tk_table.place(x=10, y=50, width=480, height=260)
        self.create_bar(parent, tk_table, False, True, 10, 50, 480, 260, 500, 320)
        return tk_table


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl: Controller = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_select_box_select_cfg.bind("<Button-1>", self.ctl.refresh_all_cfg)
        self.tk_select_box_select_cfg.bind("<<ComboboxSelected>>", self.ctl.select_cfg)
        self.tk_button_choose_src_path.bind("<Button-1>", self.ctl.choose_src_path)
        self.tk_table_out_list.bind("<<TreeviewSelect>>", self.ctl.edit_out)
        self.tk_select_box_choose_code_type.bind(
            "<Button-1>", self.ctl.refresh_code_type
        )
        self.tk_button_choose_out_path.bind("<Button-1>", self.ctl.choose_out_path)
        self.tk_button_save_out.bind("<Button-1>", self.ctl.add_out)
        pass

    def __style_config(self):
        pass

    def freeze(self):
        self.attributes("-disabled", 1)

    def free(self):
        self.attributes("-disabled", 0)


"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""


# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def refresh_all_cfg(self, evt):
        self.ui.tk_select_box_select_cfg["value"] = cfg.get_cfg_list()

    def select_cfg(self, evt):
        self.use_cfg(self.ui.tk_select_box_select_cfg.get())

    def choose_src_path(self, evt):
        self.ui.freeze()
        from tkinter import filedialog

        folder_selected = filedialog.askdirectory()
        self.ui.free()
        # 如果用户选择了文件夹，则打印路径
        if folder_selected:
            self.ui.tk_label_src_path.config(text=folder_selected)

    def edit_out(self, evt):
        select_info = self.ui.tk_table_out_list.selection()
        btn_text = ""
        code_type = ""
        out_path = ""
        if len(select_info) <= 0:
            btn_text = "新增"
        else:
            btn_text = "保存"
            item_id = select_info[0]
            vals = self.ui.tk_table_out_list.item(item_id, "values")
            code_type, out_path = vals[0], vals[1]
        self.ui.tk_button_save_out.config(text=btn_text)
        self.ui.tk_select_box_choose_code_type.set(code_type)
        self.ui.tk_label_show_out_path.config(text=out_path)

    def use_cfg(self, name: str):
        cfg_data = cfg.load_cfg(name)
        if cfg_data == None:
            return
        self.ui.tk_label_src_path.config(text=cfg_data["src_path"])
        out_list = self.ui.tk_table_out_list
        for item in out_list.get_children():
            out_list.delete(item)
        for out_info in cfg_data["out_list"]:
            out_list.insert(
                "", "end", values=(out_info["code_type"], out_info["out_path"])
            )

    def refresh_code_type(self, evt):
        self.ui.tk_select_box_choose_code_type["values"] = cfg.get_code_type_list()

    def choose_out_path(self, evt):
        self.ui.freeze()
        from tkinter import filedialog

        folder_selected = filedialog.askdirectory()
        self.ui.free()
        # 如果用户选择了文件夹，则打印路径
        if folder_selected:
            self.ui.tk_label_show_out_path.config(text=folder_selected)

    def add_out(self, evt):
        text = self.ui.tk_button_save_out.cget("text").strip()
        if text == "保存":
            pass
        elif text == "添加":
            out_list = self.ui.tk_table_out_list
            code_type = self.ui.tk_select_box_choose_code_type.get()
            out_path = self.ui.tk_label_show_out_path.cget("text")
            for item in out_list.get_children():
                vals = out_list.item(item)["values"]
                if code_type == vals[0] and out_path == vals[1]:
                    return
            out_list.insert(
                "",
                "end",
                values=(
                    code_type,
                    out_path,
                ),
            )


def open_ui():
    ctrl = Controller()
    win = Win(ctrl)
    ctrl.init(win)
    win.mainloop()


if __name__ == "__main__":
    open_ui()
