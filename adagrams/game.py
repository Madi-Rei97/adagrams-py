from random import randint

LETTER_POOL = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 
                'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
                'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'H', 'H',
                'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L',
                'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'O',
                'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
                'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T',
                'T', 'T', 'U', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y',
                'Y', 'Z']

def counting(count_what, in_what):
    total_count = 0
    for i in in_what:
        if i == count_what:
            total_count += 1

    return total_count

def draw_letters():
    letters = []

    for letter in range(10):
        letters.append(LETTER_POOL[randint(0, 97)])
    
    index = 0
    for letter in letters:
        if (counting(letter, letters) > counting(letter, LETTER_POOL)):
            letters[index] = LETTER_POOL[randint(0, 97)]
        index += 1

    return letters

def word_as_list_and_all_caps(word):
    word_all_caps = word.upper()
    word_as_list = []
    for letter in word_all_caps:
        word_as_list.append(letter)
    
    return word_as_list

def uses_available_letters(word, letter_bank):
    word_chosen = word_as_list_and_all_caps(word)

    for letter in word_chosen:
        is_valid_word = True
        if not (letter in letter_bank) or not (counting(letter, 
                    letter_bank) <= counting(letter, word_chosen) <= 
                    counting(letter, letter_bank)):
            is_valid_word = False
    
    return is_valid_word

def length(object):
    count = 0
    for i in object:
        count += 1
    return count

def score_word(word):
    SCORE_CHART = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 
        2: ['D', 'G'], 
        3: ['B', 'C', 'M', 'P'], 
        4: ['F', 'H', 'V', 'W', 'Y'], 
        5: ['K'], 
        8: ['J', 'X'], 
        10: ['Q', 'Z']
        }
    word_chosen = word_as_list_and_all_caps(word)
    total_score = 0

    for word_letter in word_chosen:
        for score, letter_list in SCORE_CHART.items():
            for letter in letter_list:
                if letter == word_letter:
                    total_score += score
    
    if length(word_chosen) >= 7:
        total_score += 8
    
    return total_score

def get_highest_word_score(word_list):
    score_list = []
    for word in word_list:
        score = score_word(word)
        score_list.append(score)

    winning_score = score_list[0]
    for score in score_list:
        if score > score_list[0]:
            winning_score = score

    index = 0
    high_score_words = []
    for score in score_list:
        if score == winning_score:
            high_score_words.append(word_list[index])
        index += 1

    fewest_letters_word = high_score_words[0]
    for word in high_score_words:
        if length(word) < length(fewest_letters_word):
            fewest_letters_word = word

    fewest_letter_words_list = []
    for word in high_score_words:
        if length(word) == length(fewest_letters_word):
            fewest_letter_words_list.append(word)
    
    length_10_words = []
    for word in high_score_words:
        if length(word) == 10:
            length_10_words.append(word)

    if length(high_score_words) > 1:
        for word in high_score_words:
            if length(word) == 10 and length(length_10_words) == 1:
                winning_word = word
                break
            elif length(word) == 10 and length(length_10_words) > 1:
                winning_word = length_10_words[0]
            elif length(fewest_letter_words_list) == 1:
                winning_word = fewest_letters_word
            elif length(fewest_letter_words_list) > 1:
                winning_word = fewest_letter_words_list[0]
    else:
        winning_word = high_score_words[0]

    return winning_word, winning_score
