class RomanNumerals:
    def to_roman(val):
        def substract(val, divisor):
            while val >= divisor:
                val = val - divisor
            return val

        """
        Ex. val = 901, 
        if val >= 900:
            conversion = CM
            val = val - 900
        returns 1, CM

        """
        def special_cases(val, conversion, special, roman):
            if val >= special:
                conversion = conversion + roman
                val = val - special
            return val, conversion

        conversion = ''

        conversion = conversion + 'M' * (val//1000)
        val = substract(val, 1000)
        val, conversion = special_cases(val, conversion, 900, 'CM')

        conversion = conversion + 'D' * (val//500)
        val = substract(val, 500)
        val, conversion = special_cases(val, conversion, 400, 'CD')

        conversion = conversion + 'C' * (val//100)        
        val = substract(val, 100)
        val, conversion = special_cases(val, conversion, 90, 'XC')

        conversion = conversion + 'L' * (val//50)
        val = substract(val, 50)
        val, conversion = special_cases(val, conversion, 40, 'XL')

        conversion = conversion + 'X' * (val//10)
        val = substract(val, 10)
        val, conversion = special_cases(val, conversion, 9, 'IX')

        conversion = conversion + 'V' * (val//5)
        val = substract(val, 5)
        val, conversion = special_cases(val, conversion, 4, 'IV')

        conversion = conversion + 'I' * (val//1)

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

        conversion = 0

        value, cont = convert(roman_num, 'M', 1000)
        conversion = conversion + value
        roman_num = roman_num[cont:]

        value, cont = convert(roman_num, 'D', 500)
        conversion = conversion + value
        roman_num = roman_num[cont:]

        value, cont = special_convert(roman_num, 'C', 100, ['CM', 'CD'], [900, 400])
        conversion = conversion + value
        roman_num = roman_num[cont:]

        value, cont = convert(roman_num, 'L', 50)
        conversion = conversion + value
        roman_num = roman_num[cont:]

        value, cont = special_convert(roman_num, 'X', 10, ['XC', 'XL'], [90, 40])
        conversion = conversion + value
        roman_num = roman_num[cont:]


        value, cont = convert(roman_num, 'V', 5)
        conversion = conversion + value
        roman_num = roman_num[cont:]

        value, cont = special_convert(roman_num, 'I', 1, ['IX', 'IV'], [9, 4])
        conversion = conversion + value
        roman_num = roman_num[cont:]

        return conversion