from roman_numerals_helper_dryer import RomanNumerals 

def test_to_roman():
    assert RomanNumerals.to_roman(1000) == 'M'
    assert RomanNumerals.to_roman(4) ==  'IV'
    assert RomanNumerals.to_roman(1) == 'I'
    assert RomanNumerals.to_roman(1990) == 'MCMXC'
    assert RomanNumerals.to_roman(2008) == 'MMVIII'
    assert RomanNumerals.to_roman(3013) == 'MMMXIII'
    assert RomanNumerals.to_roman(1768) == 'MDCCLXVIII'
    assert RomanNumerals.to_roman(3958) == 'MMMCMLVIII'
    assert RomanNumerals.to_roman(3812) == 'MMMDCCCXII'
    assert RomanNumerals.to_roman(3308) == 'MMMCCCVIII'
    assert RomanNumerals.to_roman(2823) == 'MMDCCCXXIII'
    assert RomanNumerals.to_roman(3882) == 'MMMDCCCLXXXII'
    assert RomanNumerals.to_roman(1009) == 'MIX'
    assert RomanNumerals.to_roman(249) == 'CCXLIX'
    assert RomanNumerals.to_roman(3999) == 'MMMCMXCIX'
    
def test_from_roman():
    assert RomanNumerals.from_roman('XXI') == 21
    assert RomanNumerals.from_roman('I') == 1
    assert RomanNumerals.from_roman('IV') == 4
    assert RomanNumerals.from_roman('MMVIII') == 2008
    assert RomanNumerals.from_roman('MDCLXVI') == 1666
    assert RomanNumerals.from_roman('MMMDCCCLXVII') == 3867
    assert RomanNumerals.from_roman('MDIV') == 1504
    assert RomanNumerals.from_roman('MMDCCCXXVI') == 2826
    assert RomanNumerals.from_roman('MMMDCLXXIX') == 3679
    assert RomanNumerals.from_roman('MDCCCLXXV') == 1875
    assert RomanNumerals.from_roman('MMXCIII') == 2093
    assert RomanNumerals.from_roman('DCXXIV') == 624
    assert RomanNumerals.from_roman('MCMLXXXIX') == 1989
    assert RomanNumerals.from_roman('MMMDCCCVI') == 3806
    assert RomanNumerals.from_roman('MDCCLXVII') == 1767