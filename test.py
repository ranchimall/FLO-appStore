from tkinter import *
from tkinter import messagebox
import subprocess
import os
import webbrowser
import json
app={}
app["location"] = 'apps/FLO-shared-secret/'
app["github"] = "https://github.com/akhil2015/FLO-shared-secret.git"
print(os.path.isdir(app["location"]))
#print(os.path.isdir(app["location"]) and subprocess.Popen("git config --get remote.origin.url",cwd=app["location"],stdout=subprocess.PIPE,shell=True).communicate()[0].decode("utf-8")==app["github"])
#print(subprocess.Popen("git diff --raw",cwd=app["location"],stdout=subprocess.PIPE,shell=True).communicate()[0]=="")
subprocess.Popen(['rm', '-rf', app['location']])