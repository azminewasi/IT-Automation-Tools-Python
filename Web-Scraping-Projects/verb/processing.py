with open('verb.txt', 'r') as f:
        lines = f.readlines()

pro=[]
for line in lines:
    data=line.split(":")[0].strip()
    pro.append(data)


with open('processed - verb.txt', 'w') as f2:
    for item in pro:
        f2.write("%s\n" % item)
        print(item)