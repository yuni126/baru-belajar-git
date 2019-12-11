#membuat json
import json

data = {"nama": "Yuni Kurniawati", "jurusan":"statistika","hobby": ["nonton", "main"]}

with open('orang2.json', 'w') as json_file:
  json.dump(data, json_file)