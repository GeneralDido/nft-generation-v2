import base64
from PIL import Image
from io import BytesIO

PATH = rarity_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/png_files/'

with open(PATH + "0.png", "rb") as image_file:
    data = base64.b64encode(image_file.read())

print(data)

text_file = open("/Users/dimitrispanouris/Desktop/combination_list_2/output/test.txt", "w")
text_file.write(data.decode('utf-8'))
text_file.close()
