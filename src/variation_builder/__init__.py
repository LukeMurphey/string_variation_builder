# -*- coding: utf-8 -*-
combinations = [
    ['Ἰωάννης', 'ό Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]

def get_new_combos(combo_strings, current_combos=None):
    """
    Make a new list of possible combinations of the given list of existing combinations, combined with the new combinations.

    Consider the following examples:

        get_new_combos(['a', 'b'])
        [ ['a'], ['b'] ]

        get_new_combos(['a', 'b'], [['c']])
        [ ['a', 'c'], ['b', 'c'], ['c', 'a'], ['c', 'b'] ]

    Arguments:
    combo_strings -- A list of strings from which to derive combinations
    current_combos -- A list of lists of strings that represents the current combination already computed
    """

    # Initialize the combos if necessary
    if current_combos is None:
        current_combos = [[]]

    # Here is the list of new combinations
    new_combos = []

    for combo_string in combo_strings:

        # Get new combos of existing ones
        for combo in current_combos:
            new_combos_for_string = get_new_combo(combo, combo_string)
            new_combos.extend(new_combos_for_string)

        # Seed the new combos that are not based on current ones
        # new_combos.append([combo_string])

    return new_combos

def uniqify_list_of_lists(lists):
    """
    Make sure the list is unique.

    Arguments:
    lists -- a list of lists to make unique
    """
    return [list(x) for x in set(tuple(x) for x in lists)]

def get_new_combo(current_combination, new_string):
    """
    Make a new list of possible combinations of the given list combined with the new string.

    Consider the following example:

        get_new_combo(['a', 'b'], 'c')
        [['a', 'b', 'c'], ['a', 'c', 'b'], ['c', 'a', 'b']]

    Arguments:
    current_combination -- a list of strings the represents the current combination
    new_string -- a new string from which to make derivations
    """

    new_combos = []

    for i in range(0, len(current_combination) + 1):
        new_combo = current_combination.copy()

        # If this is past the end, then add it to the end
        if i >= len(current_combination):
            new_combo.append(new_string)

        # Otherwise: just add it into the list
        else:
            new_combo.insert(i, new_string)
        
        new_combos.append(new_combo)

    return uniqify_list_of_lists(new_combos)

def make_variants(current_combination, variants):
    if isinstance(variants, str):
        return [variants]
    
    for next_variants in variants:
        new_variants = make_variants(current_combination, next_variants)
