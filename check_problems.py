import json
import pandas as pd
import glob
from natsort import natsorted

JSON_PATH = '/Users/dimitrispanouris/Desktop/combination_list_2/output/'
EXCEL_PATH = '/Users/dimitrispanouris/Desktop/excel/Excel files/'
OUT_PATH = '/Users/dimitrispanouris/Desktop/combination_list_2/'

'''
 attributes_array:
     0: background
     1: clothes
     2: hair_back
     3: hair_front
     4: eyes
     5: MouthEyes
     6: body
     7: hat_back
     8: hat_mid
     9: hat_front
     10: face
     11: hands
     12: effect
     13: hands_back
'''


def get_items_from_path(path: str) -> list:
    items_list = glob.glob(path + '*.xlsx') + glob.glob(path + '*.json')
    return natsorted(items_list)


def get_attribute_number(attr: dict) -> int:
    return int(attr.get('value').split('/')[-1].split('-')[0])


def make_attributes_array_from_json(filename: str) -> list:
    with open(filename) as file:
        data = json.load(file)
    attributes_dict = data.get('attributes')
    attributes_array = []
    for i in range(14):
        attributes_array.append(get_attribute_number(attributes_dict[i]))
    return attributes_array


def make_df_list() -> list:
    lst = get_items_from_path(EXCEL_PATH)  # list sequence same as in make_array.py
    new_df_list = []
    for excel_file in lst:
        new_df_list.append(pd.read_excel(EXCEL_PATH + excel_file.split('/')[-1], sheet_name=0))
    return new_df_list


df_list = make_df_list()
json_list = get_items_from_path(JSON_PATH)
check_problems_list = []

for json_file in json_list:
    attributes = make_attributes_array_from_json(json_file)

    json_file_attribute = {
        'json_file': json_file.split('/')[-1],
        'bg-clothes': df_list[0].iloc[attributes[0]][attributes[1]],
        'bg-mouthEyes': df_list[1].iloc[attributes[0]][attributes[5]],
        'bg-face': df_list[2].iloc[attributes[0]][attributes[10]],
        'bg-effect': df_list[4].iloc[attributes[0]][attributes[12]],
        'clothes-hairBack': df_list[3].iloc[attributes[1]][attributes[2]],
        'clothes-eyes': df_list[5].iloc[attributes[1]][attributes[4]],
        'clothes-hatBack': df_list[6].iloc[attributes[1]][attributes[7]],
        'clothes-face': df_list[7].iloc[attributes[1]][attributes[10]],
        'clothes-hands': df_list[8].iloc[attributes[1]][attributes[11]],
        'hairBack-hairFront': df_list[9].iloc[attributes[2]][attributes[3]],
        'hairBack-eyes': df_list[10].iloc[attributes[2]][attributes[4]],
        'hairBack-hatBack': df_list[11].iloc[attributes[2]][attributes[7]],
        'hairBack-face': df_list[12].iloc[attributes[2]][attributes[10]],
        'hairFront-hatBack': df_list[13].iloc[attributes[3]][attributes[7]],
        'eyes-mouthEyes': df_list[14].iloc[attributes[4]][attributes[5]],
        'mouthEyes-face': df_list[15].iloc[attributes[5]][attributes[10]],
        'mouthEyes-hands': df_list[16].iloc[attributes[5]][attributes[11]],
        'mouthEyes-effect': df_list[17].iloc[attributes[5]][attributes[12]],
        'body-face': df_list[18].iloc[attributes[6]][attributes[10]],
        'body-hands': df_list[19].iloc[attributes[6]][attributes[11]],
        'hatBack-hatMid': df_list[20].iloc[attributes[7]][attributes[8]],
        'hatBack-hatFront': df_list[21].iloc[attributes[7]][attributes[9]],
        'hatBack-face': df_list[22].iloc[attributes[7]][attributes[10]],
        'hatBack-effect': df_list[23].iloc[attributes[7]][attributes[12]],
        'face-effect': df_list[24].iloc[attributes[10]][attributes[12]],
        'hands-effect': df_list[25].iloc[attributes[11]][attributes[12]],
        'hands-handsBack': df_list[26].iloc[attributes[11]][attributes[13]],
    }

    check_problems_list.append(json_file_attribute)
final_df = pd.DataFrame(check_problems_list)
final_df.to_excel(OUT_PATH + 'check_problems.xlsx')
