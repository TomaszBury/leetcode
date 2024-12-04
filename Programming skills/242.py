def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)



s = "anagram"
t = "nagaram"

assert isAnagram(s, t) == True

s = "rat"
t = "car"

assert isAnagram(s, t) == False