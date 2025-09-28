from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

HAND_SIZE = 10
PILE_SIZE = len(LETTER_POOL)

def make_new_draw_pile():
    draw_pile = []
    for letter, count in LETTER_POOL.items():
        [draw_pile.append(letter)] * count
    return draw_pile

def draw_letters():
    new_pile = make_new_draw_pile()
    new_pile_len = PILE_SIZE
    hand = []

    for _ in range(HAND_SIZE):
        hand.append(new_pile.pop(randint(0, new_pile_len - 1)))
        new_pile_len -= 1

    return hand

def counting(count_what, in_what):
    total_count = 0
    for i in in_what:
        if i == count_what:
            total_count += 1

    return total_count

def uses_available_letters(word, letter_bank):
    if not word:
        return False
    
    for letter in word:
        if letter.upper() in letter_bank and counting(letter.upper(), 
                    word.upper()) <= counting(letter.upper(), letter_bank):
            continue
        else:
            return False
        
    return True

def score_word(word):
    SCORE_CHART = { 
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
                    }

    BONUS_MIN_LENGTH = 7
    BONUS_POINTS = 8

    total_score = 0
    for letter in word:
        if letter.upper() in SCORE_CHART:
            total_score += SCORE_CHART[letter.upper()]
    
    if len(word) >= BONUS_MIN_LENGTH:
        total_score += BONUS_POINTS

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
        if len(word) < len(fewest_letters_word):
            fewest_letters_word = word

    fewest_letter_words_list = []
    for word in high_score_words:
        if len(word) == len(fewest_letters_word):
            fewest_letter_words_list.append(word)
    
    length_10_words = []
    for word in high_score_words:
        if len(word) == 10:
            length_10_words.append(word)

    if len(length_10_words) >= 1:
        winning_word = length_10_words[0]
    elif len(fewest_letter_words_list) >= 1:
        winning_word = fewest_letter_words_list[0]

    return winning_word, winning_score
