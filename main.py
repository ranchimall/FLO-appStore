from tkinter import *
from tkinter import messagebox
import subprocess


class FLOappStore:
	def __init__(self, root):
		self.root = root

	def start(self):
		self.MainFrame = Frame(self.root, height=1000,width=500)
		self.MainFrame.pack()
		WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
		WelcomeLabel.grid(column = 1, columnspan =2)
		self.img = PhotoImage(file="apps/FLO-Shared-Secret/flo.png")
		button = Button(self.MainFrame,image = self.img,width="50",height="50",command=lambda:self.execute('apps/FLO-Shared-Secret/FLO_Secret'))
		button.grid()

	def execute(self,f):
		subprocess.run([f])
root = Tk()
root.title("FLOappStore")
gui = FLOappStore(root)
gui.start()
root.mainloop()