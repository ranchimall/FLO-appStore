def searchDict(dicArr,key,val):
    for i in range(len(dicArr)):
    	if(dicArr[i][key]==val):
            return i
    return -1

d = [{'id': '1', 'name': 'Alexandria', 'icon': 'Icon/Alexandria.png', 'type': 'Webapp', 'url': 'https://alexandria.io/browser/'}, {'id': '2', 'name': 'AlternateLove', 'icon': 'Icon/AternaLove.png', 'type': 'Cmdline', 'location': 'apps/aternalove', 'exec': './auto-aterna-love.sh', 'github': 'https://github.com/metacoin/aternalove.git'}, {'id': '3', 'name': 'Caltech', 'icon': 'Icon/Caltech.png', 'type': 'Webapp', 'url': 'https://etdb.caltech.edu/browse'}, {'id': '4', 'name': 'Flotorizer', 'icon': 'Icon/Flotorizer.png', 'type': 'Webapp', 'url': 'http://flotorizer.net/'}, {'id': '5', 'name': 'Medici', 'icon': 'Icon/Medici.png', 'type': 'Webapp', 'url': 'https://www.mediciventures.com/'}, {'id': '6', 'name': 'FloSharedSecret', 'icon': 'Icon/SharedSecret.png', 'type': 'Gui', 'location': 'apps/FLO-shared-secret/', 'exec': './FLO_Secret', 'github': 'https://github.com/akhil2015/FLO-shared-secret.git'}, {'id': '7', 'name': 'FloRate', 'icon': 'Icon/Florate.png', 'type': 'Gui', 'location': 'apps/FloRate-Dapp/', 'exec': './Florate', 'github': 'https://github.com/Tarun047/FloRate-Dapp.git'}, {'id': '8', 'name': 'tZero', 'icon': 'Icon/tZero.png', 'type': 'Webapp', 'url': 'https://www.tzero.com/'}, {'id': '9', 'name': 'WorldMood', 'icon': 'Icon/WorldMood.png', 'type': 'Webapp', 'url': 'http://worldmood.io/'}, {'id': '10', 'name': 'Xcertify', 'icon': 'Icon/Xcertify.png', 'type': 'Cmdline', 'location': 'apps/Xcertify/', 'exec': './xcertify', 'github': 'https://github.com/akhil2015/Xcertify.git'}]
del(d[1])
print(d)
i = searchDict(d,'id','4')
if(i!=-1):
	print(i)
