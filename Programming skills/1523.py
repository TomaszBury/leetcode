class Solution:
    def countOdds(low: int, high: int) -> int:
        odds:int = high - low
        if odds % 2 == 0 and low % 2 != 0:
            print(odds / 2 + 1)
            return int(odds / 2 + 1)
        elif odds % 2 == 0 :
            print(odds / 2)
            return int(odds / 2)
        else:
            print(f"odds:{odds} {int((odds -1 ) /2 + 1):,}")
            return int((odds -1 ) /2 + 1)
        


low:int = 3; high:int = 7
assert Solution.countOdds(low,high) == 3

low:int = 8; high:int = 10
assert Solution.countOdds(low,high) == 1

low:int = 800445804; high:int = 979430543
assert Solution.countOdds(low,high) == 89492370