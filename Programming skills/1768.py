def mergeAlternately(word1: str, word2: str) -> str:
        result:str = ""
        for w_1, w_2 in zip(word1,word2):
                result += w_1 + w_2

        if len(word1) > len(word2):
                result += word1[len(word2):]
        elif len(word2) > len(word1):
                result += word2[len(word1):]
        return result

word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))