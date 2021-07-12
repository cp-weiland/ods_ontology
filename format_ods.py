import json

with open("ods.json.owl") as jsonFile:
    parsed = json.load(jsonFile)
    jsonFile.close()
    
print(json.dumps(parsed, indent=4, sort_keys=True))
