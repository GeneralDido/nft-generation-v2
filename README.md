# How to use

## Folder Structure

Store all traits in folder `images/`, each trait in a different subfolder.
Example sub-folder structure (starts from index 1):

```
1-background
2-clothes
3-hair-back
... 
```
Each image in the sub-folder starts from index 0, example:
```
0-Field Dawn
1-Field Night
2-Field Day
3-Field Day_Rainbow
... 
```
Notice the `_` in the name, indicates that this trait has two sub-traits, in this case `BG Primary` and `BG Secondary`. In this example `Field Day` and `Rainbow` are two distinct traits.

The `output` folder structure is the following:
```
json_files   # json metadata of image
png_files    # png of image
rarity_files # rarity calculations of collection/image
txt_files    # keeps the "dna" of the image
```

## Image Combinations

### Step 1
Before running the program, we develop the combinations. In order to do this, we use the Excel files from the corresponding folder. 

Each file is named in specific way: `00-Background Clothes` means we develop combinations for Background and Clothes, the first 0 indicates the first trait, example: 
```
0: Background, 1: Clothes, 2: Hairback, ...
```
The second 0 indicates the first trait of the remaining traits. Example:
```
For Background, the remaining traits are:
[Clothes, HairBack, HairFront, Eyes, MouthEyes, ...]
Then:
0: Clothes, 1: HairBack, 2: HairFront, ...
```

See the Excel file structure as example on how to develop the combinations. Generally, 0 means the combination in (x,y) is not allowed, 1: the combination is allowed.

### Step 2
We need to generate the files in `final_combinations/`. To do this, we use the `make_array.py` 
[script is not optimized, so some manual work is currently required].

First we get all excel files from `Excel files/`, and we only combine the results for each trait in order to generate a file for all the combinations for that particular trait.

For example, for `Background`, we develop combinations with `Clothes`, `MouthEyes`, `Face`, `Effect`.
In this example, we need files #0, #1, #2, #4. We use those files for the vars `hat, ...` and `dataframe, ...`. 

The nums `k, l, m, ...` are the numbers for the trait, in this example:
```
k: Clothes = 0
l: MouthEyes = 4
m: Face = 9
n: Effect = 11
```
If a number is 2 digits, we define it directly, as in `n`in this example.

Then in line 103 we first insert the correct number of iterations, which is the total items from current_item until last_item. In the example of Background, we have 13 remaining traits.

In the other lines we insert `knum, lnum, ...` and run the program.

The program will generate the file for that particular trait and all allowed combinations for that trait. In this example, it will produce all allowed combinations for Background. We follow the same procedure for all combinations to develop all files.

### Step 3

We insert all files from `final_combinations/` to `item_generator.py`. Be careful on the final array you construct, check example in the file.

We then run the program and generate all combinations in `combinations.txt`. 

We also generate all other data about the files. We copy all those files in `items.py`. 

### Step 4
In `items.py` we first develop the correct `allow_combinations_help`. Example:
```
allow_combinations_help = [[0, 0, [1, 2, 3, 5, 6, 7, 8, 10, 12]],
                           [1, 0, [1, 3, 4, 6, 7, 10, 11]],
                           [2, 0, [2, 3, 5, 6, 8, 9, 10]],
                           [3, 0, [0, 1, 2, 4, 5, 6, 7, 8, 9]],
                           [4, 0, [1, 2, 3, 4, 5, 6, 7, 8]],
                           [5, 0, [0, 1, 2, 3, 7]],
                           [6, 0, [0, 1, 2, 5, 6]],
                           [7, 0, [3, 5]],
                           [8, 1, [0, 1, 2, 3, 4]],
                           [9, 1, [0, 1, 2, 3]],
                           [10, 0, [0, 2]],
                           [11, 0, []],
                           [12, 1, [0]]]
```
The first item in each subarray is the current trait, in this example:
```
0: Background
1: Clothes
2: Hair Back
...
```
The second item is a boolean value, meaning if all combinations are allowed for that trait. If yes, then the value = 1, else value = 0.

The third item is a list of all other remaining traits after that trait, starting from index 0. If we don't allow all combinations, we remove the index in the array.

In the previous example, we allow only specific combinations for `Background` and `Clothes`, `MouthEyes`, `Face`, `Effect`. This means we remove indexes: 0, 4, 9, 11.

We do the same for all other traits and lists.

This was made to optimize the speed of searching for the program (it only searches for a combinations if not all combinations are allowed).

### Step 5

In the same file, `items.py`, you can now change the rarity values of the traits. The rarities are the third element in the list for each trait. 

For example, if `Nothing` in `Effect` should have a higher probability than the other traits, you can increase this. Zero probabilities, i.e. item never exists in the output, are also possible.

### Step 6

In `generate_collection.py` we specify all attributes from `items.py` and we use them to generate unique images. We change `total_items` for the total items of the collection. 

Important is `final_list`, which is the final list that will be rendered/generated by the program. It is better to have matching traits together when making the folder structure and running the program, and then use a specific way to render the images. For this example, `hair_back` and `hair_front` are very close to each other folder/structure wise, because they fit together and is easier to search for the program, but when we render the final image, `hair_back` renders many layers before `hair_front`.

If everything is defined correctly, the program should begin developing images!

## Rarity Generation

For Rarity, we have used different algorithms, most notably OpenRarity as well as other methods. 

### Step 1
We first use `rarity_files_constructor.py`. We define the paths, data, collection_size. Then run the program, and it will construct all general rarities for the collection, based on each trait and the occurrences for each trait. 

It will also construct `nft_rarities.xlsx` and `nft_rarity_numbers.xlsx`, which are stats for each NFT, either as raw data or as numbers.

### Step 2

We use `rarity_calculator.py` to develop all rarities for the collection. The `nft_rarity_final.xlsx` includes the rarities. 

The most important rarity value is: `open_rarity_include_num_traits`.