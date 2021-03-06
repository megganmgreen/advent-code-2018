""" Part One """
from string import ascii_uppercase

def get_polymer():
    """
        Opens a file; returns a polymer string
    """

    with open('day-05.txt') as file:
        polymer = file.read().strip()

    return polymer


def catalyze_reaction(polymer):
    """
        Takes in a polymer string; returns a reaction list
    """

    reaction = list(polymer)

    i = 0
    j = 1
    while j < len(reaction):
        if reaction[i] == 0 and i > 0:
            i += -1
        elif (reaction[i] == 0 and i == 0) or reaction[i].swapcase() != reaction[j]:
            i = j
            j += 1
        else:  # reaction!
            reaction[i] = 0
            reaction[j] = 0
            j += 1
            if i == 0:
                i = j
                j += 1
            else:
                i += -1

    return reaction


def collapse_product(reaction):
    """
        Takes in a reaction list; returns a product string
    """

    product = ''.join([unit for unit in reaction if unit != 0])
    return product


""" Part Two """
def preen_polymer(polymer, unit):
    """
        Takes in a polymer string and a unit string; returns a polymer string
    """

    preened_polymer = list(polymer)
    # unit = unit.upper()

    for i in range(len(preened_polymer)):
        if preened_polymer[i].upper() == unit:
            preened_polymer[i] = 0

    return ''.join([p for p in preened_polymer if p != 0])


def make_all_preened_and_reacted_products(polymer):
    """
        Takes in a polymer string; returns a dictionary of possible products
        after preening one unit from the list of 26 units
    """

    products = {}

    for char in list(ascii_uppercase):
        prod = collapse_product(catalyze_reaction(preen_polymer(polymer, char)))
        if not products.get(len(prod)):
            products[len(prod)] = []
        products[len(prod)].append(prod)

    return products


def get_shortest_product(polymer):
    """
        Takes in a polymer string; returns the length integer of the shortest
        possible product
    """

    return sorted(make_all_preened_and_reacted_products(polymer).keys())[0]
