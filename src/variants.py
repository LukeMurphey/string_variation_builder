# -*- coding: utf-8 -*-
from variation_builder import get_new_combos_recursive, convert_to_string

# This computes the variations possible of the koine Greek that would still be translated as "John loves Mary"
# See https://www.youtube.com/watch?v=ECdq5yv7HOc 

def remove_overlap(a, b):
    a = set(a)
    b = set(b)
    return a.difference(b)

# Get the basics
combinations = [
    ['Ἰωάννης', 'ό Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]
basic = get_new_combos_recursive(combinations)
basic = convert_to_string(sorted(basic))

# Now get the ones with alternative spellings of John
combinations_john = [
    ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]
spelling_john = get_new_combos_recursive(combinations_john)
spelling_john = convert_to_string(sorted(spelling_john))
spelling_john = remove_overlap(spelling_john, basic)

# Now get the ones with alternative spellings of Mary
combinations_mary = [
    ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν', 'Μαριάμμην', 'τὴν Μαριάμμην']
]
spelling_mary = get_new_combos_recursive(combinations_mary)
spelling_mary = convert_to_string(sorted(spelling_mary))
spelling_mary = remove_overlap(spelling_mary, spelling_john)
spelling_mary = remove_overlap(spelling_mary, basic)

# Output them
import csv
with open('variants.csv', 'w', newline='') as csvfile:
    varwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

    for row in basic:
        varwriter.writerow([row])

    for row in spelling_john:
        varwriter.writerow([row])

    for row in spelling_mary:
        varwriter.writerow([row])
