#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import webbrowser
import json


class FLOappStore:
	def __init__(self, root):
		self.root = root

	def start(self):
		self.MainFrame = Frame(self.root, height=1000,width=500)
		self.MainFrame.pack()
		WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
		WelcomeLabel.grid(column = 1, columnspan =2)
		self.icon=[]
		self.appButton=[]
		for i in range(len(apps)):
			self.icon= self.icon+[PhotoImage(file=apps[i]["icon"])]
			self.appButton = self.appButton + [Button(self.MainFrame,text=apps[i]["name"],image = self.icon[i],compound="left",width="500",height="50",command=lambda i=i:self.execute(i))]
			self.appButton[i].grid(column = 1)

	def execute(self,i):
		print(apps[i]["name"])
		if(apps[i]["type"] == "Gui"):
			subprocess.Popen(apps[i]["exec"], cwd=apps[i]["location"])
		elif(apps[i]["type"] == "Cmdline"):
			subprocess.Popen(["mate-terminal --command %s" % (apps[i]["exec"])],cwd=apps[i]["location"],stdout=subprocess.PIPE,shell=True)
		elif(apps[i]["type"] == "Webapp"):
			webbrowser.open(apps[i]["exec"],new=1)

with open('AppData.json',encoding='utf-8') as F:
	apps=json.loads(F.read())["Dapps"]
root = Tk()
root.title("FLOappStore")
gui = FLOappStore(root)
gui.start()
root.mainloop()
