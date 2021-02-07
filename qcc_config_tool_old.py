# -*- coding: UTF-8 -*-
import subprocess

import os
import operator as op


from tkinter import *
from tkinter.messagebox import *

from enum import Enum

write_list = []
count_dut = 0
process_status = False


def center_window(w=300, h=200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.resizable(False, False)


def cmd(command):
    global process_status
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        #print(subp.communicate()[1])
        process_status = True
    else:
        process_status = False


def GetWavFile():
    current_ver.set("")
    final_result.set("")
    firmware_ver.set("")
    bluetooth_name.set("")
    bluetooth_address.set("")


def ConfirmLatestVerson():
    InputVersonValue = latest_ver.get()
    latest_ver.set(InputVersonValue)

    return InputVersonValue


def StartComparing():
    extract_list = ConfirmLatestVerson()
    if not extract_list:
        showinfo(title='Tips by Eugene', message='请先输入目标版本号')
    else:
        read_list = current_ver.get()
        if not read_list:
            showinfo(title='Tips by Eugene', message='请先进行读取DUT信息')
        else :
          compare_reslut = op.eq(read_list, extract_list)
          if compare_reslut is True:
            final_result.set("Success")
          else:
            final_result.set("Failed")
            showwarning(title='Check failure', message='当前版本号与输入的版本号不一致')


def QccReadConfigCmd():
    global process_status
    global count_dut
    write_list = []
    final_result.set("")
    read_qcc_command = r".\ConfigCmd.exe dev2txt qcc_configure.txt -usbdbg 1 -database hyd.sdb -system QCC512X_CONFIG"
    cmd(read_qcc_command)

    if process_status == False:
        GetWavFile()
        showerror(title='Read failure', message='找不到待测产品')
        return
    else:
        count_dut += 1
        count.set(count_dut)
        eugene_file = open(r"./qcc_configure.txt", "r")
        for index in range(25):
            write_list = eugene_file.readline()
            if index == 18:
                blue_address_list = write_list[56:60] + "-" + write_list[39:41] + "-" + write_list[18:25]
                bluetooth_address.set(blue_address_list)
            if index == 21:
                bluetooth_name.set(write_list[21:38])
        write_str   = write_list[20:48:3]
        version_str = write_list[44:48:3]
        version_str = "V = " + version_str
        current_ver .set(write_str)
        firmware_ver.set(version_str)
        eugene_file.close()
        os.remove(r"./qcc_configure.txt")

def Status_Entry():
    if status_value.get() == True :
        Entry(root, textvariable=latest_ver, width=20, state="readonly"  ).grid(row=1, column=2)
    else :
        Entry(root, textvariable=latest_ver, width=20, state="normal"  ).grid(row=1, column=2)


root = Tk(className=" Qualcomm Verson Check Tool")
center_window(400, 300)


a = 1
b = 1
Label(root, text="  最新版本号  ").grid(row=a, column=b)
latest_ver = StringVar()
latest_ver.set("")
write_verson = Entry(root, textvariable=latest_ver, width=20,state = "normal").grid(row=a, column=b+1)
write_verson = Entry(root, textvariable=latest_ver, width=20,state = "normal").grid(row=a, column=b+1)

status_value = IntVar()
status_value.set("0")
Checkbutton(root,text = '锁定版本号',variable = status_value,command = Status_Entry).grid(row = a, column = b+2)


a = 2

Label(root, text="  当前版本号  ").grid(row=a, column=b)
current_ver = StringVar()
latest_ver.set("")
Entry(root, textvariable=current_ver, width=20).grid(row=a, column=b+1)

Button(root, text=" 进行读取 ", command=QccReadConfigCmd, bg="lightblue", width=10).grid(row=a, column=b+2)


a = 3

Label(root, text="  固件版本  ",).grid(row=a, column=b)
firmware_ver= StringVar()
firmware_ver.set("")
Entry(root, textvariable=firmware_ver, width=20).grid(row=a, column=b+1)

a = 4

Label(root, text="  蓝牙名称  ").grid(row=a, column=b)
bluetooth_name = StringVar()
Entry(root, textvariable=bluetooth_name, width=20).grid(row=a, column=b+1)
bluetooth_name.set("")

a = 5

Label(root, text="  蓝牙地址  ").grid(row=a, column=b)
bluetooth_address = StringVar()
Entry(root, textvariable=bluetooth_address, width=20).grid(row=a, column=b+1)
bluetooth_address.set("")

Button(root, text=" 开始对比 ", command=StartComparing, bg="lightyellow", width=10).grid(row=6, column=3)

a = 6

final_result = StringVar()
Label(root, textvariable = final_result, width=20, foreground = "red", font=('微软雅黑', 10, 'bold')).grid(row=a, column=b + 1)
final_result.set("")

count = StringVar()
count.set("0")
Label(root, textvariable = count, width=6, font=("宋体", "8")).grid(row=a, column=b)


mainloop()
