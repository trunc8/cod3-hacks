#trunc8

import random
import time

words = ["ASTRAL","EVERGREEN","PEACOCK"]
word = random.choice(words)
letter_mask = {ch:0 for ch in word}
letters_used = []
attempts = 10

start_time = time.time()
while True:
    print(f"Attempts left: {attempts}")
    for ch in word:
        if letter_mask[ch]:
            print(ch, end = " ")
        else:
            print("_", end = " ")
    print()
    print("Letter used so far: ", letters_used)
    ch = input("Enter a letter: ").upper()
    if ch=='-1':
        print(f"You have forfeited. The correct word was {word}.")
        break
    elif ch<'A' or ch>'Z' or len(ch)!=1:
        print("\tInvalid input")
        continue
    elif ch in letters_used:
        print("\tAlready checked on this later. Was it by mistake?")
        continue
    attempts = attempts - 1
    letters_used.append(ch)
    if ch in word:
        print("\tYou got a strike!")
        letter_mask[ch] = 1
    if sum(letter_mask.values())==len(letter_mask):
        print(f"You've won!! The word is {word}.")
        break

elapsed_time = time.time()-start_time
print(time.strftime("Time taken= %H:%M:%S", time.gmtime(elapsed_time)))