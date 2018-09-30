import subprocess
import json
import random
import requests
import hashlib

JsonAddress = 'oXa7t72t3CgnR11ycxVfdupz55eucHufHj'
toAddress = 'oXa7t72t3CgnR11ycxVfdupz55eucHufHj'
tempAcc = str(random.randint(100000,999999))
amt = '0.01'

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

def getJsonData():
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
            if 'Dapp' in app.keys():
                Dapps = Dappend(Dapps,app['Dapp'])
    #print(Dapps)
    return Dapps

def findHash(data):
    result = hashlib.sha1(data.encode())
    return str(result.hexdigest())

apps = getJsonData()
print(apps)

print("Enter floData :")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
appData = ' '.join(lines)
try:
    appData=json.loads(appData)
except:
    print('Unable to parse JSON : '+appData)
    exit(0)

print(appData)
apps = Dappend(apps , appData)
print(apps)
apphash = findHash(str(apps))

floData = json.dumps({'Dapp':appData ,'hash':apphash})
print('floData = '+floData)

process = subprocess.Popen(['flo-cli','-testnet','getaccount',JsonAddress], stdout=subprocess.PIPE)
account = process.communicate()[0].decode().strip()
process = subprocess.Popen(['flo-cli','-testnet','setaccount',JsonAddress,tempAcc], stdout=subprocess.PIPE)
process = subprocess.Popen(['flo-cli','-testnet','sendfrom',tempAcc,toAddress,amt,'6','','',floData], stdout=subprocess.PIPE)
txid = process.communicate()[0].decode()
print('txid : '+txid)
process = subprocess.Popen(['flo-cli','-testnet','setaccount',JsonAddress,account], stdout=subprocess.PIPE)
