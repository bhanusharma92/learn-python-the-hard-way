def break_words(stuff):
    """this fuction will break up stuff for us"""
    word = stuff.split(' ')
    return word

def sort_words(words):
    """sort the words"""
    return sorted(words)

def print_first_word(words):
    """print the first word"""
    word = words.pop(0)
    return word

def print_last_word(words):
    """print last word"""
    word = words.pop(-1)
    return word

def sorted_sentence(sentence):
    """Take in full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last word of the sentence"""
    words = break_words(sentence)
    first_word = print_first_word(words)
    last_word = print_last_word(words)
    print(first_word, " ", last_word)

def print_first_and_last_sorted(sentence):
    sorted_words = sorted_sentence(sentence)
    first_word = print_first_word(sorted_words)
    last_word = print_last_word(sorted_words)
    print(first_word, " ", last_word)







