def isMonotonic(nums:list[int]) -> bool:
    incresing:list[bool] = []
    decreasing:list[bool] = []

    for i in range(1,len(nums)):
        if nums[i-1] >= nums[i]:
            incresing.append(True)
        else:
            incresing.append(False)

        if nums[i-1] <= nums[i]:
            decreasing.append(True)
        else:
            decreasing.append(False)

    return all(incresing) or all(decreasing)



nums = [1,2,2,3]
assert isMonotonic(nums) == True

nums = [6,5,4,4]
assert isMonotonic(nums) == True

nums = [1,3,2]
assert isMonotonic(nums) == False