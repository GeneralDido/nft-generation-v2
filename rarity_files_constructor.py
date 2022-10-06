import glob
import json
from natsort import natsorted
from collections import Counter
import pandas as pd
from operator import itemgetter

json_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/json_files/'
rarity_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/rarity_files/'

filelist = glob.glob(json_path + '*')
filelist = natsorted(filelist)

data = {
    'BG Primary': [],
    'BG Secondary': [],
    'Clothes': [],
    'Hair Back': [],
    'Hair Front': [],
    'Hair Color': [],
    'Eyes': [],
    'Eyes Color': [],
    'Mouth': [],
    'Body': [],
    'Hat': [],
    'Face': [],
    'Hands': [],
    'Effect': [],
    'TraitCount': []
}

for file in filelist:
    with open(file) as f:
        trait_data = json.load(f)
    attributes = trait_data['attributes'][:-2]
    trait_count = 0
    for key in data:
        trait_list = list(filter(lambda attribute: attribute['trait_type'] == key, attributes))
        if key == 'TraitCount':
            data[key].append(trait_count)
        elif trait_list:
            data[key].append(trait_list[0]['value'])
            trait_count += 1
        else:
            data[key].append('Nothing')

collection_size = 1000

all_traits = []

# construct general Excel files for average rarity of each trait
for trait in data:
    counts = Counter(data[trait])
    trait_data = []
    for key, value in counts.items():
        trait_data.append((key, value / collection_size, value))
    pd.DataFrame(trait_data).to_excel(rarity_path + trait + '.xlsx', header=False, index=False)
    all_traits.append(trait_data)

# construct two Excel files with all rarities per NFT as text (nft_rarities.xlsx) and numbers (nft_rarity_numbers.xlsx)
data_list = []
for key in data:
    data_list.append(data[key])

df_list = []
for i in range(collection_size):
    df_list.append({
        'NFT num': i,
        'BG Primary': data_list[0][i],
        'BG Secondary': data_list[1][i],
        'Clothes': data_list[2][i],
        'Hair Back': data_list[3][i],
        'Hair Front': data_list[4][i],
        'Hair Color': data_list[5][i],
        'Eyes': data_list[6][i],
        'Eyes Color': data_list[7][i],
        'Mouth': data_list[8][i],
        'Body': data_list[9][i],
        'Hat': data_list[10][i],
        'Face': data_list[11][i],
        'Hands': data_list[12][i],
        'Effect': data_list[13][i],
        'TraitCount': data_list[14][i],
    })

df = pd.DataFrame(df_list)
df.to_excel(rarity_path + 'nft_rarities.xlsx', index=False)

max_trait_occurrence = []  # returns a tuple of the most popular attribute in a trait, example: ('City Neon', 0.071, 71)
for i in range(len(all_traits)):
    max_trait_occurrence.append(max(all_traits[i], key=itemgetter(1)))

rarity_num_list = []
for i in range(collection_size):
    rarity_num_list.append({
        'NFT num': i,
        'BG Primary': [v[1] for k, v in enumerate(all_traits[0]) if v[0] == data_list[0][i]][0],
        'BG Secondary': [v[1] for k, v in enumerate(all_traits[1]) if v[0] == data_list[1][i]][0],
        'Clothes': [v[1] for k, v in enumerate(all_traits[2]) if v[0] == data_list[2][i]][0],
        'Hair Back': [v[1] for k, v in enumerate(all_traits[3]) if v[0] == data_list[3][i]][0],
        'Hair Front': [v[1] for k, v in enumerate(all_traits[4]) if v[0] == data_list[4][i]][0],
        'Hair Color': [v[1] for k, v in enumerate(all_traits[5]) if v[0] == data_list[5][i]][0],
        'Eyes': [v[1] for k, v in enumerate(all_traits[6]) if v[0] == data_list[6][i]][0],
        'Eyes Color': [v[1] for k, v in enumerate(all_traits[7]) if v[0] == data_list[7][i]][0],
        'Mouth': [v[1] for k, v in enumerate(all_traits[8]) if v[0] == data_list[8][i]][0],
        'Body': [v[1] for k, v in enumerate(all_traits[9]) if v[0] == data_list[9][i]][0],
        'Hat': [v[1] for k, v in enumerate(all_traits[10]) if v[0] == data_list[10][i]][0],
        'Face': [v[1] for k, v in enumerate(all_traits[11]) if v[0] == data_list[11][i]][0],
        'Hands': [v[1] for k, v in enumerate(all_traits[12]) if v[0] == data_list[12][i]][0],
        'Effect': [v[1] for k, v in enumerate(all_traits[13]) if v[0] == data_list[13][i]][0],
        'TraitCount': [v[1] for k, v in enumerate(all_traits[14]) if v[0] == data_list[14][i]][0],
        'BG Primary_max': max_trait_occurrence[0][1],
        'BG Secondary_max': max_trait_occurrence[1][1],
        'Clothes_max': max_trait_occurrence[2][1],
        'Hair Back_max': max_trait_occurrence[3][1],
        'Hair Front_max': max_trait_occurrence[4][1],
        'Hair Color_max': max_trait_occurrence[5][1],
        'Eyes_max': max_trait_occurrence[6][1],
        'Eyes Color_max': max_trait_occurrence[7][1],
        'Mouth_max': max_trait_occurrence[8][1],
        'Body_max': max_trait_occurrence[9][1],
        'Hat_max': max_trait_occurrence[10][1],
        'Face_max': max_trait_occurrence[11][1],
        'Hands_max': max_trait_occurrence[12][1],
        'Effect_max': max_trait_occurrence[13][1],
        'TraitCount_max': max_trait_occurrence[14][1],
    })

df = pd.DataFrame(rarity_num_list)
df.to_excel(rarity_path + 'nft_rarity_numbers.xlsx', index=False)
