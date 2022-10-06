import glob
import os

PATH = '/Users/dimitris/Downloads/6-MouthEyes/*'
lst = glob.glob(PATH)
lst = sorted(lst)
for elem in lst:
    num = int(elem.split('/')[-1].split('-')[0])
    new_num = num-1
    print(num, new_num)
    os.rename(elem, '/Users/dimitris/Downloads/6-MouthEyes/' + str(new_num) + '-MouthEyes.png')

