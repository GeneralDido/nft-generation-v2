import pandas as pd
import glob
from natsort import natsorted

IN_PATH = '/Users/dimitrispanouris/Desktop/excel/Excel files/'
OUT_PATH = '/Users/dimitrispanouris/Desktop/excel/reverted/'


def reverse_excel_file(file_lst: list):
    for file in file_lst:
        filename = file.split('/')[-1]
        df = pd.read_excel(IN_PATH + filename)
        df2 = df.T
        df2.to_excel(OUT_PATH + filename)


lst = glob.glob(IN_PATH + '*')
lst = sorted(lst)
lst = natsorted(lst)
reverse_excel_file(lst)