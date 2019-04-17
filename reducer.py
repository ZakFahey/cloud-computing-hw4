#!/usr/bin/env python
import sys
import json

result = {}

for line in sys.stdin:
    frequencies = json.loads(line)
    for key in frequencies.keys():
        if key not in result:
            result[key] = 0
        result[key] += frequencies[key]

print(json.dumps(result))