import random


class DnaGenerator:
    """
    dna_list: list of all dna's
    dna_traits_list: list of all dna traits
    list_of_characteristics: list of characteristics to include
    dna_to_create: list of dna's that should be created from the start
    dna_to_create_counter: counter for dna_to_create in items.py
    attribute_names: list of str with the names of the main characteristics, ["background", "hair_back", ...]
    combinations_helper: helps to remove complexity in allowed_combinations method.
    allow_list: main list to allow or not, check allowed_combinations method
    """

    dna_list: list
    dna_traits_list: list
    list_of_characteristics = list
    dna_to_create = list
    dna_to_create_counter: int
    attribute_names: list
    combinations_helper: list
    allow_list: list

    def __init__(
        self,
        list_of_characteristics: list,
        attribute_names: list,
        dna_to_create: list,
        combinations_helper: list,
        allow_list: list,
    ):
        self.dna_list = []
        self.dna_traits_list = []
        self.dna_to_create_counter = 0
        self.list_of_characteristics = list_of_characteristics
        self.dna_to_create = dna_to_create
        self.combinations_helper = combinations_helper
        self.attribute_names = attribute_names
        self.allow_list = allow_list

    @staticmethod
    def make_random_choice(characteristic: list) -> list:
        """ Get random item from a list of characteristics (example: eye) based on rarity score (elem: 2) """
        characteristic_values = [el[1] for el in characteristic]
        rarity_elements = [el[2] for el in characteristic]
        new_characteristic = random.choices(characteristic_values, rarity_elements)[0]
        # new_characteristic_index = characteristic_values.index(new_characteristic)
        characteristic_num = int(new_characteristic.split('/')[-1].split('-')[0])
        return [characteristic_num, new_characteristic]

    def dna_is_unique(self, new_dna: list) -> bool:
        """" Checks if dna is unique """
        if new_dna in self.dna_list:
            return False
        else:
            return True

    def allowed_combinations(self, new_dna: list) -> bool:
        """Checks if dna is allowed by comparing the values to those in the allow_list
        Example: for dna = [0, 12, 0, 13, 6, 10, 11], we get each num in list and check if the sublist is inside the
        allowed numbers, i.e. for background (0) and elem 0 we check if:
         12 is in allow_list[0][0][1][0], 0 in allow_list[0][0][1][1], etc, for hair_back #12 we check if:
         0 is in allow_list[1][12][1][0], 13 in allow_list[1][12][1][1], etc...
         Example for combinations_helper: this is an example sublist for i=0, i.e. background:
         [0, 1, [0, 1, 2, 3, 4, 5]] ->
         element 0 is current trait, i.e. 0=background.
         element 1 is 1 if we don't have to search (every combination is included) else it is set to 0.
         element 2 is a list of the other traits that are not changed, i.e. do not need to search. for example if:
         [0, 2, 3, 4, 5] -> it means in trait 1 from the list of other traits, we need to check because something is missing.
         (element 0=hair_back, 1=body, etc.)
        """
        for i, dna in enumerate(new_dna):
            check_dna_list = new_dna[i + 1:]
            if not check_dna_list:
                return True
            if self.combinations_helper[i][1] == 1:
                continue
            else:
                for j, check_dna in enumerate(check_dna_list):
                    if j in self.combinations_helper[i][2]:
                        continue
                    else:
                        if check_dna not in self.allow_list[i][dna][1][j]:
                            return False

    def create_from_dna_to_create_list(self) -> None:
        """ Gets and constructs dna from the dna_to_create list, -1 means any trait from the specific characteristic """
        new_dna = self.dna_to_create[self.dna_to_create_counter]
        new_characteristic_list = []
        if -1 not in new_dna:
            self.dna_list.append(new_dna)
            for i, characteristic in enumerate(self.list_of_characteristics):
                for item in characteristic:
                    if item[0] == new_dna[i]:
                        new_characteristic_list.append(item[1])
            self.dna_traits_list.append(new_characteristic_list)
            print(new_dna, new_characteristic_list)
        else:
            new_dna_list = []
            while True:
                for i, characteristic in enumerate(self.list_of_characteristics):
                    if new_dna[i] != -1:
                        for item in characteristic:
                            if item[0] == new_dna[i]:
                                new_characteristic_list.append(item[1])
                                new_dna_list.append(new_dna[i])
                    else:
                        optimized_characteristic = self.optimize_choice(new_dna_list, characteristic, i)
                        random_characteristic = self.make_random_choice(optimized_characteristic)
                        new_dna_list.append(random_characteristic[0])
                        new_characteristic_list.append(random_characteristic[1])
                if self.dna_is_unique(new_dna_list):
                    break
                else:
                    new_dna_list = []
                    new_characteristic_list = []
            self.dna_list.append(new_dna_list)
            self.dna_traits_list.append(new_characteristic_list)
            print(new_dna_list, new_characteristic_list)

    def optimize_choice(self, current_dna: list, next_characteristic: list, current_characteristic_num: int) -> list:
        """ Returns a list of the only choices available for the current dna.
        We start from the whole list of the next characteristic to choose from.
        current_characteristic_num is which list we are currently.
        For example, for bg_3 next_characteristic could be [0, 1, 2] and current_characteristic_num = 2.
        Then for each characteristic of the current_dna we find out which ones fit, and filter the list accordingly.
        In the end we return the filtered list.
        next_characteristic = [[0, 'images/7-mouth/Mouth 1.png', 10.0], [1, 'images/7-mouth/Mouth 2.png', 10.0], [2, 'images/7-mouth/Mouth 3.png', 10.0], ...]
        combinations helper: [0, 1, [0, 1, 2, 3, 4, 5]]
        """

        if not current_dna:
            return next_characteristic

        filtered_list = next_characteristic
        for i, dna in enumerate(current_dna):

            if self.combinations_helper[i][1] == 1:
                continue
            elif current_characteristic_num - i - 1 in self.combinations_helper[i][2]:
                continue
            else:
                list_to_filter = self.allow_list[i][dna][1][current_characteristic_num - i - 1]
                filtered_list = list(filter(lambda x: x[0] in list_to_filter, filtered_list))

        return filtered_list

    def make_dna(self) -> (dict, list):
        """ If we haven't fully traversed dna_to_create list, create dna from that list, else make new random dna """
        if self.dna_to_create_counter < len(self.dna_to_create):
            self.create_from_dna_to_create_list()
            self.dna_to_create_counter += 1
            return dict(zip(self.attribute_names, self.dna_traits_list[-1]))
        else:
            while True:
                new_dna = []
                new_characteristic = []
                for i, characteristic in enumerate(self.list_of_characteristics):
                    optimized_characteristic = self.optimize_choice(new_dna, characteristic, i)
                    random_characteristic = self.make_random_choice(optimized_characteristic)
                    new_dna.append(random_characteristic[0])
                    new_characteristic.append(random_characteristic[1])
                if self.dna_is_unique(new_dna):
                    self.dna_list.append(new_dna)
                    self.dna_traits_list.append(new_characteristic)
                    # print(new_characteristic)
                    return dict(zip(self.attribute_names, self.dna_traits_list[-1])), new_characteristic
