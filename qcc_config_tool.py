# coding:utf-8
import time
import subprocess

import os
import tkinter as tk
import tkinter.messagebox

result_detial = "null"

def center_window(w = 300, h = 200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))

def cmd(command):
    subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    subp.wait(2)
    if subp.poll() == 0:
        print(subp.communicate()[1])
        OpenFile(subp.communicate()[1])
    else:
        print("fail")

def GetWavFile():
    cmd("gcc -v")
    """ cmd("exit 1") """

def OpenFile(str):
    eugene_file = open("qcc3021_detail.txt","wb")
    eugene_file.close()
    eugene_file = open("qcc3021_detail.txt","w")
    eugene_file.write(str)
    eugene_file.close()

root = tkinter.Tk(className=' Qualcomm Prompt Create Tool')
center_window(400, 300)

c = tk.StringVar()

a = 1
b = 1
tk.Label(root, text = "  0.0.wav  ").grid(row = a,column = b)
tk.Entry(root,textvariable = "lajiguoguang", bd = 3, width = 10).grid(row = a,column = b+1)
tk.Button(root, text =" 垃圾国光 ",bd = 3, command = GetWavFile, activebackground = "yellow").grid(row = a, column = b+2)

root.mainloop()