#!/usr/bin/python3
words = ['broccoli', 'cucumber', 'cauliflower', 'avocado', 'zucchini', 'asparagus', 'rhinoceros', 'chrysanthemum', 'xylophone', 'crocodile', 'pterodactyl', 'schizophrenia', 'antidisestablishmentarianism', 'supercalifragilisticexpialidocious', 'pneumonoultramicroscopicsilicovolcanoconiosis', 'hippopotamus', 'acrophobia', 'triskaidekaphobia', 'turophobia', 'sesquipedalian', 'Exacerbate', 'Pseudonym', 'Ambidextrous', 'Chrysanthemum', 'Dichotomy', 'Epiphany', 'Galvanize', 'Inscrutable', 'Labyrinth', 'Perfunctory', 'Eccentric', 'Phenomenal', 'Serendipity', 'Ineffable', 'Exquisite', 'Magnanimous', 'Quintessential', 'Ubiquitous', 'Enigma', 'Paradoxical']

words2 = ["apple", "banana", "orange", "peach", "grape", "lemon", "chair", "table", "knife", "spoon", "plate", "glass", "mouse", "clock", "brush", "tooth", "light", "phone", "door", "plant"]

ordered_words = sorted(words2, key=len)
for word in ordered_words:
    print(word)
#print(ordered_words)

