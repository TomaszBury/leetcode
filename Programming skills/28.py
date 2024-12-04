def strStr(haystack: str, needle: str) -> int:
    if len(haystack) == len(needle) and haystack == needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        print(f"i:{i} needle:{needle} == haystack[i:len(needle):{haystack[i:len(needle)]} len(needle):{len(needle)}")
        if needle == haystack[i: i+len(needle)]:
            return i
     
    return -1


haystack = "sadbutsad"
needle = "sad"

assert strStr(haystack, needle) == 0

haystack = "leetcode"
needle = "leeto"

assert strStr(haystack, needle) == -1

haystack = "hello"
needle = "ll"

assert strStr(haystack, needle) == 2

haystack = "a"
needle = "a"

assert strStr(haystack, needle) == 0

haystack = "abc"
needle = "c"

assert strStr(haystack, needle) == 2