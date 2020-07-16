# -*- coding: utf-8 -*-
import re
from variation_builder import get_new_combos_recursive, convert_to_string

# This computes the variations possible of the koine Greek that would still be translated as "John loves Mary"
# See https://www.youtube.com/watch?v=ECdq5yv7HOc 

DROP_THESE = re.compile('^(((μὲν)|(τε)).*)|(.*((μὲν)|(τε)))$')

def drop_bad_conjunctions(entries):
    new_list = []

    for entry in entries:
        if not DROP_THESE.match(entry):
            new_list.append(entry)

    return new_list

def remove_overlap(a, b):
    a = set(a)
    b = set(b)
    return a.difference(b)

# Basic ordering differences only
combinations = [
    ['Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν']
]

ordering_only = get_new_combos_recursive(combinations)
ordering_only = convert_to_string(sorted(ordering_only))

# With articles
combinations_articles = [
    ['Ἰωάννης', 'ό Ἰωάννης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]

with_articles = get_new_combos_recursive(combinations_articles)
with_articles = convert_to_string(sorted(with_articles))

# Now get the ones with alternative spellings of John
combinations_john = [
    ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν']
]
spelling_john = get_new_combos_recursive(combinations_john)
spelling_john = convert_to_string(sorted(spelling_john))
spelling_john = remove_overlap(spelling_john, with_articles)

# Now get the ones with alternative spellings of Mary
combinations_mary = [
    ['Ἰωάννης', 'ό Ἰωάννης', 'Ἰωάνης', 'ό Ἰωάνης'],
    'ὰγαπᾷ',
    ['Μαρίαν', 'τὴν Μαρίαν', 'Μαριάμμην', 'τὴν Μαριάμμην']
]
spelling_mary = get_new_combos_recursive(combinations_mary)
spelling_mary = convert_to_string(sorted(spelling_mary))
spelling_mary = remove_overlap(spelling_mary, spelling_john)
spelling_mary = remove_overlap(spelling_mary, with_articles)

# Output them
import csv
with open('variants.csv', 'w', newline='') as csvfile:
    varwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

    for row in with_articles:
        varwriter.writerow([row])

    for row in spelling_john:
        varwriter.writerow([row])

    for row in spelling_mary:
        varwriter.writerow([row])
