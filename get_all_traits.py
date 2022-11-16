import glob
from collections import Counter
import pandas as pd
from natsort import natsorted

image_path = '/Users/dimitrispanouris/Desktop/combination_list_2/images/'
rarity_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/rarity_files/'


def return_unique_tuple_items(itemlist: list) -> (list, list):
    primary_item = []
    secondary_item = []

    for i in range(len(itemlist)):
        primary_item.append(itemlist[i][0])
        if len(itemlist[i]) > 1:
            secondary_item.append(itemlist[i][1])
    bg_primary_unique = list(Counter(primary_item).keys())
    bg_secondary_unique = list(Counter(secondary_item).keys())
    return bg_primary_unique, bg_secondary_unique


def make_excel_with_number_of_traits_from_images():
    filelist = glob.glob(image_path + '*')
    filelist = natsorted(filelist)
    all_traits_files = []

    for file in filelist:
        traits_file_list = glob.glob(file + '/*')
        traits_file_list = natsorted(traits_file_list)
        all_traits_files.append(traits_file_list)

    _traits = []
    trait_names = []
    trait_nums = []

    for trait_file in all_traits_files:
        _traits.append(list(map(lambda x: x.split('/')[-1].split('-')[1].split('.')[0].split('_'), trait_file)))
    items_final = []

    backgrounds = _traits[0]
    bg_primary_unique, bg_secondary_unique = return_unique_tuple_items(backgrounds)
    items_final.append(
        {
            'trait': bg_primary_unique,
            'number': len(bg_primary_unique)
        }
    )
    items_final.append(
        {
            'trait': bg_secondary_unique,
            'number': len(bg_secondary_unique)
        }
    )
    print(bg_primary_unique)
    clothes = _traits[1]
    clothes_flat = [item for sublist in clothes for item in sublist]

    hair_back_list = _traits[2]
    hair_back, hair_color = return_unique_tuple_items(hair_back_list)

    hair_front_list = _traits[3]
    hair_front, _ = return_unique_tuple_items(hair_front_list)

    eyes_list = _traits[4]
    eyes, eyes_color = return_unique_tuple_items(eyes_list)
    mouth = ['Relaxed', 'Confused', 'Grinning', 'Afraid', 'Sad', 'Surprised', 'Yummy', 'Wicked', 'Sly', 'Scared',
             'Ahegao', 'Laugh', 'Disappointed', 'Happy', 'Melting', 'Smile', 'Confused', 'Tongue', 'Smirk', 'Scream',
             'Hehe', 'Nothing']

    body = _traits[6]
    hat_list = _traits[7]

    face = _traits[10]
    hands = ['Nothing'], ['Shy'], ['Love'], ['Heart'], ['Victory'], ['Axe'], ['Bow'], ['Fireball'], ['Katana'], ['Pistol'], ['Shrine'],['Rifle'],['Great Sword']

    effect = _traits[12]

    # df = pd.DataFrame(items_final)
    # df.to_excel(rarity_path + 'all_image_traits.xlsx', index=False)


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


make_excel_with_number_of_traits_from_images()
