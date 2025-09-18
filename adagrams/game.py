from random import randint

letter_pool = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 
                'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
                'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H',
                'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L',
                'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O',
                'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
                'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T',
                'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y',
                'Y', 'Z']

def draw_letters():
    letters = []

    for letter in range(10):
        letters.append(letter_pool[randint(0, 97)])
    
    index = 0
    for letter in letters:
        if letters.count(letter) > letter_pool.count(letter):
            letters[index] = letter_pool[randint(0, 97)]
        index += 1

    return letters

def uses_available_letters(word, letter_bank):
    word_all_caps = word.upper()
    word_as_list = []
    for letter in word_all_caps:
        word_as_list.append(letter)

    for letter in word_as_list:
        is_valid_word = True
        if not (letter in letter_bank) or not (letter_bank.count(letter) <= 
                    word_as_list.count(letter) <= letter_bank.count(letter)):
            is_valid_word = False
    
    return is_valid_word

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass