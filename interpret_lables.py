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
with open("labels.json") as f:
    data = list(json.load(f))


## convert coordinations into labels
interpreted = []
new_dict = defaultdict(list) 
# f = open("train_labeled.txt", "w")
for i in range(len(processed_train)):
    name, coord = processed_train[i]
    temp = ''
    for index in coord:
        new_dict[name].append(data[index])

with open("train_labeled.json", "w") as outfile:  
    json.dump(new_dict, outfile)