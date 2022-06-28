class RomanNumerals:        
    def to_roman(val):
        def substract(val, divisor):
            while val >= divisor:
                val = val - divisor
            return val

        values = {
            "M": 1000, "CM": 900,"D": 500, "CD": 400,
            "C": 100, "XC": 90,  "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, 'I': 1
        }

        conversion = ''

        for letter, number in values.items():
            conversion = conversion + letter * (val//number)
            val = substract(val, number)

        return conversion

    def from_roman(roman_num): 
        def convert(number, roman_value, numeric_value):
            cont = 0
            for value in number:
                if value == roman_value:
                    cont = cont + 1
                else:
                    break
            return numeric_value * cont, cont

        def special_convert(number, roman_value, numeric_value, special_roman, special_numeric):
            if number[:2] == special_roman[0]:
                return special_numeric[0], 2
            elif number[:2] == special_roman[1]:
                return special_numeric[1], 2
            else:
                return convert(number, roman_value, numeric_value)

        values = {
            "M": 1000, "D":	500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1
        }

        special_values = {
            "C": [['CM', 'CD'], [900, 400]], 
            "X": [['XC', 'XL'], [90, 40]], 
            "I": [['IX', 'IV'], [9, 4]]
        }

        conversion = 0
        for letter, number in values.items():     
            if letter in special_values:
                value, cont = special_convert(roman_num, letter, number, special_values[letter][0], special_values[letter][1])
            else:   
                value, cont = convert(roman_num, letter, number)
            conversion = conversion + value
            roman_num = roman_num[cont:]
            
        return conversion