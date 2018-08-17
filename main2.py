#!/usr/bin/env python3
from tkinter import *
import subprocess
import os
import webbrowser

current_dir=os.getcwd()

class FLOappStore:
	def __init__(self, root):
		self.root = root

	def medici(self):
		webbrowser.open("https://www.mediciventures.com/",new=1)

	def alexandria(self):
		webbrowser.open("https://alexandria.io/browser/",new=1)

	def caltech(self):
		webbrowser.open("https://etdb.caltech.edu/browse",new=1)

	def tzero(self):
		webbrowser.open("https://www.tzero.com/",new=1)

	def worldmood(self):
		webbrowser.open("http://worldmood.io/",new=1)

	def flotorizer(self):
		webbrowser.open("http://flotorizer.net/",new=1)

	def xcertify(self):
		os.chdir('apps/Xcertify/')
		os.system('gnome-terminal -- ./xcertify')
		os.chdir(current_dir)

	def aternalove(self):
		os.chdir('apps/Aterna-Love/')
		os.system('gnome-terminal -- ./auto-aterna-love.sh')
		os.chdir(current_dir)

	def start(self):
		self.MainFrame = Frame(self.root, height=1000,width=500)
		self.MainFrame.pack()
		WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
		WelcomeLabel.grid(column = 1, columnspan =4)
		self.img1 = PhotoImage(file="Logos/SharedSecret.png")
		button1 = Button(self.MainFrame,image = self.img1,width="187",height="186",command=lambda:self.execute('apps/FLO-Shared-Secret/FLO_Secret'))
		button1.grid(row=2,column=1)
		self.img2 = PhotoImage(file="Logos/Medici.png")
		button2 = Button(self.MainFrame,image=self.img2, width="187",height="186",command=self.medici)
		button2.grid(row=2, column=2)
		self.img3= PhotoImage(file="Logos/Flotorizer.png")
		button3= Button(self.MainFrame,image=self.img3,width="187",height="186",command=self.flotorizer)
		button3.grid(row=2,column=3)
		self.img4 = PhotoImage(file="Logos/WorldMood.png")
		button4 = Button(self.MainFrame,image=self.img4,width="187",height="186",command=self.worldmood)
		button4.grid(row=2,column=4)
		self.img5 = PhotoImage(file="Logos/tZero.png")
		button5 = Button(self.MainFrame, image=self.img5, width="187", height="186",command=self.tzero)
		button5.grid(row=3, column=1)
		self.img6 = PhotoImage(file="Logos/Alexandria.png")
		button6 = Button(self.MainFrame, image=self.img6, width="187", height="186",command=self.alexandria)
		button6.grid(row=3, column=2)
		self.img7 = PhotoImage(file="Logos/Caltech.png")
		button7 = Button(self.MainFrame, image=self.img7, width="187", height="186",command=self.caltech)
		button7.grid(row=3, column=3)
		self.img8 = PhotoImage(file="Logos/Xcertify.png")
		button8 = Button(self.MainFrame, image=self.img8, width="187", height="186",command=self.xcertify)
		button8.grid(row=3, column=4)
		self.img9 = PhotoImage(file="Logos/Florate.png")
		button9 = Button(self.MainFrame, image=self.img9, width="187", height="186",command=lambda:self.execute('apps/Florate/Florate'))
		button9.grid(row=4, column=1)
		self.img10 = PhotoImage(file="Logos/AternaLove.png")
		button10 = Button(self.MainFrame, image=self.img10, width="187", height="186",command=self.aternalove)
		button10.grid(row=4, column=2)


	def execute(self,f):
		subprocess.run([f])
root = Tk()
root.title("FLOappStore")
gui = FLOappStore(root)
gui.start()
root.mainloop()
