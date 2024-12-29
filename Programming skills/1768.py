def mergeAlternately(word1: str, word2: str) -> str:
        result:str = ""
        for w_1, w_2 in zip(word1,word2):
                result += w_1 + w_2

        if len(word1) > len(word2):
                result += word1[len(word2):]
        elif len(word2) > len(word1):
                result += word2[len(word1):]
        return result

word1 = "abc"; word2 = "pqr"

assert mergeAlternately(word1, word2) == "apbqcr"

word1 = "ab"; word2 = "pqrs"
assert mergeAlternately(word1, word2) == "apbqrs"

word1 = "abcd"; word2 = "pq"
assert mergeAlternately(word1, word2) == "apbqcd"