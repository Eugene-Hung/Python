# -*- coding: UTF-8 -*-
import subprocess
import ctypes
import os
import operator as op


from tkinter import *
from tkinter.messagebox import *

from enum import Enum

write_list     = []
count_dut      = 0
test_success   = 0
test_failed    = 0
process_status = False


class Eugene_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

        self.state_val   = IntVar()
        self.latest_ver  = StringVar()
        self.current_ver = StringVar()
        self.fw_vers  = StringVar()
        self.bt_name  = StringVar() 
        self.bt_addr  = StringVar()
        self.fin_resl = StringVar()
        self.all_val  = StringVar()
        self.succ_val = StringVar()
        self.fail_val = StringVar()

        self.state_val.  set("0")
        self.latest_ver. set("")
        self.current_ver.set("")
        self.fw_vers. set("")
        self.bt_name. set("")
        self.bt_addr. set("")
        self.fin_resl.set("")
        self.all_val. set("0")
        self.succ_val.set("0")
        self.fail_val.set("0")

    def cmd(self, command):
        global process_status

        subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        subp.wait(2)
        if subp.poll() == 0:
            #print(subp.communicate()[1])
            process_status = True
        else:
            process_status = False
        


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
        self.fin_resl_label = Label(self.init_window_name, text="  对比结果    ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_a_label = Label(self.init_window_name, text="  当前检测总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_s_label = Label(self.init_window_name, text="  校对成功总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))
        self.count_f_label = Label(self.init_window_name, text="  校对失败总数 ", width = 15,height = 2, font=("微软雅黑", "10", "bold"))

        self.lat_ver_label.grid(row = label_x + 0, column = label_y + 0)
        self.cur_ver_label.grid(row = label_x + 1, column = label_y + 0)
        self.fw_ver_label.grid (row = label_x + 2, column = label_y + 0)
        self.bt_name_label.grid(row = label_x + 3, column = label_y + 0)
        self.bt_addr_label.grid(row = label_x + 4, column = label_y + 0)
        self.fin_resl_label.grid(row = label_x + 5, column = label_y + 0)
        self.count_a_label.grid(row = label_x + 7, column = label_y + 0)
        self.count_s_label.grid(row = label_x + 7, column = label_y + 1)
        self.count_f_label.grid(row = label_x + 7, column = label_y + 2)

        

        entry_x = 1
        entry_y = 1

        self.lat_ver_entry  = Entry(self.init_window_name, textvariable = self.latest_ver,        width = 25)
        self.cur_ver_entry  = Entry(self.init_window_name, textvariable = self.current_ver,       width = 25)
        self.fw_ver_entry   = Entry(self.init_window_name, textvariable = self.fw_vers,      width = 25)
        self.bt_name_entry  = Entry(self.init_window_name, textvariable = self.bt_name,    width = 25)
        self.bt_addr_entry  = Entry(self.init_window_name, textvariable = self.bt_addr, width = 25)
        self.fin_resl_entry  = Entry(self.init_window_name, textvariable = self.fin_resl, width=25, foreground = "red", state = "readonly")
        self.count_a_entry  = Entry(self.init_window_name, textvariable = self.all_val, width=6, font=("微软雅黑", "12", "bold"),state = "readonly")
        self.count_s_entry  = Entry(self.init_window_name, textvariable = self.succ_val, width=6, font=("微软雅黑", "12", "bold"),state = "readonly", foreground = "blue")
        self.count_f_entry  = Entry(self.init_window_name, textvariable = self.fail_val, width=6, font=("微软雅黑", "12", "bold"),state = "readonly", foreground = "red")
        
        self.lat_ver_entry.grid(row = entry_x + 0, column = entry_y + 1)
        self.cur_ver_entry.grid(row = entry_x + 1, column = entry_y + 1)
        self.fw_ver_entry.grid (row = entry_x + 2, column = entry_y + 1)
        self.bt_name_entry.grid(row = entry_x + 3, column = entry_y + 1)
        self.bt_addr_entry.grid(row = entry_x + 4, column = entry_y + 1)
        self.fin_resl_entry.grid(row = entry_x + 5, column = entry_y + 1)
        self.count_a_entry.grid(row = entry_x + 8, column = entry_y + 0)
        self.count_s_entry.grid(row = entry_x + 8, column = entry_y + 1)
        self.count_f_entry.grid(row = entry_x + 8, column = entry_y + 2)

        button_x = 1
        button_y = 1

        self.lock_button = Checkbutton(self.init_window_name, text = '锁定版本号',variable = self.state_val,command = self.Status_Entry)
        self.read_button = Button(self.init_window_name, text=" 进行读取 ", bg="lightblue"  , width=10, command = self.QccReadConfigCmd)
        self.comp_button = Button(self.init_window_name, text=" 开始对比 ", bg="lightyellow", width=10, command = self.StartComparing)
        
        self.lock_button.grid(row = button_x + 0, column = button_y + 2)
        self.read_button.grid(row = button_x + 1, column = button_y + 2)
        self.comp_button.grid(row = button_x + 2, column = button_y + 2)
    
    def Status_Entry(self):
        if self.state_val.get() == True :
            self.lat_ver_entry["state"] = "readonly"
        else :
            self.lat_ver_entry["state"] = "normal"

    def ClearInputValue(self):
        self.current_ver.set("")
        self.fin_resl.set("")
        self.fw_vers.set("")
        self.bt_name.set("")
        self.bt_addr.set("")
    
    def QccReadConfigCmd(self):
        global process_status
        global count_dut

        write_list = []
        self.fin_resl.set("")
        read_qcc_command = r".\ConfigCmd.exe dev2txt qcc_configure.txt -usbdbg 1 -database hyd.sdb -system QCC512X_CONFIG"
        self.cmd(read_qcc_command)

        if process_status == False:
            self.ClearInputValue()
            showerror(title='Read failure', message='找不到待测产品')
            return
        else:
            count_dut += 1
            self.all_val.set(count_dut)
            eugene_file = open(r"./qcc_configure.txt", "r")
            for index in range(25):
                write_list = eugene_file.readline()
                if index == 18:
                    blue_address_list = write_list[56:60] + "-" + write_list[39:41] + "-" + write_list[18:25]
                    self.bt_addr.set(blue_address_list)
                if index == 21:
                    self.bt_name.set(write_list[21:38])
            write_str   = write_list[20:48:3]
            version_str = write_list[44:48:3]
            version_str = "V = " + version_str
            self.current_ver .set(write_str)
            self.fw_vers.set(version_str)
            eugene_file.close()
            os.remove(r"./qcc_configure.txt")
    
    def ConfirmLatestVerson(self):
        InputVersonValue = self.latest_ver.get()
        self.latest_ver.set(InputVersonValue)

        return InputVersonValue

    def StartComparing(self):
        global test_success
        global test_failed
        extract_list = self.ConfirmLatestVerson()
        if not extract_list:
            showinfo(title='Tips by Eugene', message='请先输入目标版本号')
        else:
            read_list = self.current_ver.get()
            if not read_list:
                showinfo(title='Tips by Eugene', message='请先进行读取DUT信息')
            else :
              compare_reslut = op.eq(read_list, extract_list)
              if compare_reslut is True:
                self.fin_resl.set("Success")
                test_success += 1
                self.succ_val.set(test_success)
              else:
                self.fin_resl.set("Failed")
                showwarning(title='Check failure', message='当前版本号与输入的版本号不一致')
                test_failed += 1
                self.fail_val.set(test_failed)


def EugeneGUIStart():
    init_window = Tk()
    eugene_gui  = Eugene_GUI(init_window)
    eugene_gui.WindowConfigure(450, 450)

    init_window.mainloop()

EugeneGUIStart()