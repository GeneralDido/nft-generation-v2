import json
import names


def map_mouth_eyes(mouth_eyes: str) -> str:
    mouth_eyes_num = int(mouth_eyes.split('/')[-1].split('-')[0])

    match mouth_eyes_num:
        case num if num <= 31:
            return 'Relaxed'
        case num if 32 <= num <= 87:
            return 'Confused'
        case num if 88 <= num <= 135:
            return 'Grinning'
        case num if 136 <= num <= 191:
            return 'Afraid'
        case num if 192 <= num <= 239:
            return 'Sad'
        case num if 240 <= num <= 287:
            return 'Surprised'
        case num if 288 <= num <= 335:
            return 'Yummy'
        case num if 336 <= num <= 375:
            return 'Wicked'
        case num if 376 <= num <= 439:
            return 'Sly'
        case num if 440 <= num <= 495:
            return 'Scared'
        case num if 496 <= num <= 519:
            return 'Ahegao'
        case num if 520 <= num <= 583:
            return 'Laugh'
        case num if 584 <= num <= 639:
            return 'Disappointed'
        case num if 640 <= num <= 703:
            return 'Happy'
        case num if 704 <= num <= 759:
            return 'Melting'
        case num if 760 <= num <= 815:
            return 'Smile'
        case num if 816 <= num <= 871:
            return 'Confused'
        case num if 872 <= num <= 935:
            return 'Tongue'
        case num if 936 <= num <= 999:
            return 'Smirk'
        case num if 1000 <= num <= 1055:
            return 'Scream'
        case num if 1056 <= num <= 1111:
            return 'Hehe'
        case _:
            return 'Nothing'


def generate_json(number: int, characteristics: dict, address: str):
    def append_attribute(trait_type: str, trait_value: str):
        data["attributes"].append(
            {
                "trait_type": trait_type,
                "value": trait_value,
            }
        )

    name = names.get_full_name(gender='female')
    data = {"name": f"CryptoGirl #{number} {name}", "symbol": "CGP", "description": "Meet the crypto girl party.",
            "seller_fee_basis_points": 500, "image": f"{number}.png", "external_url": "", "edition": "2022",
            "attributes": []}

    traits = []

    for key, value in characteristics.items():
        traits.append(value.split('/')[-1].split('-')[1].split('.')[0])

    bg_list = traits[0].split('_')

    bg_primary = bg_list[0]
    bg_secondary = bg_list[1] if len(bg_list) > 1 else 'Nothing'

    hair_back_list = traits[2].split('_')
    if hair_back_list[0] == 'Nothing':
        hair_back = 'Nothing'
        hair_color = 'Nothing'
    else:
        hair_back = hair_back_list[0]
        hair_color = hair_back_list[1]

    hair_front = traits[3].split('_')[0]

    eyes_list = traits[4].split('_')
    eyes = eyes_list[0]
    eyes_color = eyes_list[1]

    append_attribute('BG Primary', bg_primary)

    if bg_secondary != 'Nothing':
        append_attribute('BG Secondary', bg_secondary)

    append_attribute('Clothes', traits[1])

    if hair_back != 'Nothing':
        append_attribute('Hair Back', hair_back)
        append_attribute('Hair Front', hair_front)
        append_attribute('Hair Color', hair_color)

    append_attribute('Eyes', eyes)

    append_attribute('Eyes Color', eyes_color)

    append_attribute('Mouth', map_mouth_eyes(characteristics['mouth_eyes']))

    append_attribute('Body', traits[6])

    if traits[7] != 'Nothing':
        append_attribute('Hat', traits[7])

    if traits[10] != 'Nothing':
        append_attribute('Face', traits[10])

    if traits[11] != 'Nothing':
        append_attribute('Hands', traits[11])

    if traits[12] != 'Nothing':
        append_attribute('Effect', traits[12])

    data["attributes"].append(
        {"display_type": "number", "trait_type": "generation", "value": 1}
    )
    data["attributes"].append(
        {"display_type": "number", "trait_type": "sequence", "value": number}
    )

    data["properties"] = {}
    data["properties"]["category"] = "image"

    data["properties"]["files"] = []
    data["properties"]["files"].append({"uri": "", "type": "image/png"})
    data["properties"]["creators"] = []
    data["properties"]["creators"].append({"address": address, "share": 100})

    with open("output/json_files/" + f"{number}.json", "w") as outfile:
        json.dump(data, outfile)
