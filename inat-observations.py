import pandas as pd
data = pd.read_csv('C:\\Users\\User\\Documents\\Python\\observations.csv')

for taxon in data.columns:
    taxon_name = taxon.split('_')[1]
    dict = {}
    for taxon in data[taxon]:
        if type(taxon) != str:
            continue
        dict[taxon] = dict.get(taxon, 0) + 1
    
    list = []
    for (key, count) in dict.items():
        list.append((count, key))
    list = sorted(list, reverse = True)
    
    print(taxon_name+':', len(dict), '\nmost popular:', list[0], '\n')
