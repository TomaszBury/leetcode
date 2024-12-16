def toLowerCase(s: str) -> str:
    return s.lower()


s = "Hello"
assert toLowerCase(s) == "hello"

s = "here"
assert toLowerCase(s) == "here"
s = "LOVELY"
assert toLowerCase(s) == "lovely"