############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code

        self.first_harvest = first_harvest

        self.color = color

        self.is_seedless = is_seedless

        self.is_bestseller = is_bestseller

        self.pairings = []

        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    # Fill in the rest
    # print(all_melon_types)
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    print(melon_types)
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print("- " + pairing)
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # take the list of all_melon type
    melon_dict = {}
    for melon in melon_types:
        # print(melon)
        # if melon.code not in melon_dict:
        melon_dict[melon.code] = melon
    
    # print(melon_dict)
    return melon_dict

   


############
# Part 2   #
############

class Melon():
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape, color_rating, field, harvested_by):
        self.melon_type = melon_type
        self.shape = shape
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        if self.color_rating > 5 and self.shape > 5 and self.field != 3:
            return True
        else:
            return False

        

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, 'Sheila')  
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, 'Michael')   
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons_list = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, 
                   melon_7, melon_8, melon_9]

    return melons_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.harvested_by} from Field {melon.field} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.harvested_by} from Field {melon.field} (NOT SELLABLE)')    

    # Fill in the rest 


all_melon_types = make_melon_types()

print_pairing_info(all_melon_types)

# melon_dict = make_melon_type_lookup(all_melon_types)

melons = make_melons(all_melon_types)

get_sellability_report(melons)