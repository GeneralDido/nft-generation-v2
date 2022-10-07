import glob
from collections import Counter
import pandas as pd
from natsort import natsorted

image_path = '/Users/dimitrispanouris/Desktop/combination_list_2/images/'
rarity_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/rarity_files/'


def make_excel_with_number_of_traits_from_images():
    filelist = glob.glob(image_path + '*')
    filelist = natsorted(filelist)
    all_traits = []

    for file in filelist:
        all_traits.append(glob.glob(file + '/*'))

    _traits = []
    trait_names = []
    trait_nums = []

    for trait in all_traits:
        _traits.append(list(map(lambda x: x.split('/')[-1].split('-')[1].split('.')[0].split('_'), trait)))

    items_final = []
    for i in range(len(_traits)):
        trait1 = []
        trait2 = []
        for j in range(len(_traits[i])):
            trait1.append(_traits[i][j][0])
            if len(_traits[i][j]) > 1:
                trait2.append(_traits[i][j][1])

        trait1_unique = list(Counter(trait1).keys())
        items_final.append(
            {
             'trait': trait1_unique,
             'number': len(trait1_unique)
            }
        )
        if trait2:
            trait2_unique = list(Counter(trait2).keys())
            items_final.append(
                {
                    'trait': trait2_unique,
                    'number': len(trait2_unique)
                }
            )

    df = pd.DataFrame(items_final)
    df.to_excel(rarity_path + 'all_image_traits.xlsx', index=False)


def get_number_of_traits_in_excel_files():
    filenames = [
        'BG Primary.xlsx',
        'BG Secondary.xlsx',
        'Body.xlsx',
        'Clothes.xlsx',
        'Effect.xlsx',
        'Eyes Color.xlsx',
        'Eyes.xlsx',
        'Face.xlsx',
        'Hair Back.xlsx',
        'Hair Color.xlsx',
        'Hair Front.xlsx',
        'Hands.xlsx',
        'Hat.xlsx',
        'Mouth.xlsx',
    ]
    data = []
    for file in filenames:
        df = pd.read_excel(rarity_path + file, header=None)
        data.append({
            'trait': file,
            'number': len(df)
        })

    df = pd.DataFrame(data)
    df.to_excel(rarity_path + 'all_collection_traits.xlsx', index=False)
