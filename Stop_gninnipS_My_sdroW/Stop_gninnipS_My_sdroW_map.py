def spin_words(sentence):
    reverse = lambda x: x[::-1] if len(x) >= 5 else x
    return ' '.join(map(reverse, sentence.split()))