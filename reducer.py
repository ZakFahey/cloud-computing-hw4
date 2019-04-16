import sys
import json

result = {}

for line in sys.stdin:
    frequencies = json.loads(line)
    for key, val in frequencies.__dict__.iteritems():
        if key not in result:
            result[key] = 0
        result[key] += val

print(json.dumps(result))