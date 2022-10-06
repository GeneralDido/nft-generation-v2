from os import listdir
from os.path import isfile, join
from natsort import natsorted
import pyvips

PATH = '/Users/dimitrispanouris/Desktop/'


def make_list(path: str) -> list:
    path = PATH + path
    new_list = [f for f in listdir(path) if isfile(join(path, f))]
    filtered_list = filter(lambda item: item != '.DS_Store', new_list)
    return natsorted(filtered_list)


def combine_mouth_eyes(new_mouth: str, new_eyes: str, name: str):
    images = [
        pyvips.Image.new_from_file(PATH + 'mouth/' + new_mouth, access="sequential"),
        pyvips.Image.new_from_file(PATH + 'eyes/' + new_eyes, access="sequential")
    ]
    image = images[0].composite(images[1:], "over")
    image.write_to_file(
        PATH + 'moutheyes/' + f'{name}.png')


mouthList = make_list('mouth')
eyesList = make_list('eyes')

for mouth in mouthList:
    for eyes in eyesList:
        combine_mouth_eyes(mouth, eyes, str(mouth) + '_' + str(eyes))
