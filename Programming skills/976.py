class Solution:
    def try_wird(nums:list[int]) -> int:
        nums.sort()
        # print(f"\nnums:{nums}")
        for i in range(len(nums)-1,-1,-1):
            a = nums[i-2]
            b = nums[i-1]
            c = nums[i]
            # print(f"a:{a} b:{b} c:{c} {a + b > c and a+c > b and c+b > a} i:{i} sum:{a + b + c}")
            if a + b > c and a+c > b and c+b > a:
                return a + b + c
        # print("Are we returning zero.")
        return 0
        

print("Solution:\n---------------------------------------------------------------------")

nums = [2,1,2]
assert Solution.try_wird(nums) == 5

nums = [1,2,1,10]
assert Solution.try_wird(nums) == 0

nums = [1,2,2,2,1,10]
assert Solution.try_wird(nums) == 6

nums = [3,4,15,2,9,4]
assert Solution.try_wird(nums) == 11