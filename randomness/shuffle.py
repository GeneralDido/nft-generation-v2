import random
# original code from: https://stackoverflow.com/questions/57340713/how-do-i-un-shuffle-a-list-back-to-its-original-form


def get_permutation(_list: list, _seed: int) -> list:
    random.seed(_seed)
    perm = list(range(len(_list)))
    random.shuffle(perm)
    random.seed()  # optional, in order to not impact other code based on random
    return perm


def shuffle(_list: list, _seed: int):  # [1, 2, 3, 4]
    perm = get_permutation(_list, _seed)  # [3, 2, 1, 0]
    _list[:] = [_list[j] for j in perm]  # [4, 3, 2, 1]


def un_shuffle(_list: list, _seed: int):  # [4, 3, 2, 1]
    perm = get_permutation(_list, _seed)  # [3, 2, 1, 0]
    result = [None] * len(_list)  # [None, None, None, None]
    for i, j in enumerate(perm):
        result[j] = _list[i]
    _list[:] = result  # [1, 2, 3, 4]


''' 
Example
alist = [1, 2, 3, 4]
print(alist)

shuffle(alist, sum(alist))
print(alist)

un_shuffle(alist, sum(alist))
print(alist)
'''
