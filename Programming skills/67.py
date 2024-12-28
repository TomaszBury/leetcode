class Solution:
    def addBinary(a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
    

a = "11"; b = "1"
assert Solution.addBinary(a,b) == "100"

a = "1010"; b = "1011"
assert Solution.addBinary(a,b) == "10101"