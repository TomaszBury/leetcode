class Solution:
    def myPow(x: float, n: int) -> float:
        return round(x ** n, 5)
    
x = 2.00000; n = 10
assert Solution.myPow(x,n) == 1024.00000

x = 2.10000; n = 3
assert Solution.myPow(x, n) == 9.26100

x = 2.00000; n = -2
assert Solution.myPow(x, n)