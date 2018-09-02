# FLO-AppStore
This is a Tkinter(Python 3) based gui app,which lets users to download/install,update,remove,execute and manage other FLO Dapps.The app reads the details of other dapps from AppData.json file.
The details are as follows 
id - App id
name - Name of the app
icon - Icon img location 
type - App type (webapp, cmdline or gui)

Webapps are available as website n should be opened in browser
Gui apps are open by running their binary files
Cmdline apps are open in terminal using gnome-terminal by executing their cmd(binary)

In addition to those values the following values are also in json file, 
webapps url - url link to the website
Gui and Cmdline dapps :
github - GitHub repo link of the app
exec - execution cmd for the binary

A button for each app (with icon and app name) is generated for each app.The appstore shows 10 (5rows*2columns) apps per page.

## Requirements
1. Linux operating system(working on a cross platform version).
2. git (to install git):
		sudo apt-get install git

## Usage
1. Clone/download this repository. (https://github.com/sairajzero/FLO-appStore/)
2. Run the binary file (FLO_appStore)
		./FLO_appStore
3. For installing an dapp,user needs to click on respective app.A popup window will open which ask user to download the dapp if not previously installed.Once installed the same popup window will have extra buttons to open/remove dapp.
4. Updates for dapps are checked everytime when user is connected to Internet.Click on dapp which user want to update,if any updates are available,update button will automatically be displayed in the popup window.
5. User can also search for any dapp in flostore using Search bar feature.
6. For navigating to other pages in Flostore,use Next/Prev Buttons.

## Other Infos

1. Source code of the AppStore is main.py
2. Apps are downloaded in the apps directory
3. Icons for the apps are stored in icon directory

**Do not remove the directories and/or files mannually**
