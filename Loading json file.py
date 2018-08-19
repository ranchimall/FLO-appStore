import json
with open('AppData.json',encoding='utf-8') as F:
     json_data=json.loads(F.read())

for app in json_data["Dapps"]:
	print(app["name"])

