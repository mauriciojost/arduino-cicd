import json
import sys
merged = []
for f in sys.argv[1:]:
    with open(f) as fi:
        j = json.load(fi)
        for jj in j['json']:
            merged.append(jj)
output={"json": merged}
print(json.dumps(output))
