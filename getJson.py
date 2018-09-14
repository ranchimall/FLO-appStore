import requests
import json 
import subprocess

JsonAddress = "ocZXNtzpiUqBvzQorjAKmZ5MhXxGTLKeSH"

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
    return text

def getJsonData():
    r = requests.get("https://testnet.florincoin.info/ext/getaddress/"+JsonAddress)
    data = json.loads(r.content)
    #print(data)
    Dapps = []
    for i in range(len(data['last_txs'])):
        if(data['last_txs'][i]['type']=='vin'):
            content = readUnitFromBlockchain(data['last_txs'][i]['addresses'])
            #print(content)
            if content.startswith("text:Dapps"):
                #print(data['last_txs'][i]['addresses'])
                pos = content.find('{')
                app = json.loads(content[pos:])
                i = searchDict(Dapps,'id',app['id'])
                if (i!=-1):
                    del(Dapps[i])
                if ('remove' not in app.keys()):
                    Dapps = Dapps + [app]
    #print(Dapps)
    return Dapps

apps = getJsonData()
print(apps)