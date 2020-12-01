from tkinter import *
import hashlib
import os
import subprocess as sp




def play1():
	z=(sp.getoutput("docker run -dit  --name cs1.6 -v /tmp/.X11-unix/:/tmp/.X11-unix/  -v /media/sf_lwsoftware/games:/root/wine -e DISPLAY=$DISPLAY --net=host cs1.6"))
	print(z)

def play2():
	z=(sp.getoutput("docker run -dit  --name solitaire -v /tmp/.X11-unix/:/tmp/.X11-unix/  -v /media/sf_lwsoftware/games:/root/wine -e DISPLAY=$DISPLAY --net=host solitaire"))
	print(z)

def play3():
	z=(sp.getoutput("docker run -dit  --name minecraft -v /tmp/.X11-unix/:/tmp/.X11-unix/  -v /media/sf_lwsoftware/games:/root/wine -e DISPLAY=$DISPLAY --net=host minecraft"))
	print(z)

def play4():
	z=(sp.getoutput("docker run -dit  --name wol -v /tmp/.X11-unix/:/tmp/.X11-unix/  -v /media/sf_lwsoftware/games:/root/wine -e DISPLAY=$DISPLAY --net=host wol"))
	print(z)




def stop1():
	z=(sp.getoutput("docker stop cs1.6"))
	print(z)
	y=(sp.getoutput("docker rm cs1.6"))
	print(y)
	
def stop2():
	z=(sp.getoutput("docker stop solitaire"))
	print(z)
	y=(sp.getoutput("docker rm solitaire"))
	print(y)
	
def stop3():
	z=(sp.getoutput("docker stop minecraft"))
	print(z)
	y=(sp.getoutput("docker rm minecraft"))
	print(y)
	
def stop4():
	z=(sp.getoutput("docker stop wol"))
	print(z)
	y=(sp.getoutput("docker rm wol"))
	print(y)


def dashboard():
	#screen3 = Toplevel(screen1) 
	screen3=Tk() 
	screen3.geometry('1080x720')  
	screen3.title('Dashboard  | GIC  | Gaming Inside Container')
	Label(screen3, text = "Wecome to GIC  Gaming Inside Container: Dashboard", fg="white" , bg = "darkred", width = "1080", height = "3", font = ( "Calibri", 16)).pack()
	Label(text = "").pack()
	Label(screen3, text = "Here is some of the awesome games of windows running inside linux containner" , font = ( "Calibri", 12)).pack()
	Label(screen3, text = "").pack()
	Label(screen3, text="Counter Strike 1.6", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=80, y=150)
	Label(screen3, text="Solitaire", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=80, y=200)
	Label(screen3, text="Minecraft", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=80, y=250)
	Label(screen3, text="West of Loathing", fg="white" , bg = "darkred", font = ( "Calibri", 12)).place(x=80, y=300)

	Button(screen3, text = "Play", width = 10, height = 1, command = play1).place(x=270, y=145)
	Button(screen3, text = "Stop", width = 10, height = 1, command = stop1).place(x=410, y=145)
	Button(screen3, text = "Play", width = 10, height = 1, command = play2).place(x=270, y=195)
	Button(screen3, text = "Stop", width = 10, height = 1, command = stop2).place(x=410, y=195)
	Button(screen3, text = "Play", width = 10, height = 1, command = play3).place(x=270, y=245)
	Button(screen3, text = "Stop", width = 10, height = 1, command = stop3).place(x=410, y=245)
	Button(screen3, text = "Play", width = 10, height = 1, command = play4).place(x=270, y=295)
	Button(screen3, text = "Stop", width = 10, height = 1, command = stop4).place(x=410, y=295)
	screen3.mainloop()
	

#dashboard()
