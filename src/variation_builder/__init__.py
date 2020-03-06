# -*- coding: utf-8 -*-
combinations = [
    ['Ἰωάννης', 'ό Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]

def is_list_not_str(o):
    if isinstance(o, str):
        return False
    if isinstance(o, list):
        return True

def is_list_of_lists(obj, raise_if_mixed=False):
    # If this isn't a list, stop
    if not is_list_not_str(obj):
        return False

    # Stop if this is an empty list
    elif len(obj) == 0:
        return False

    # Determine if this contains lists and scalars
    found_list = False
    found_scalar = False

    for entry in obj:
        if not is_list_not_str(entry):
            found_scalar = True
        else:
            found_list = True

    # Stop if the list contained both
    if raise_if_mixed and found_list and found_scalar:
        raise Exception("List contained scalars and lists! data=%r" % obj)

    # Analyze the results
    if found_list:
        return True
    elif found_scalar:
        return False
    
    raise Exception("List contains neither! data=%r" % obj)

def is_scalar(obj):
    if isinstance(obj, list) and isinstance(obj, list):
        return False
    
    return True

def filter_nones(entries):
    return [entry for entry in entries if entry is not None]

def get_new_combos_recursive(policy):
    """
    This function will flatten the lists by resolving the internal lists to an array.
    """

    # TODO: I think this is wrong. I think I need to compute scalars against all lists and recompute all lists again
    # I think I need to:
    # If list: recurse to get flat list
    # If scalar, compute combos

    # Make a list of just scalars
    scalars = []
    flattened_policies = []

    for entry in policy:

        # Add it to the scalars list
        if is_scalar(entry):
            scalars.append(entry)

        # Flatten the list of lists
        elif is_list_of_lists(entry):
            flattened_entry = get_new_combos_recursive(entry)
            # print('flattened_entry:', flattened_entry)
            # print('from:', entry, '\n\n')
            flattened_policies.extend(flattened_entry) # TODO Possibly wrong?
            # print('flattened_policies: ', flattened_policies, '!\n\n')

        elif is_list_not_str(entry):
            flattened_policies.append(entry)

    # print('scalars: %r' % scalars, '\n')
    # print('flattened_policies: %r' % flattened_policies, '\n\n')

    # The list should now just include single depth lists in flattened_policies
    # Apply them to the scalars to get the completed lists
    combos = [[]]
    last_combos = None
    for flattened_policy in flattened_policies:

        # TODO: This is not doing what I want. It currently isn't making the combinations correctly.
        # I suspect I have the argument order wrong somewhere
        computed = get_new_combos(flattened_policy, last_combos)
        # computed = get_new_combos(flattened_policy, [scalars])

        # # print("new combos:", computed, "\n\t\tfrom", flattened_policy, "\n\t\tand", last_combos)
        combos.extend(computed)
        last_combos = computed

    for scalar in scalars:
        computed = get_new_combos([scalar], last_combos)

        # # print("new combos:", computed, "\n\t\tfrom", scalar)
        combos.extend(computed)
        last_combos = computed

    combos = last_combos

    # Filter out Nones which are allowed for optional entries
    filtered = []
    for sublist in combos:
        filtered.append(filter_nones(sublist))

    combos = filtered

    # Uniqueify the list and return it
    return uniqify_list_of_lists(combos)

def convert_to_string(results):
    strings = []
    for result in results:
        strings.append(" ".join(result))

    return strings

def get_new_combos(combo_strings, current_combos=None):
    """
    Make a new list of possible combinations of the given list of existing combinations, combined with the new combinations.

    Consider the following examples:

        get_new_combos(['a', 'b'])

        [ ['a'], ['b'] ]

        get_new_combos(['a', 'b'], [['c']])
        [ ['a', 'c'], ['b', 'c'], ['c', 'a'], ['c', 'b'] ]

    Arguments:
    combo_strings -- A list of strings from which to derive combinations; these will be crossed with the current_combos to multiply them
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


