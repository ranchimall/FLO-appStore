import json
with open('AppData.json',encoding='utf-8') as F:
     json_data=json.loads(F.read())
print(json_data["Dapps"][0]["id"])

