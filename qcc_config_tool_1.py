# -*- coding: UTF-8 -*-
import subprocess

import os
import operator as op


from tkinter import *
from tkinter.messagebox import *

from enum import Enum

write_list = []
count_dut = 0
test_success = 0
test_failed = 0
process_status = False


class Eugene_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

        self.status_value      = IntVar()
        self.latest_ver        = StringVar()
        self.current_ver       = StringVar()
        self.firmware_ver      = StringVar()
        self.bluetooth_name    = StringVar() 
        self.bluetooth_address = StringVar()
        self.final_result  = StringVar()
        self.count         = StringVar()
        self.count_success = StringVar()
        self.count_faied   = StringVar()

        self.status_value.  set("0")
        self.latest_ver.    set("")
        self.current_ver.   set("")
        self.firmware_ver.  set("")
        self.bluetooth_name.set("")
        self.bluetooth_address.set("")
        self.final_result. set("")
        self.count.        set("0")
        self.count_success.set("0")
        self.count_faied.  set("0")

    def cmd(self, command):
        global process_status
        subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        subp.wait(2)
        if subp.poll() == 0:
            #print(subp.communicate()[1])
            process_status = True
        else:
            process_status = False

    def QccReadConfigCmd(self):
        global process_status
        global count_dut
        write_list = []
        self.final_result.set("")
        read_qcc_command = r".\ConfigCmd.exe dev2txt qcc_configure.txt -usbdbg 1 -database hyd.sdb -system QCC512X_CONFIG"
        self.cmd(read_qcc_command)

    def WindowConfigure(self, w, h):
        self.init_window_name.title(" Qualcomm Verson Check Tool V1.0.0")
        ws = self.init_window_name.winfo_screenwidth()
        hs = self.init_window_name.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.init_window_name.geometry("%dx%d+%d+%d" % (w, h, x, y))
        #self.init_window_name.configure(bg="black")
        self.init_window_name.attributes("-alpha",1) #虚化
        self.init_window_name.resizable(False, False)

        label_x = 1
        label_y = 1

        self.lat_ver_label = Label(self.init_window_name, text="  最新版本号  ", width = 15,height = 2, fg = "blue", font=("微软雅黑", "10", "bold"))
        self.cur_ver_label = Label(self.init_window_name, text="  当前版本号  ", width = 15,height = 2, fg = "coral", font=("微软雅黑", "10", "bold"))
        self.fw_ver_label  = Label(self.init_window_name, text="  固件版本    ", width = 15,height = 2, fg = "teal", font=("微软雅黑", "10", "bold"))
        self.bt_name_label = Label(self.init_window_name, text="  蓝牙名称    ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.bt_addr_label = Label(self.init_window_name, text="  蓝牙地址    ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.fin_res_label = Label(self.init_window_name, text="  对比结果    ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_a_label = Label(self.init_window_name, text="  当前检测总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_s_label = Label(self.init_window_name, text="  校对成功总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_f_label = Label(self.init_window_name, text="  校对失败总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))

        self.lat_ver_label.grid(row = label_x + 0, column = label_y + 0)
        self.cur_ver_label.grid(row = label_x + 1, column = label_y + 0)
        self.fw_ver_label.grid (row = label_x + 2, column = label_y + 0)
        self.bt_name_label.grid(row = label_x + 3, column = label_y + 0)
        self.bt_addr_label.grid(row = label_x + 4, column = label_y + 0)
        self.fin_res_label.grid(row = label_x + 5, column = label_y + 0)
        self.count_a_label.grid(row = label_x + 6, column = label_y + 0)
        self.count_s_label.grid(row = label_x + 6, column = label_y + 1)
        self.count_f_label.grid(row = label_x + 6, column = label_y + 2)

        

        entry_x = 1
        entry_y = 1

        self.lat_ver_entry  = Entry(self.init_window_name, textvariable = self.latest_ver,        width = 25)
        self.cur_ver_entry  = Entry(self.init_window_name, textvariable = self.current_ver,       width = 25)
        self.fw_ver_entry   = Entry(self.init_window_name, textvariable = self.firmware_ver,      width = 25)
        self.bt_name_entry  = Entry(self.init_window_name, textvariable = self.bluetooth_name,    width = 25)
        self.bt_addr_entry  = Entry(self.init_window_name, textvariable = self.bluetooth_address, width = 25)
        self.fin_res_entry  = Entry(self.init_window_name, textvariable = self.final_result, width=25, foreground = "red", state = "readonly")
        self.count_a_entry  = Entry(self.init_window_name, textvariable = self.count, width=6, font=("微软雅黑", "12", "bold"),state = "readonly")
        self.count_s_entry  = Entry(self.init_window_name, textvariable = self.count_success, width=6, font=("微软雅黑", "12", "bold"),state = "readonly", foreground = "blue")
        self.count_f_entry  = Entry(self.init_window_name, textvariable = self.count_faied, width=6, font=("微软雅黑", "12", "bold"),state = "readonly", foreground = "red")
        
        self.lat_ver_entry.grid(row = entry_x + 0, column = entry_y + 1)
        self.cur_ver_entry.grid(row = entry_x + 1, column = entry_y + 1)
        self.fw_ver_entry.grid (row = entry_x + 2, column = entry_y + 1)
        self.bt_name_entry.grid(row = entry_x + 3, column = entry_y + 1)
        self.bt_addr_entry.grid(row = entry_x + 4, column = entry_y + 1)
        self.fin_res_entry.grid(row = entry_x + 5, column = entry_y + 1)
        self.count_a_entry.grid(row = entry_x + 7, column = entry_y + 0)
        self.count_s_entry.grid(row = entry_x + 7, column = entry_y + 1)
        self.count_f_entry.grid(row = entry_x + 7, column = entry_y + 2)

        button_x = 1
        button_y = 1

        self.lock_button = Checkbutton(self.init_window_name, text = '锁定版本号',variable = self.status_value,command = self.Status_Entry)
        self.read_buttom = Button(self.init_window_name, text=" 进行读取 ", bg="lightblue", width=10)

        
        self.lock_button.grid(row = button_x + 0, column = button_y+2)
        self.read_buttom.grid(row = button_x + 1, column = button_y+2)
    
    def Status_Entry(self):
        if self.status_value.get() == True :
            Entry(self.init_window_name , textvariable=self.latest_ver, width=20, state="readonly"  ).grid(row=1, column=2)
        else :
            Entry(self.init_window_name , textvariable=self.latest_ver, width=20, state="normal"  ).grid(row=1, column=2)




def EugeneGUIStart():
    init_window = Tk()
    eugene_gui  = Eugene_GUI(init_window)
    eugene_gui.WindowConfigure(450, 350)

    init_window.mainloop()

EugeneGUIStart()