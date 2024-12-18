
def judgeCircle(moves: str) -> bool:
    move:dict[str:int] ={
    "U":90,
    "D":-90,
    "L":-1,
    "R":1,
    }
    result:int = 0
    for mo in moves:
        result += move[mo]
    return result == 0


moves = "UD"
assert judgeCircle(moves) == True
moves = "LL"
assert judgeCircle(moves) == False