def plus_minus_conversion(s):
    """replaces all occurrences of 'plus' with '+' and all occurrences of 'minus' with '-'"""
    if isinstance(s, str):
        operators = {
            'plus': '+',
            'minus': '-'
        }
        for op, symbol in operators.items():
            if op in operators:
                s = s.replace(op, symbol)
        return s
    else:
        return 'Your input is not a string type!'


print(plus_minus_conversion('minusplusminus'))
print(plus_minus_conversion(5))
print(plus_minus_conversion(['1','2','3']))
print(plus_minus_conversion('plusminusminusplus'))
