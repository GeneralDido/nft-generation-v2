import pandas as pd
import numpy as np

rarity_path = '/Users/dimitrispanouris/Desktop/combination_list_2/output/rarity_files/'

''' Calculate Statistical Rarity - rarity.tools
    https://raritytools.medium.com/ranking-rarity-understanding-rarity-calculation-methods-86ceaeb9b98c
    NFTRarity = Sum(RarityScores[traits]), RarityScore[trait] = 1 / Trait Rarity of trait 
'''
df = pd.read_excel(rarity_path + 'nft_rarity_numbers.xlsx')
df['rarity_tools_include_num_traits'] = 1 / (df['BG Primary']) + 1 / (df['BG Secondary']) + 1 / (df['Clothes']) + 1 / (df['Hair Back']) + 1 / (df['Hair Front']) + 1 / (df['Hair Color']) + 1 / (df['Eyes']) + 1 / (df['Eyes Color']) + 1 / (df['Mouth']) + 1 / (df['Body']) + 1 / (df['Hat']) + 1 / (df['Face']) + 1 / (df['Hands']) + 1 / (df['Effect']) + 1 / (df['TraitCount'])
df['rarity_tools_no_num_traits'] = df['rarity_tools_include_num_traits'] - 1 / (df['TraitCount'])

df['rarity_tools_include_num_traits_rank'] = df['rarity_tools_include_num_traits'].rank(ascending=False)
df['rarity_tools_include_num_traits_rank_percentile'] = df['rarity_tools_include_num_traits'].rank(ascending=False, pct=True)

df['rarity_tools_no_num_traits_rank'] = df['rarity_tools_no_num_traits'].rank(ascending=False)
df['rarity_tools_no_num_traits_rank_percentile'] = df['rarity_tools_no_num_traits'].rank(ascending=False, pct=True)

''' Calculate OpenRarity
    https://openrarity.gitbook.io/developers/fundamentals/methodology
    NFTRarity = Sum(RarityScores[traits]), RarityScore[trait] = -log2(Trait Rarity of trait)
'''
df['open_rarity_include_num_traits'] = - np.log2(df['BG Primary']) - np.log2(df['BG Secondary']) - np.log2(df['Clothes']) - np.log2(df['Hair Back']) - np.log2(df['Hair Front']) - np.log2(df['Hair Color']) - np.log2(df['Eyes']) - np.log2(df['Eyes Color']) - np.log2(df['Mouth']) - np.log2(df['Body']) - np.log2(df['Hat']) - np.log2(df['Face']) - np.log2(df['Hands']) - np.log2(df['Effect']) - np.log2(df['TraitCount'])
df['open_rarity_no_traits'] = df['open_rarity_include_num_traits'] + np.log2(df['TraitCount'])

df['open_rarity_include_num_traits_rank'] = df['open_rarity_include_num_traits'].rank(ascending=False)
df['open_rarity_include_num_traits_rank_percentile'] = df['open_rarity_include_num_traits'].rank(ascending=False, pct=True)

df['open_rarity_no_traits_rank'] = df['open_rarity_no_traits'].rank(ascending=False)
df['open_rarity_no_traits_rank_percentile'] = df['open_rarity_no_traits'].rank(ascending=False, pct=True)

''' Calculate Normalized Statistical Rarity
    https://howrare.is/faq
    NFTRarity = 1 / (count of occurrences for the attribute / count of most popular attribute in a trait 
'''
df['normalized_rarity'] = 1 / (df['BG Primary'] / df['BG Primary_max']) + 1 / (df['BG Secondary'] / df['BG Secondary_max']) + 1 / (df['Clothes'] / df['Clothes_max']) + 1 / (df['Hair Back'] / df['Hair Back_max']) + 1 / (df['Hair Front'] / df['Hair Front_max']) + 1 / (df['Hair Color'] / df['Hair Color_max']) + 1 / (df['Eyes'] / df['Eyes_max']) + 1 / (df['Eyes Color'] / df['Eyes Color_max']) + 1 / (df['Mouth'] / df['Mouth_max']) + 1 / (df['Body'] / df['Body_max']) + 1 / (df['Hat'] / df['Hat_max']) + 1 / (df['Face'] / df['Face_max']) + 1 / (df['Hands'] / df['Hands_max']) + 1 / (df['Effect'] / df['Effect_max']) + 1 / (df['TraitCount'] / df['TraitCount_max'])
df['normalized_rarity_rank'] = df['normalized_rarity'].rank(ascending=False)
df['normalized_rarity_rank_percentile'] = df['normalized_rarity'].rank(ascending=False, pct=True)


''' Calculate Absolute statistical Rarity
    https://moonrank.app/faq
    We take the % rarity of each value and multiply it together to get the absolute statistical rarity.
'''
df['absolute_rarity'] = df['BG Primary'] * df['BG Secondary'] * df['Clothes'] * df['Hair Back'] * df['Hair Front']  * df['Hair Color'] * df['Eyes'] * df['Eyes Color'] * df['Mouth'] * df['Body'] * df['Hat'] * df['Face'] * df['Hands'] * df['Effect'] * df['TraitCount'] * 100000000000000000
df['absolute_rarity_rank'] = df['absolute_rarity'].rank(ascending=True)
df['absolute_rarity_rank_percentile'] = df['absolute_rarity'].rank(ascending=True, pct=True)

df.to_excel(rarity_path + 'nft_rarity_final.xlsx', index=False)
