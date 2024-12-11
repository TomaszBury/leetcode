def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    progression:float = arr[0] - arr[1]
    progression_current:float = 0
    for i in range(2, len(arr)):
        progression_current = arr[i-1] - arr[i]
        if progression != progression_current:
            return False
        else:
            progression = progression_current

    return True

arr = [3,5,1]
assert canMakeArithmeticProgression(arr) == True

arr = [1,2,4]
assert canMakeArithmeticProgression(arr) == False

