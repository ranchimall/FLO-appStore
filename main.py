#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox
import subprocess
import os
import sys
import webbrowser
import json
import math
import socket
import requests
import hashlib

JsonAddresses = ["FT9qkvuWXWBDRhHd42tDr5nMYFSx7bEhV7","FBcRbCxwChjTdgVewGMPBDDEFXzPcc7GAH","FC6CRkRCeJEKEGF2r1SFppPD5DXfVe1zWq"]

def searchDict(dicArr,key,val):
    for i in range(len(dicArr)):
        if(dicArr[i][key]==val):
            return i
    return -1

def findHash(data):
    result = hashlib.sha1(data.encode())
    return str(result.hexdigest())

def isConnected():
    try:
        socket.create_connection(("www.github.com", 80))
        return True
    except:
        messagebox.showerror('FLOappStore', "Unable to Connect to GitHub!\nPlease check Internet connectivity and firewall!")
        return False

def readUnitFromBlockchain(txid):
    rawtx = subprocess.check_output(["flo-cli", "getrawtransaction", str(txid)])
    rawtx = str(rawtx)
    rawtx = rawtx[2:-3]
    tx = subprocess.check_output(["flo-cli", "decoderawtransaction", str(rawtx)])
    content = json.loads(tx)
    text = content['floData']
    return str(text)

def Dappend(Dapps,app):
    i = searchDict(Dapps,'id',app['id'])
    #print(str(i))
    if (i!=-1):
        del(Dapps[i])
    #print(app.keys())
    if ('remove' not in app.keys()):
        Dapps = Dapps + [app]
    return Dapps

def verifyHash(localHash,txid):
    content = readUnitFromBlockchain(txid)
    #print(content)
    try:
        if(json.loads(content)['hash'] == localHash):
            return True
        else:
            return False
    except:
        return False


def getJsonData(Dapps, lastTx,JsonAddress):
    try:
        r = requests.get("https://www.florincoin.info/ext/getaddress/"+JsonAddress)
        data = json.loads(r.content)
    except:
        isConnected()
        return
    #print(Dapps)
    localHash = findHash(str(Dapps))
    try:
        if(lastTx == -1 or not verifyHash(localHash,data['last_txs'][lastTx]['addresses'])):
            lastTx = 0
        else:
            lastTx = lastTx+1
    except:
        lastTx = 0
    #print(lastTx)
    for i in range(lastTx,len(data['last_txs'])):
        #print(i)
        if(data['last_txs'][i]['type']=='vin'):
            content = readUnitFromBlockchain(data['last_txs'][i]['addresses'])
            #print(content)
            try:
                app = json.loads(content)
            except Exception as e: 
                #print(e)
                continue
            #print(app)
            try:
                if 'Dapp' in app.keys():
                    Dapps = Dappend(Dapps,app['Dapp'])
            except:
                continue
    #print(Dapps)
    {'Dapps':apps ,'lastTx':lastTx}
    returndata = {}
    returndata['Dapps'] = Dapps
    returndata['lastTx'] = len(data['last_txs'])-1
    return (returndata)

class FLOappStore:
    def __init__(self, root):
        self.root = root
        self.maxRow=5
        self.maxCol=2

    def start(self):
        self.MainFrame = Frame(self.root)
        self.MainFrame.pack()
        WelcomeLabel = Label(self.MainFrame,text="FLO AppStore",font=("Arial", 20))
        WelcomeLabel.grid(row=1,column = 1,columnspan=2)
        self.searchBox=Entry(self.MainFrame)
        self.searchBox.grid(row=2,column=1,sticky="E")
        self.searchButton=Button(self.MainFrame,text="Search",command = self.searchApps)
        self.searchButton.grid(row=2,column=2,sticky="W")
        self.searchApps()


    def clearSearch(self):
        self.searchBox.delete(0, 'end')
        self.searchApps()

    def searchApps(self):
        try:
            self.clearSearchButton.destroy()
        except:
            None
        self.searchResult=[]
        searchText=self.searchBox.get()
        if(searchText != ""):
            self.clearSearchButton=Button(self.MainFrame,text="Clear Search",command = self.clearSearch)
            self.clearSearchButton.grid(row=2,column=2,sticky="N")
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
            try:
                img=PhotoImage(file=app["icon"])
            except:
                img=PhotoImage(file='Icon/noimage.png')
            self.icon= self.icon+[img]
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
        #print(app["name"])
        isConnected()
        self.appWin = Toplevel()
        self.appWin.title(app["name"])
        self.appWin.geometry("500x400")
        self.appWin.resizable(0,0)

        try:
            description = app["description"]
        except:
            description = '*NIL*'

        Label1 = Label(self.appWin, text="Description")
        Label1.pack()       
        GTextFrame = Frame(self.appWin)
        GScroll = Scrollbar(GTextFrame)
        GScroll.pack(side=RIGHT, fill=Y)
        self.GLMsg = Text(GTextFrame,height=10,width=50,yscrollcommand=GScroll.set)
        self.GLMsg.insert(END, description)
        self.GLMsg.config(state='disabled')
        self.GLMsg.pack(side = LEFT)
        GTextFrame.pack()
        GScroll.config(command=self.GLMsg.yview)


        if(app["type"] == "Gui" or app["type"] == "Cmdline"):
            if(os.path.isdir(app["location"]) and subprocess.Popen("git config --get remote.origin.url",cwd=app["location"],stdout=subprocess.PIPE,shell=True).communicate()[0].decode("utf-8").strip()==app["github"]):
                openButton = Button(self.appWin,text="Open App",command=lambda :self.openApp(app))
                openButton.pack()
                if(subprocess.Popen("git diff --raw",cwd=app["location"],stdout=subprocess.PIPE,shell=True).communicate()[0].decode("utf-8")!=""):
                    updateButton = Button(self.appWin,text="Update App",command=lambda :self.updateApp(app))
                    updateButton.pack()
                removeButton = Button(self.appWin,text="Remove App",command=lambda :self.removeApp(app))
                removeButton.pack()
            else:
                downloadButton = Button(self.appWin,text="Download App",command=lambda :self.downloadApp(app))
                downloadButton.pack()
        elif(app["type"] == "Webapp"):
            openButton = Button(self.appWin,text="Open Browser",command=lambda :self.openBrowserApp(app))
            openButton.pack()
        self.appWin.mainloop()

    def downloadApp(self,app):
        self.appWin.destroy()
        subprocess.Popen(['rm', '-rf', app['location']])
        if(not isConnected()):
            return
        subprocess.Popen("gnome-terminal -- git clone %s"%(app["github"]),cwd="apps/",shell=True)
        messagebox.showinfo(app['name'], f"Downloading {app['name']}...\n Please Wait until the downloader closes")

    def removeApp(self,app):
        self.appWin.destroy()
        subprocess.Popen(['rm', '-rf', app['location']])
        messagebox.showinfo(app['name'], f"Removed {app['name']}...")

    def updateApp(self,app):
        self.appWin.destroy()
        if(not isConnected()):
            return
        subprocess.Popen("gnome-terminal -- git pull --all",cwd=app['location'],shell=True)
        subprocess.Popen("gnome-terminal -- git reset --hard HEAD ",cwd=app['location'],shell=True)
        messagebox.showinfo(app['name'], f"Updating {app['name']}...\n Please Wait until the updater closes")

    def openApp(self,app):
        self.appWin.destroy()
        if(app["type"] == "Gui"):
            subprocess.Popen(app["exec"], cwd=app["location"])
        elif(app["type"] == "Cmdline"):
            subprocess.Popen("gnome-terminal --command 'bash -c %s;bash'"%(app["exec"]),cwd=app["location"],stdout=subprocess.PIPE,shell=True)

    def openBrowserApp(self,app):
        self.appWin.destroy()
        webbrowser.open(app["url"],new=1)


def refreshAppData():
    global apps
    apps = []
    print("Refreshing App Details")
    try:
        with open('Apps.json','r') as F:
            data=json.loads(F.read())
            flag = True
    except:
        flag = False
        data = {}


    for addr in JsonAddresses:
        try:
            appdata = data[addr]['Dapps']
            #print(appdata)
            lastTx = data[addr]['lastTx']
        except:
            appdata = []
            lastTx = -1
        data[addr] = getJsonData(appdata,lastTx,addr)
        #print(data[addr])
        apps = apps + data[addr]['Dapps']
    with open('Apps.json','w+') as F:
        #print(data)
        data = json.dumps(data)
        F.write(data)
    print("Loaded App Details")

def Credits():
    print("Credits")
    creditsWin = Toplevel()
    creditsWin.title('Credits')
    infoLabel = Label(creditsWin,text="FLO AppStore",font=("Arial", 16))
    infoLabel.pack()
    vLabel = Label(creditsWin,text="version 1.0",font=("Arial", 8))
    vLabel.pack()
    creditLabel1 = Label(creditsWin,text="\n--Created by--",font=("Arial", 10))
    creditLabel1.pack()
    creditLabel2 = Label(creditsWin,text="Ranchi Mall Internship Blockchain Contract",font=("Arial", 12))
    creditLabel2.pack()
    internLabel = Label(creditsWin,text="Interns : Sai Raj, Kaushal",font=("Arial", 8))
    internLabel.pack()
    forLabel1 = Label(creditsWin,text="\n--For--",font=("Arial", 10))
    forLabel1.pack()
    forLabel2 = Label(creditsWin,text="Ranchi Mall FLO Blockchain Contract",font=("Arial", 12))
    forLabel2.pack()
    
    creditsWin.mainloop()


refreshAppData()
root = Tk()
root.title("FLOappStore")
root.geometry("1100x500")
root.resizable(0,0)

menubar = Menu(root)
appmenu = Menu(menubar, tearoff=0)
appmenu.add_command(label="Refresh", command=refreshAppData)
appmenu.add_separator()
appmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="App", menu=appmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="ReadMe", command=lambda :webbrowser.open("README.md"))
helpmenu.add_command(label="GitHub", command=lambda :webbrowser.open("https://github.com/ranchimall/FLO-appStore",new=1))
helpmenu.add_separator()
helpmenu.add_command(label="Credits", command=Credits)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

gui = FLOappStore(root)
gui.start()
root.mainloop()


