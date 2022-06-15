from pig_latin import pig_it

def test_simple_words():
  assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
  assert pig_it('This is my string') == 'hisTay siay ymay tringsay'

def test_one_length_words():
   assert pig_it('O tempora o mores !') == 'Oay emporatay oay oresmay !'
   assert pig_it('A b C d E') == 'Aay bay Cay day Eay'
   assert pig_it('a . Bias di') == 'aay . iasBay iday'

def test_random_words_from_Codewars():
  assert pig_it('Veni vidi vici') == 'eniVay idivay icivay'
  assert pig_it('Cucullus non facit monachum') == 'ucullusCay onnay acitfay onachummay'
  assert pig_it('Sic transit gloria mundi') == 'icSay ransittay loriagay undimay'
  assert pig_it('Errare humanum est') == 'rrareEay umanumhay steay'
  assert pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?'
  assert pig_it('Hic et nunc') == 'icHay teay uncnay'
  assert pig_it('Requiescat in pace') == 'equiescatRay niay acepay'
  assert pig_it('Dura lex sed lex') == 'uraDay exlay edsay exlay'
  assert pig_it('Barba non facit philosophum') == 'arbaBay onnay acitfay hilosophumpay'
  assert pig_it('Acta est fabula') == 'ctaAay steay abulafay'