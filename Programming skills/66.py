def plusOne(digits: list[int]) -> list[int]:
    temp_digit:str = ''.join(map(str, digits))
    temp_digits:int = int(temp_digit) + 1

    return [int(digit) for digit in str(temp_digits)]


digits = [1,2,3]
assert plusOne(digits) == [1,2,4]

digits = [4,3,2,1]
assert plusOne(digits) == [4,3,2,2]

digits = [9]
assert plusOne(digits) == [1,0]