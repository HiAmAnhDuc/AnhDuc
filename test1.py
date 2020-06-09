def char_to_int(c):
    if not isinstance(c, str):
        raise TypeError("Not a string")
    
    if len(c) >= 2:
        raise ValueError("Not a single digit")
    
    return ord(c)


def string_to_int(s):
    if not isinstance(s, str):
        raise TypeError("Not a string")
    for i in s:
        if not isinstance(i, int):
            raise ValueError("Not a positive integer string expression")
    
def is_palindrome(value):
    
    content = list(value)    
    check = True

    while len(content) > 0 and check:       
        if content[0] != content[(len(content) - 1)]:
            check = False
        else:
            content.pop(0)
            if len(content) > 0:
                content.pop((len(content) - 1))

    return check

def roman_numeral_to_int(roman_numeral):
    if not isinstance(roman_numeral, str):
        raise TypeError("Not a string")
    

    for i in roman_numeral:
        if i != 'N' and i != 'I' and i != 'V' and i != 'X' and i != 'L' and i != 'C' and i != 'D' and i != 'M':
            raise ValueError("Not a Roman numeral")
        
    rm = {'N':0, 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0;
    for i,c in enumerate(roman_numeral):
        if (i + 1) == len(roman_numeral) or rm[c] >= rm[roman_numeral[i + 1]]:
            result += rm[c]
        else:
            result -= rm[c]
    return result

print(roman_numeral_to_int("XYZ"))