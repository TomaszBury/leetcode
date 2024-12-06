def moveZeroes(nums: list[int]) -> list[int]:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    non_zero:list[int] = [x for x in nums if x != 0]
    zeros:list[int] = [0] * (len(nums) - len(non_zero))
        
    return non_zero + zeros



nums = [0,1,0,3,12]

assert moveZeroes(nums) == [1,3,12,0,0]

nums = [0]
assert moveZeroes(nums) == [0]

nums = [0,0,1]
assert moveZeroes(nums) == [1,0,0]

