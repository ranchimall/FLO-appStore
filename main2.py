#!/usr/bin/env python3
from tkinter import *
import webbrowser
from tkinter import messagebox
import subprocess


class FLOappStore:
	def __init__(self, root):
		self.root = root

	def medici(self):
		webbrowser.open("https://www.mediciventures.com/",new=1)

	def start(self):
		self.MainFrame = Frame(self.root, height=1000,width=500)
		self.MainFrame.pack()
		WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
		WelcomeLabel.grid(column = 1, columnspan =4)
		self.img1 = PhotoImage(file="Logos/SharedSecret.png")
		button1 = Button(self.MainFrame,image = self.img1,width="187",height="186",command=lambda:self.execute('apps/FLO-Shared-Secret/FLO_Secret'))
		button1.grid(row=2,column=1)
		self.img2 = PhotoImage(file="Logos/Medici.png")
		button2 = Button(self.MainFrame, image=self.img2, width="187", height="186",command=self.medici)
		button2.grid(row=2, column=2)

	def execute(self,f):
		subprocess.run([f])
root = Tk()
root.title("FLOappStore")
gui = FLOappStore(root)
gui.start()
root.mainloop()
