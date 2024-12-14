

def romanToInt(s: str) -> int:
    romans:dict[str:int] = {
                        "I":1,
                        "V":5,
                        "X":10,
                        "L":50,
                        "C":100,
                        "D":500,
                        "M":1000
                        }
    number:int = 0
    letter:str = ""
    for i in range(len(s)):
        letter = s[i]
        number += romans[letter]
        if letter == "M" and s[i-1] == "C" and i-1 >= 0:
            number -= 200
        elif letter == "C" and s[i-1] == "X" and i-1 >= 0:
            number -= 20
        elif letter == "D" and s[i-1] == "C" and i-1 >= 0:
            number -= 200
        elif letter == "L" and s[i-1] == "X" and i-1 >= 0:
            number -= 20
        elif letter == "X" and s[i-1] == "I" and i-1 >= 0:
            number -= 2
        elif letter == "V" and s[i-1] == "I" and i-1 >= 0:
            number -= 2
            
     
    return number
s = "MMMCDXC"
assert romanToInt(s) == 3490

s = "III"
assert romanToInt(s) == 3

s = "LVIII"
assert romanToInt(s) == 58

s = "MCMXCIV"
assert romanToInt(s) == 1994

s = "IX"
assert romanToInt(s) == 9

s = "MCDLXXVI"
assert romanToInt(s) == 1476