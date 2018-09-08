import requests
import json 
import subprocess

def getJsonData():
    r = requests.get("https://testnet.florincoin.info/ext/getaddress/ocZXNtzpiUqBvzQorjAKmZ5MhXxGTLKeSH")
    data = json.loads(r.content)
    #print(data)

    def readUnitFromBlockchain(txid):
        rawtx = subprocess.check_output(["flo-cli","--testnet", "getrawtransaction", str(txid)])
        rawtx = str(rawtx)
        rawtx = rawtx[2:-3]
        tx = subprocess.check_output(["flo-cli","--testnet", "decoderawtransaction", str(rawtx)])
        content = json.loads(tx)
        text = content['floData']
        return text

    Dapps = []
    for i in range(len(data['last_txs'])):
        if(data['last_txs'][i]['type']=='vin'):
            content = readUnitFromBlockchain(data['last_txs'][i]['addresses'])
            #print(content)
            if content.startswith("text:Dapps"):
                print(data['last_txs'][i]['addresses'])
                pos = content.find('{')
                Dapps = Dapps + [json.loads(content[pos:])]

    print(Dapps)
    return Dapps