import pandas as pd
import glob
from natsort import natsorted
PATH = '/Users/dimitrispanouris/Desktop/excel/Excel files/*'
OUT_PATH = '/Users/dimitrispanouris/Desktop/excel/final_combinations/'


lst = glob.glob(PATH)
lst = sorted(lst)
lst = natsorted(lst)
# print(lst)

#0 ['/Users/dimitris/Desktop/Excel files/00-Background Clothes.xlsx',
#1 '/Users/dimitris/Desktop/Excel files/04-Background MouthEyes.xlsx',
#2 '/Users/dimitris/Desktop/Excel files/09-Background Face.xlsx',
#3 '/Users/dimitris/Desktop/Excel files/10-ClothesHairBack.xlsx',
#4 '/Users/dimitris/Desktop/Excel files/011-Background Effect.xlsx',
#5 '/Users/dimitris/Desktop/Excel files/12-ClothesEyes.xlsx',
#6'/Users/dimitris/Desktop/Excel files/15-ClothesHatBack.xlsx',
#7 '/Users/dimitris/Desktop/Excel files/18-Clothes Face.xlsx',
#8 '/Users/dimitris/Desktop/Excel files/19-Clothes Hands.xlsx',
#9 '/Users/dimitris/Desktop/Excel files/20-HairBack HairFront.xlsx',
#10 '/Users/dimitris/Desktop/Excel files/21-HairBack Eyes.xlsx',
#11 '/Users/dimitris/Desktop/Excel files/24-HairBackHatBack.xlsx',
#12 '/Users/dimitris/Desktop/Excel files/27-HairBack Face.xlsx',
#13 '/Users/dimitris/Desktop/Excel files/33-HairFrontHatBack.xlsx',
#14 '/Users/dimitris/Desktop/Excel files/40-Eyes MouthEyes.xlsx',
#15 '/Users/dimitris/Desktop/Excel files/54-MouthEyes Face.xlsx',
#16 '/Users/dimitris/Desktop/Excel files/55-MouthEyes Hands.xlsx',
#17 '/Users/dimitris/Desktop/Excel files/56-MouthEyes Effect.xlsx',
#18 '/Users/dimitris/Desktop/Excel files/63-Body Face.xlsx',
#19 '/Users/dimitris/Desktop/Excel files/64-Body Hands.xlsx',
#20 '/Users/dimitris/Desktop/Excel files/70-HatBack HatMid.xlsx',
#21 '/Users/dimitris/Desktop/Excel files/71-HatBack HatFront.xlsx',
#22 '/Users/dimitris/Desktop/Excel files/72-HatBack Face.xlsx',
#23 '/Users/dimitris/Desktop/Excel files/74-HatBack Effect.xlsx',
#24 '/Users/dimitris/Desktop/Excel files/101-Face Effect.xlsx',
#25 '/Users/dimitris/Desktop/Excel files/110-Hands Effect.xlsx',
#26 '/Users/dimitrispanouris/Desktop/excel/Excel files/111-Hands HandsBack.xlsx']

names = {'BG': 0, 'Hat': 7, 'Hair': 2, 'Body': 6, 'Eyes': 4, 'MouthEyes': 5, 'Clothes': 1, 'HairFront': 3, 'Face': 10, 'Hands': 11 }


def make_array(df: pd.DataFrame, ) -> list:
    arr = []
    index = names[df.columns[0]]
    for i in range(df.shape[0]):
        inside_arr = []
        for j in range(df.shape[1] - 1):
            if df.iloc[[i]][j].values.item() == 1:
                inside_arr.append(j)
        arr.append([[index, i], inside_arr])
    return arr

hat0 = lst[0]
hat1 = lst[1]
hat2 = lst[2]
hat3 = lst[4]
# hat4 = lst[8]
# hat5 = lst[7]

dataframe = pd.read_excel(hat0)
dataframe2 = pd.read_excel(hat1)
dataframe3 = pd.read_excel(hat2)
dataframe4 = pd.read_excel(hat3)
# dataframe5 = pd.read_excel(hat4)
# dataframe6 = pd.read_excel(hat5)

k = make_array(dataframe)
knum = int(hat0.split('-')[0].split('/')[-1][1])
# knum = 1
# knum = 0

l = make_array(dataframe2)
lnum = int(hat1.split('-')[0].split('/')[-1][1])
# lnum = 1

m = make_array(dataframe3)
mnum = int(hat2.split('-')[0].split('/')[-1][1])

n = make_array(dataframe4)
# nnum = int(hat3.split('-')[0].split('/')[-1][1])
nnum = 11

# o = make_array(dataframe5)
# onum = int(hat4.split('-')[0].split('/')[-1][1])
#
# p = make_array(dataframe6)
# pnum = int(hat5.split('-')[0].split('/')[-1][1])


# print(k, knum)
# print(l, lnum)
# print(m, mnum)
# print(n, nnum)
# print(o, onum)
# print(p, pnum)

final_arr = []
for i in range(len(k)):

    newArr = [k[i][0]]
    for j in range(13):  # insert total items from current_item until last_item
        if j == knum:  # background: clothes-hands_back = 13, body: hat_back-hands_back = 7, hands: effect-hands_back= 2
            newArr.append(k[i][1])
        elif j == lnum:
            newArr.append(l[i][1])
        elif j == mnum:
            newArr.append(m[i][1])
        elif j == nnum:
            newArr.append(n[i][1])
        # elif j == onum:
        #     newArr.append(o[i][1])
        # elif j == pnum:
        #     newArr.append(p[i][1])
        else:
            newArr.append(1)
    final_arr.append(newArr)

print('---- -- -- - ---- ')
print(final_arr)

f = open(OUT_PATH + "5011-background_correct.txt", "a")
f.write(str(final_arr))
f.close()