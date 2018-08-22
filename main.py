#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import webbrowser
import json
import math


class FLOappStore:
	def __init__(self, root):
		self.root = root
		self.maxRow=5
		self.maxCol=2
		self.flag=0

	def start(self):
		self.MainFrame = Frame(self.root)
		self.MainFrame.pack()
		WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
		WelcomeLabel.grid(row=1,column = 1,columnspan=2)
		self.searchBox=Entry(self.MainFrame)
		self.searchBox.grid(row=2,column=1,sticky="E")
		self.searchButton=Button(self.MainFrame,text="Search",command = self.searchApps)
		self.searchButton.grid(row=2,column=2,sticky="W")
		self.clearSearch()

		
	def clearSearch(self):
		if self.flag==1:
			self.clearSearchButton.destroy()
			self.flag=0
		self.searchBox.delete(0, 'end')
		self.searchApps()

	def searchApps(self):
		self.searchResult=[]
		searchText=self.searchBox.get()
		if(searchText != ""):
			self.flag=1
			self.clearSearchButton=Button(self.MainFrame,text="Clear Search",command = self.clearSearch)
			self.clearSearchButton.grid(row=2,column=2,sticky="N")
		if(searchText == "" and self.flag == 1):
			self.flag=0
			self.clearSearchButton.destroy()
		for app in apps:
			if (searchText.lower() in app["name"].lower()):
				self.searchResult = self.searchResult + [app]
		self.totalPage = math.ceil(len(self.searchResult)/(self.maxRow*self.maxCol))
		self.listApps(1)

	def listApps(self,pageNum):
		try:
			self.listFrame.destroy()
		except:
			None

		self.listFrame = Frame(self.MainFrame)
		if not len(self.searchResult):
			noResultLabel = Label(self.listFrame,text="No Apps found!")
			noResultLabel.grid()
			self.listFrame.grid(column=1,columnspan=2)
			return

		if pageNum<1:
			pageNum=self.totalPage
		elif pageNum>self.totalPage:
			pageNum=1

		self.icon=[]
		self.appButton=[]
		Xrow=1
		Xcol=1
		startIndex=(pageNum-1)*(self.maxRow*self.maxCol)

		for app in self.searchResult[startIndex:]:
			self.icon= self.icon+[PhotoImage(file=app["icon"])]
			self.appButton = self.appButton + [Button(self.listFrame,text=app["name"],image = self.icon[-1],compound="left",width="500",height="50",command=lambda app=app:self.execute(app))]
			self.appButton[-1].grid(row = Xrow,column = Xcol)
			Xcol=Xcol+1
			if (Xcol>self.maxCol):
				Xcol=1
				Xrow=Xrow+1
				if (Xrow>self.maxRow):
					break
		prevButton = Button(self.listFrame,text="Prev",command=lambda :self.listApps(pageNum-1))
		nextButton = Button(self.listFrame,text="Next",command=lambda :self.listApps(pageNum+1))
		pageLabel = Label(self.listFrame,text=f"{pageNum}/{self.totalPage}")
		prevButton.grid(row=self.maxRow+1,column=1,columnspan=self.maxCol,sticky="W")
		nextButton.grid(row=self.maxRow+1,column=1,columnspan=self.maxCol,sticky="NE")
		pageLabel.grid(row=self.maxRow+1,column=1,columnspan=self.maxCol,sticky="N")
		self.listFrame.grid(column=1,columnspan=2)

	def execute(self,app):
		print(app["name"])
		if(app["type"] == "Gui"):
			subprocess.Popen(app["exec"], cwd=app["location"])
		elif(app["type"] == "Cmdline"):
			subprocess.Popen(["gnome-terminal --command %s" % (app["exec"])],cwd=app["location"],stdout=subprocess.PIPE,shell=True)
		elif(app["type"] == "Webapp"):
			webbrowser.open(app["exec"],new=1)

with open('AppData.json',encoding='utf-8') as F:
	apps=json.loads(F.read())["Dapps"]
root = Tk()
root.title("FLOappStore")
root.geometry("1100x500")
root.resizable(0,0)
gui = FLOappStore(root)
gui.start()
root.mainloop()


