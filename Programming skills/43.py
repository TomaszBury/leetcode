class Solution:
    def multiply(num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
    
num1 = "2"; num2 = "3"
assert Solution.multiply(num1, num2) == "6"

num1 = "123"; num2 = "456"
assert Solution.multiply(num1, num2) == "56088"