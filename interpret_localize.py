import json
from collections import defaultdict 


## get <name coordination>
f = open("train.txt", "r")
info = f.readlines()
location = []
processed_train = []
for i in range(len(info)):
    name, location = info[i].split(' ')
    name = name.split('/')[-1]
    location = location.split(',')
    last_element = location.pop()
    last_element = int(last_element.split('\\')[0])
    temp = []
    for loc in location:
        temp.append(int(loc))
    temp.append(last_element)
    node = (name, temp)
    processed_train.append(node)

## process labels.json
with open("localize.json") as f:
    data = json.load(f)

## convert coordinations into labels
new_dict = defaultdict(list) 
for i in range(len(processed_train)):
    name, coord = processed_train[i]
    temp = ''
    index = coord[0]
    if index > 0:
        temp1 = data[str(index)]
        for element in temp1:
            new_dict[str(name)].append(element)

with open("train_localized.json", "w") as outfile:  
    json.dump(new_dict, outfile)