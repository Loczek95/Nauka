import random

def enconding_word(word):
    if len(word) > 3:
        first_letter = word[0]
        last_letter = word[-1]
        middle_letter = word[1:-1]
        middle_letter_to_shuffle = list(middle_letter)
        random.shuffle(middle_letter_to_shuffle)
        middle_letter_after_shuffle = "".join(middle_letter_to_shuffle)
        return print(first_letter + middle_letter_after_shuffle+ last_letter)

    else:
        print(word)


print("Podaj słowo:")
word = input()
enconding_word(word)





