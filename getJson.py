import requests
import json 
import subprocess
import hashlib

JsonAddress = 'oXa7t72t3CgnR11ycxVfdupz55eucHufHj'

def searchDict(dicArr,key,val):
    for i in range(len(dicArr)):
        if(dicArr[i][key]==val):
            return i
    return -1

def findHash(data):
    result = hashlib.sha1(data.encode())
    return str(result.hexdigest())

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

def verifyHash(localHash,txid):
    content = readUnitFromBlockchain(txid)
    try:
        if(json.loads(content)['hash'] == localHash):
            print("true")
            return True
        else:
            return False
    except:
        return False


def getJsonData(Dapps, lastTx):
    r = requests.get("https://testnet.florincoin.info/ext/getaddress/"+JsonAddress)
    data = json.loads(r.content)
    #print(data)
    localHash = findHash(str(Dapps))
    if(lastTx == -1 or not verifyHash(localHash,data['last_txs'][lastTx]['addresses'])):
        lastTx = 0
    print(lastTx)
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
            if 'Dapp' in app.keys():
                Dapps = Dappend(Dapps,app['Dapp'])
    #print(Dapps)
    return (Dapps,len(data['last_txs'])-1)

try:
    with open('Apps.json','r') as F:
        data=json.loads(F.read())
        apps = data['Dapps']
        lastTx = data['lastTx']
except:
    apps = []
    lastTx = -1

print(apps)
print(lastTx)
(apps,lastTx) = getJsonData(apps,lastTx)

with open('Apps.json','w+') as F:
    data = json.dumps({'Dapps':apps ,'lastTx':lastTx})
    print(data)
    F.write(data)


