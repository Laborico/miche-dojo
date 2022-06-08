def word_pattern(pattern, string):
    word_list = string.split(" ")
    
    if len(pattern) != len(word_list):
        return False
    
    letter_definition = {}
    for i, word in enumerate(word_list):
        if pattern[i] in letter_definition:
            if letter_definition[pattern[i]] != word:
                return False
        else:
            if word in letter_definition.values():
                return False
            letter_definition[pattern[i]] = word
            
    return True