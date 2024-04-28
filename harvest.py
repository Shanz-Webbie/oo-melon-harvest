############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""
    species = "melon"

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.name = name  
        self.code = code
        self.first_harvest = first_harvest 
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    # musk.add_pairing("basil")
    # all_melon_types.append(musk)



# code, first_harvest, color, is_seedless, is_bestseller, name
    melon_dict ={'musk':
        {'code':'musk',
        'first_harvest':1998, 
        'color':'green',
        'is_seedless':True,
        'is_bestseller':True,
        'name':'Muskmelon',
        'pairings':['mint']},
        'cas':
        {'code':'cas',
        'first_harvest':2003, 
        'color':'orange',
        'is_seedless':False,
        'is_bestseller':False,
        'name':'Casaba',
        'pairings':['mint','strawberries']},
        'cren':
        {'code':'cren',
        'first_harvest':1996, 
        'color':'green',
        'is_seedless':False,
        'is_bestseller':False,
        'name':'Crenshaw',
        'pairings':['prosciutto']},
        'yw':
        {'code':'yw',
        'first_harvest':2013, 
        'color':'yellow',
        'is_seedless':False,
        'is_bestseller':True,
        'name':'Yellow Watermelon',
        'pairings':['ice cream']}
        }
    
    # musk = MelonType('musk',melon_dict['musk']['code'], 
    #                           melon_dict['musk']['first_harvest'], 
    #                           melon_dict['musk']['is_seedless'], 
    #                           melon_dict['musk']['is_bestseller'], 
    #                           melon_dict['musk']['name'])
    # print(musk.name)
    
    for melon in melon_dict:
        melon_obj = MelonType(melon, melon_dict[melon]['code'], 
                              melon_dict[melon]['first_harvest'], 
                              melon_dict[melon]['is_seedless'], 
                              melon_dict[melon]['is_bestseller'], 
                              melon_dict[melon]['name'])
        melon_obj.add_pairing(melon_dict[melon]['pairings'])
        all_melon_types.append(melon_obj)
    
    return all_melon_types

# make_melon_types()

melon_types = make_melon_types()

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # return [melon for melon in all_melon_types, print(f"{melon.name} pairs with {melon.pairings}")]
    for melon in melon_types:
        print(f"{melon.name} pairs with {melon.pairings}")
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest
    melon_dict = {}
    for each_melon in melon_types:
        melon_dict[each_melon.code] = each_melon
    print(melon_dict)
    return melon_dict

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_name, shape, color, field_location, harvester):
        self.color = color
        self.melon_name = melon_name
        self.shape = shape
        self.field_location = field_location
        self.harvester = harvester
        

    def is_sellable(shape, color, field_location):
        if shape > 5 and color > 5:
            if field_location != 3:
                return True
            else:
                False

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melon_list.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])
    print(melon_list)
    return melon_list
melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable() == True:
            print(f'Harvested by {melon.harvester} from {melon.field_location} (Can be sold)')
        else:
            print(f"Harvested by {melon.harvester} from {melon.field_location} (Can't be sold)")


    # Fill in the rest
