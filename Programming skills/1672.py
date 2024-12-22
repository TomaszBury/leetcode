
class Solution:
    def maximumWealth(accounts: list[list[int]]) -> int:
        max_value:int = 0
        for i in range(len(accounts)):
            if max_value < sum(accounts[i]):
                max_value = sum(accounts[i])
        
        return max_value


accounts = [[1,2,3],[3,2,1]]
assert Solution.maximumWealth(accounts) == 6