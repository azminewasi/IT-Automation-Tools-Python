with open('noun.txt', 'r') as f:
        lines = f.readlines()


res = []
for i in lines:
    if i.strip() not in res:
        res.append(i.strip())

with open('processed - noun.txt', 'w') as f2:
    for item in res:
        f2.write("%s\n" % item)
        print(item)