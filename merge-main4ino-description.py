import json
import sys
merged = []
versionDescription = sys.argv[1]
jsonFiles = sys.argv[2:]
for f in jsonFiles:
    with open(f) as fi:
        j = json.load(fi)
        for jj in j['json']:
            merged.append(jj)
output={"versionDescription": sys.argv[1], "json": merged}
print(json.dumps(output))
