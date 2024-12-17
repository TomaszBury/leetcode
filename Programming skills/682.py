import re

def calPoints(operations: list[str]) -> int:
    print("\ncalPoints\n")
    score:list[int] = []
    for i in range(len(operations)):
        operation = operations[i]
        if is_valid_integer(operation):
            score.append(int(operation))
        elif operation == "D":
            score.append(2 * score[-1])
        elif operation == "C":
            score.pop()
        elif operation == "+":
            score.append(score[-1] + score[-2])

        print(f"op:{operation} score:{score}")
            

    print(f"score:{score} score:{sum(score)}")
    return sum(score)

def is_valid_integer(s):
    pattern = r'^[-+]?\d+$'
    return bool(re.match(pattern, s))

ops = ["5","2","C","D","+"]
assert calPoints(ops) == 30

ops = ["5","-2","4","C","D","9","+","+"]
assert calPoints(ops) == 27

ops = ["1","C"]
assert calPoints(ops) == 0

