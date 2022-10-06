import pyvips
import items
from item_generator import attribute_names
from dna_generator import DnaGenerator
from generate_json_solana import generate_json

attributes = [
    items.background,
    items.clothes,
    items.hair_back,
    items.hair_front,
    items.eyes,
    items.mouth_eyes,
    items.body,
    items.hat_back,
    items.hat_mid,
    items.hat_front,
    items.face,
    items.hands,
    items.effect,
    items.hands_back
]

total_items = 1000


def make_dna_file(num: int, characteristic_list: list):
    characteristic_nums = list(map(lambda x: int(x.split('/')[-1].split('-')[0]), characteristic_list))
    with open("output/txt_files/" + f"{str(num)}.txt", 'w') as outfile:
        outfile.write(str(characteristic_nums))


def generate_collection(num_items: int) -> None:
    new_character = DnaGenerator(
        attributes,
        attribute_names,
        items.dna_to_create,
        items.allow_combinations_help,
        items.allow_list,
    )
    for i in range(num_items):

        not_found_dna = True

        while not_found_dna:
            try:
                characteristic = new_character.make_dna()
                not_found_dna = False
            except:
                not_found_dna = True

        image_list = []
        for j in range(len(attributes)):
            image_list.append(new_character.dna_traits_list[i][j])

        final_list = [
            image_list[0],
            image_list[13],
            image_list[7],
            image_list[2],
            image_list[6],
            image_list[5],
            image_list[1],
            image_list[10],
            image_list[8],
            image_list[3],
            image_list[9],
            image_list[11],
            image_list[12],
        ]

        images = [
            pyvips.Image.new_from_file(filename, access="sequential")
            for filename in final_list
        ]

        image = images[0].composite(images[1:], "over")


        print(i, characteristic)
        generate_json(
            i, characteristic[0], address="nZgsTL8MUK5xVtFDDEdkv55AsX15vQ6saA6FpfWbh7a"  # ---> this should change, I return two things now from make_dna
        )
        image.write_to_file(
            "output/png_files/" + f"{i}.png")
        make_dna_file(i, characteristic[1])


generate_collection(total_items)
