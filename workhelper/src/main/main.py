#!/usr/bin/python
#coding=UTF-8
import sys,os,time

# import Tkinter

from tkinter import *
import tkinter.messagebox
from workhelper.src.main.project.icbc import icbcWorkFrame as icbc
from workhelper.src.main.project.icbc.icbcwork import icbcwork

# print("hello")

appWindow = Tk()

# 一般设置
appWindow.title('工作助手')
appWindow.geometry('500x500+500+200')


# 添加按钮列表
btn_width = '100'
btn_bg = "lightblue"
btn_name_list = ['工行','农行','test3','test4']

frame = None
# workFrame
workFrame = tkinter.Frame(appWindow)
workFrame.pack()


# for name in btn_name_list :
#     btn_test = Button(appWindow, text= name, bg="lightblue", width="100")
#     btn_test.pack()
def onClickForTest():
    info = "work for test"
    print(info)
    tkinter.messagebox.showinfo(title="显示输入内容", message=info)
    # frame.pack_forget()
    frame = icbc.getIcbcFrame(workFrame)
    frame.pack()


def onClickForICBC():
    print("work for ICBC")
    frame = icbc.getIcbcFrame(workFrame)
    frame.pack()
    # icbc_work = icbcwork()
    # icbc_work.openandroidas()
    # icbc_work.openios()
    # icbc_work.openroot()

def onClickForABC():
    print("work for ABC")


path = StringVar()

def onClickForHash():
    hash_path = path.get()
    print("hash:%s" % (hash_path))
    cmd = "sh ../../file/hash.sh %s" % (hash_path)
    os.system(cmd)


btn_test = Button(appWindow, text="test", bg=btn_bg, width=btn_width, command = onClickForTest)
btn_test.pack()

btn_icbc = Button(appWindow, text= "工行", bg=btn_bg, width=btn_width, command = onClickForICBC )
btn_icbc.pack()

btn_abc = Button(appWindow, text= "农行", bg=btn_bg, width=btn_width, command = onClickForABC )
btn_abc.pack()

btn_abc = Button(appWindow, text= "计算hash", bg=btn_bg, width=btn_width, command = onClickForHash )
btn_abc.pack()


# 待hash的目录
text_hash_path = Entry(appWindow,textvariable= path)
text_hash_path.pack()


# 进入消息循环
appWindow.mainloop()


