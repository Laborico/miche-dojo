from word_patterns import word_pattern

def test_correct_pattern_on_string():
  assert word_pattern('abab', 'apple banana apple banana') == True
  assert word_pattern('abba', 'car truck truck car') == True
  assert word_pattern('aaaa', 'cat cat cat cat') == True
  assert word_pattern('bbbabcb', 'c# c# c# javascript c# python c#') == True
  assert word_pattern('abcdef', 'apple banana cat donkey elephant flower') == True
  assert word_pattern('xyzzyx', '1 2 3 3 2 1') == True
  assert word_pattern('aafggiilp', 'cow cow fly pig pig sheep sheep chicken aardvark') == True

def test_incorrect_pattern_on_string():
  assert word_pattern('abab', 'apple banana banana apple') == False
  assert word_pattern('aaaa', 'cat cat dog cat') == False
  assert word_pattern('xyzzyx', 'apple banana apple banana') == False
  assert word_pattern('aaaa', 'cat cat cat') == False
  assert word_pattern('abba', 'dog dog dog dog') == False
  assert word_pattern('aafggiilp', 'cow cow fly rooster pig sheep sheep chicken aardvark') == False

def test_randoms_from_codewars():
  assert word_pattern('dtt', 'bulma goku goku') == True
  assert word_pattern('rttr', 'goten majin majin majin goten') == False
  assert word_pattern('rttrr', 'goten majin majin majin goten') == False
  assert word_pattern('ttttitft', 'roshi roshi roshi roshi majin roshi tien roshi') == True
  assert word_pattern('odovoob', 'krillin trunks krillin frieza krillin krillin kaioken') == True
  assert word_pattern('ffcjfbc', 'majin majin bulma kaioken majin tien bulma') == True
  assert word_pattern('vvvsdvd', 'frieza frieza frieza roshi kaioken frieza kaioken') == True
  assert word_pattern('httctxxxx', 'goten majin majin muten majin genkidama genkidama genkidama genkidama') == True
  assert word_pattern('mbhjbhfbh', 'masenko bulma majin goku bulma majin frieza bulma majin') == True
  assert word_pattern('etssis', 'genkidama frieza majin majin toketsu majin') == True
  assert word_pattern('lgwqgyl', 'trunks genkidama gohan kamehameha genkidama roshi trunks') == True
  assert word_pattern('xdlxjxo', 'frieza majin vegeta frieza goku frieza gohan') == True
  assert word_pattern('aawajzf', 'genkidama genkidama gohan genkidama roshi toketsu vegeta') == True
  assert word_pattern('gadf', 'genkidama frieza goku roshi') == True
  assert word_pattern('kjojodkl', 'masenko roshi madan roshi madan kamehameha masenko tien') == True
  assert word_pattern('glfeefkl', 'krillin majin bulma gohan gohan bulma trunks majin') == True
  assert word_pattern('qyqqoy', 'kaioken goku kaioken kaioken muten goku') == True
  assert word_pattern('ijjs', 'tien madan madan gohan') == True
  assert word_pattern('hcphkpchk', 'goten toketsu tien goten vegeta tien toketsu goten vegeta') == True
  assert word_pattern('xoxzxmzom', 'trunks frieza trunks genkidama trunks kaioken genkidama frieza kaioken') == True
  assert word_pattern('aaefbu', 'goku goku madan gohan frieza trunks') == True
  assert word_pattern('cqqrc', 'goku vegeta vegeta frieza goku') == True
  assert word_pattern('hpthtlp', 'gohan trunks goku gohan goku krillin trunks') == True
  assert word_pattern('llddllla', 'krillin krillin madan madan krillin krillin krillin majin') == True
  assert word_pattern('hefhqeqfq', 'vegeta madan goten vegeta roshi madan roshi goten roshi') == True
  assert word_pattern('qct', 'kaioken vegeta madan') == True
  assert word_pattern('pbe', 'trunks kaioken majin') == True
  assert word_pattern('tuy', 'goten goku genkidama') == True
  assert word_pattern('nytb', 'muten goku roshi bulma') == True
  assert word_pattern('jerferjvrr', 'krillin goku vegeta genkidama goku vegeta krillin muten vegeta vegeta') == True
  assert word_pattern('zcy', 'trunks majin masenko') == True
  assert word_pattern('cgttsg', 'krillin goku toketsu toketsu roshi goku') == True
  assert word_pattern('fzuur', 'kaioken masenko majin majin krillin') == True
  assert word_pattern('xss', 'krillin kamehameha kamehameha') == True
  assert word_pattern('bjbbcb', 'frieza goten frieza frieza genkidama frieza') == True
  assert word_pattern('bqqnqbqyw', 'trunks goten goten bulma goten trunks goten frieza kaioken') == True
  assert word_pattern('sxsezddze', 'gohan vegeta gohan krillin madan majin majin madan krillin') == True
  assert word_pattern('ttt', 'bulma bulma bulma') == True
  assert word_pattern('qqbqacbfca', 'goten goten genkidama goten bulma goku genkidama kaioken goku bulma') == True
  assert word_pattern('wdcoowcw', 'madan krillin tien gohan gohan madan tien madan') == True
  assert word_pattern('bijlibjp', 'genkidama muten goten trunks muten genkidama goten gohan') == True