import subprocess
import json


def writeDatatoBlockchain(text,receiver,amt):
    """
    Function Name: writeDatatoBlockChain

    Function use: write the recieved Data to the Block-Chain with a specified amount amt charge
    """

    txid = subprocess.check_output(["flo-cli","--testnet", "sendtoaddress",receiver,str(amt),'""','""',"true","false","10",'UNSET',str(text)])
    txid = str(txid)
    txid = txid[2:-3]
    return txid

def readUnitFromBlockchain(txid):
    #Reads Unit Data from Block Chain
    rawtx = subprocess.check_output(["flo-cli","--testnet", "getrawtransaction", str(txid)])
    rawtx = str(rawtx)
    rawtx = rawtx[2:-3]
    tx = subprocess.check_output(["flo-cli","--testnet", "decoderawtransaction", str(rawtx)])
    content = json.loads(tx)
    text = content['floData']
    return text

def readDatafromBlockchain(cursor):
    #Read a Block of data from Blockchain
    text = []
    cursor_data = readUnitFromBlockchain(cursor)
    while(cursor_data[:5]=='next:'):
        cursor = cursor_data[5:69]
        #print("fetching this transaction->>"+cursor)
        text.append(cursor_data[70:])
        cursor_data = readUnitFromBlockchain(cursor)
    text.append(cursor_data)
    #print(text)
    text=('').join(text)
    return text
