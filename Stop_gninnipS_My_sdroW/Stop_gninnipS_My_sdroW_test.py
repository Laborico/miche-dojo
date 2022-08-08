from Stop_gninnipS_My_sdroW_list import spin_words

def loop(sentence, expected):
    for i, word in enumerate(sentence):
        assert spin_words(word) == expected[i]
        

def test_short_words():
    sentences = ['a', 'abc', 'able',
                 'acid', '123', 'test'] 
    loop(sentences, sentences)
    
def test_long_words():
    sentences = ['tests', '12345', 'rotavator',
                 'malayalam', 'longWord', 'asdasd'] 
    expected = ['stset', '54321', 'rotavator',
                'malayalam', 'droWgnol', 'dsadsa']
    loop(sentences, expected)
    
def test_sentences():
    sentences = ['Stop Spinning My Words', 'This is a test', 'I cannot remember longer words',
                 'Easy peacy lemmon squezzy', 'Some random words put together', 
                 'King for a day'] 
    expected = ['Stop gninnipS My sdroW', 'This is a test', 'I tonnac rebmemer regnol sdrow',
                'Easy ycaep nommel yzzeuqs', 'Some modnar sdrow put rehtegot', 
                'King for a day']
    loop(sentences, expected)