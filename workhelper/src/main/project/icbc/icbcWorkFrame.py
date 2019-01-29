from tkinter import *
import tkinter.messagebox



def getIcbcFrame(parent):
    icbcFrame = tkinter.Frame(width = 500, height=300)
    btn_test = Button(icbcFrame, text="test", bg='white', width=100)
    btn_test.pack()

    return icbcFrame