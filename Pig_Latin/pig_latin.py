import string

def pig_it(text):
    words = text.split()
    for i, word in enumerate(words):
        if len(word) > 1:
            words[i] = word[1:] + word[0] + 'ay'
        elif word not in string.punctuation:
            words[i] = word + 'ay'

    return ' '.join(words)