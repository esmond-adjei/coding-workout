#!/usr/bin/python3
import random

def scramble(word):
    scrambled_word = ''
    len_w = len(word) - 1
    rands = []
    a = random.Random()

    for i in range(len_w+1):

        r = a.randint(1, len_w)
        while r in rands:
            r = a.randint(1, len_w)
        
        scrambled_word += word[r]
        rands.append(r)
    
    return scrambled_word

print(scramble("esmond"))


