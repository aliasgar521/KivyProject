import sys
import os
import Tkinter
import tkMessageBox

top=Tkinter.Tk()

def red():
	import pong
	pong.PongApp().run()
		#main()
    #os.system('python pong.py')

def yellow():
    os.system('python yellow.py')
def blue():
    os.system('python purple.py')
def green():
    os.system('python green.py')

A=Tkinter.Button(top,text="red",command= red)
B=Tkinter.Button(top,text="yellow",command= yellow)
C=Tkinter.Button(top,text="blue",command= blue)
D=Tkinter.Button(top,text="green",command= green)
A.pack()
B.pack()
C.pack()
D.pack()
top.mainloop()


