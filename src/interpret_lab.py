import json


## get <name coordination>
f = open("output/lists/localize/train.txt", "r")
info = f.readlines()
location = []
processed_train = []
for i in range(len(info)):
    name, location = info[i].split(' ')
    name = name.split('/')[-1]
    location = location.split(',')
    last_element = location.pop()
    last_element = int(last_element.split('\\')[0])
    # location[-1] = location[-1].split('\\')[0]
    # location.append(last_element)
    temp = []
    for loc in location:
        temp.append(int(loc))
    temp.append(last_element)
    # print (name, temp)
    node = (name, temp)
    processed_train.append(node)




## process localize.json

with open("../localize.json") as f:
    data = json.load(f)



