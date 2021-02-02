#!C:\Python27\python.exe
# -*- coding:UTF-8 -*-

import os
import tkinter as tk
import tkinter.messagebox

from tkinter import filedialog,ttk

def center_window(w = 300, h = 200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


def opendir():
  dir=os.path.dirname(fpath.get())
  os.system('start '+ dir)

def GetWavFile():
  file_path=filedialog.askopenfilename()
  fpath.set(file_path)


root = tkinter.Tk(className=' Qualcomm Prompt Create Tool')
center_window(600, 500)

fpath=tk.StringVar()

a = 0
b = 0
tk.Label(root, text = "  0.0.wav  ").grid(row = a,column = b)
filedialog.Entry(root, textvariable = fpath, bd = 3, width = 55).grid(row = a,column = b+1)
tk.Button(root, text ="Open Audio File",bd = 2, command = GetWavFile, activebackground = "yellow").grid(row = a, column = b+2)

a = 1
b = 0
tk.Label(root, text = "  1.0.wav  ").grid(row = a,column = b)
filedialog.Entry(root,textvariable = fpath, bd = 3, width = 55).grid(row = a,column = b+1)
tk.Button(root, text ="Open Audio File",bd = 2, command = GetWavFile, activebackground = "yellow").grid(row = a, column = b+2)

root.mainloop()