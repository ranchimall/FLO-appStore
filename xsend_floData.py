import subprocess
import json

address = 'oXa7t72t3CgnR11ycxVfdupz55eucHufHj'
toAddress = 'ocZXNtzpiUqBvzQorjAKmZ5MhXxGTLKeSH'


process = subprocess.Popen(['flo-cli','-testnet','listunspent','1','9999999','["'+address+'"]'], stdout=subprocess.PIPE)
unspent = json.loads(process.communicate()[0].decode())

print("Enter floData :")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
floData = '\n'.join(lines)
try:
	floData=str(json.loads(floData))
except:
	None
print('floData='+floData)

print(len(unspent))
for i in range(len(unspent)):
	print('\n'+str(i)+':'+str(unspent[i]['amount']))
	if(unspent[i]['spendable'] and unspent[i]['amount']>0.01005):
		txid = unspent[i]['txid']
		amount = unspent[i]['amount']
		print(txid)
		print(amount)

		process = subprocess.Popen(['flo-cli','-testnet','createrawtransaction','[{"txid":"'+txid+'", "vout":0}]','{"'+toAddress+'":0.01, "'+address+'":'+str(round(amount-0.01005,7))+'}','0','false','"'+floData+'"'], stdout=subprocess.PIPE)
		createHash = process.communicate()[0].decode().strip()
		print(createHash)

		process = subprocess.Popen(['flo-cli','-testnet','signrawtransaction',createHash], stdout=subprocess.PIPE)
		sign = json.loads(process.communicate()[0].decode())
		print(sign)

		if(not sign['complete']):
			print("Failed to sign transaction : "+sign['errors'][0]['error'])
			continue

		process = subprocess.Popen(['flo-cli','-testnet','sendrawtransaction',sign['hex']], stdout=subprocess.PIPE)
		newtxid = str(process.communicate()[0].decode())
		print(newtxid)
		if(newtxid):
			break







