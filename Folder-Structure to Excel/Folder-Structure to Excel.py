import os
import pprint


def path_to_dict(path, d):

    name = os.path.basename(path)
    if os.path.isdir(path):
        if name not in d['dirs']:
            d['dirs'][name] = {'dirs':{},'files':[]}
        for x in os.listdir(path):
            if x[0]==".":
                continue
            path_to_dict(os.path.join(path,x), d['dirs'][name])
    else:
        d['files'].append(name)
    return d


mydict = path_to_dict('./', d = {'dirs':{},'files':[]})


import pandas as pd

df = pd.DataFrame(mydict)

normalized = pd.json_normalize(df['col'])

# join the normalized column to df
df = df.join(normalized).drop(columns=['col'])

print(df)