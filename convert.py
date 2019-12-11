import sys
import json

out = open("targets_data.json", "w")

data = {
    "beatDuration" : 0.3,
    "sliderMultiplier" : 1.4,
    "targets":[]
}

timing = False
notes = False

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line[:-1]

        if line.startswith('SliderMultiplier'):
            try:
                data["sliderMultiplier"] = float(line.split(":")[1])
            except:
                continue
        if line == "[TimingPoints]":
            timing = True
            notes = False
            continue
        if line == "[HitObjects]":
            timing = False
            notes = True
            continue
        if notes:
            if line:
                parts = line.split(",")
                if not ('{0:08b}'.format(int(parts[3])))[4] == '1':
                    data["targets"].append(line)
            continue
        if timing:
            parts = line.split(",")
            try:
                if float(parts[1]) > 0:                
                    data["beatDuration"] = float(parts[1])/1000
                    timing = False
            except:
                continue

json.dump(data,out)
        
