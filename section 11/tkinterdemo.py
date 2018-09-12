try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hellow World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
canvas.pack(side='left')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")
button3 = tkinter.Button(mainWindow, text="button3")
button1.pack(side='left', anchor='n')
button2.pack(side='top', anchor='s')
button3.pack(side='right', anchor='e')

mainWindow.mainloop()
