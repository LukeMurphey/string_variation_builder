# -*- coding: utf-8 -*-
combinations = [
    ['Ἰωάννης', 'ό Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]

def get_new_combos(current_combinations, new_string):
    # Here is the list of new combinations
    new_combos = []

    # Make new combinations of the existing combinations
    for combo in current_combinations:
        new_combo = combo.copy()
        
        for i in range(0, len(combo)):
            new_combo = combo.copy()

    return new_combos

def get_new_combo(current_combination, new_string):
    new_combos = []

    for i in range(0, len(current_combination) + 1):
        new_combo = current_combination.copy()

        # If this is past the end, then add it to the end
        if i > len(current_combination):
            new_combo.append(new_string)
        else:
            new_combo.insert(i, new_string)
        
        new_combos.append(new_combo)

    return new_combos

def make_variants(current_combination, variants):
    if isinstance(variants, str):
        return [variants]
    
    for next_variants in variants:
        new_variants = make_variants(current_combination, next_variants)

#for variant in make_variants(combinations):
#    print(variant)


test_get_new_combo()
