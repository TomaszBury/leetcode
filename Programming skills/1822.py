def arraySign(nums: list[int]) -> int:
    if 0 in nums: return 0

    product:int = 1

    for num in nums:
        product *= num
    
    if product > 0: return 1

    if product < 0: return -1



nums = [-1,-2,-3,-4,3,2,1]

assert arraySign(nums) == 1

nums = [1,5,0,2,-3]
assert arraySign(nums) == 0

nums = [-1,1,-1,1,-1]
assert arraySign(nums) == -1