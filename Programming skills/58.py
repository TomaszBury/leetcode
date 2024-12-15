def lengthOfLastWord(s: str) -> int:
    # last_word:str = s.strip()
    # index:int = last_word.rfind(" ") + 1
    return len(s.strip()[s.strip().rfind(" ") + 1:])




s = "Hello World"
assert lengthOfLastWord(s) == 5

s = "   fly me   to   the moon  "
assert lengthOfLastWord(s) == 4

s = "luffy is still joyboy"
assert lengthOfLastWord(s) == 6