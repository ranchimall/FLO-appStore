import subprocess
import json
import requests
import hashlib

def searchDict(dicArr,key,val):
    for i in range(len(dicArr)):
        if(dicArr[i][key]==val):
            return i
    return -1

def readUnitFromBlockchain(txid):
    rawtx = subprocess.check_output(["flo-cli","--testnet", "getrawtransaction", str(txid)])
    rawtx = str(rawtx)
    rawtx = rawtx[2:-3]
    tx = subprocess.check_output(["flo-cli","--testnet", "decoderawtransaction", str(rawtx)])
    content = json.loads(tx)
    text = content['floData']
    return str(text)

def Dappend(Dapps,app):
    i = searchDict(Dapps,'id',app['id'])
    if (i!=-1):
        del(Dapps[i])
    if ('remove' not in app.keys()):
        Dapps = Dapps + [app]
    return Dapps

def getJsonData(JsonAddress):
    r = requests.get("https://testnet.florincoin.info/ext/getaddress/"+JsonAddress)
    data = json.loads(r.content)
    #print(data)
    Dapps = []
    for i in range(len(data['last_txs'])):
        if(data['last_txs'][i]['type']=='vin'):
            content = readUnitFromBlockchain(data['last_txs'][i]['addresses'])
            try:
                app = json.loads(content)
            except : 
                continue
            #print(app)
            try:
                if 'Dapp' in app.keys():
                    Dapps = Dappend(Dapps,app['Dapp'])
            except:
                continue
    #print(Dapps)
    return Dapps

def findHash(data):
    result = hashlib.sha1(data.encode())
    return str(result.hexdigest())


JsonAddress=input('Enter Admin address :')
apps = getJsonData(JsonAddress)
#print(apps)

print("Enter app Details :")
appData = {}
appData['id'] = input('Enter App ID \t: ')
if input('Remove app ? (Y/N)') == 'Y':
    appData['remove'] = True
else:
    appData['name'] = input('Enter App Name \t: ')
    appData['description'] = input('Enter Description \t: ')
    appData['icon'] = input('Enter Icon location \t: ')
    appData['type'] = input('Enter App Type (Webapp|Cmdline|Gui): ')
    if appData['type'] == 'Webapp':
        appData['url'] = input('Enter App url \t: ')
    elif appData['type'] == 'Cmdline' or appData['type'] == 'Gui':
        appData['github'] = input('Enter Github link (.git) \t: ')
        appData['location'] = 'apps/'+input('Enter Repository name \t: ') +'/'
        appData['exec'] = input('Enter execution cmd (eg. ./binary) \t: ')

print(appData)
apps = Dappend(apps ,appData)
#print(apps)
apphash = findHash(str(apps))

floData = json.dumps({'Dapp':appData ,'hash':apphash})
print('\nfloData = '+floData)

