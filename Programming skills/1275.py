def tictactoe(moves: list[list[int]]) -> str:
    wins:list[list[list[int]]] = [
        [[0,0],[1,1],[2,2]],
        [[0,2],[1,1],[2,0]],
        [[0,0],[1,0],[2,0]],
        [[0,1],[1,1],[2,1]],
        [[0,2],[1,2],[2,2]],
        [[0,0],[0,1],[0,2]],
        [[1,0],[1,1],[1,2]],
        [[2,0],[2,1],[2,2]]
        ]
    moves_A:list[list[int]] = moves[::2]
    moves_B:list[list[int]] = moves[1::2]

    who_ended:bool = ""
    if len(moves) % 2 == 0 and len(moves) >= 6:
        who_ended = "B"
    elif len(moves_A) >= 3:
        who_ended = "A"

    solutions_A:list[list[int]] = wins
    solutions_B:list[list[int]] = wins


    if who_ended == "A":
        for wining_solution in solutions_A:
            win:int = 0
            for move in moves_A:
                if move in wining_solution:
                    win += 1
                if win == 3:
                    return "A"
    elif who_ended == "B":
        for wining_solution in solutions_B:
            win:int = 0
            for move in moves_B:
                if move in wining_solution:
                    win +=1
                if win == 3:
                    return "B"
    
    if len(moves) == 9: return "Draw"
    
    return "Pending"



moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
assert tictactoe(moves) == "Draw"

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
assert tictactoe(moves) == "A"

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
assert tictactoe(moves) == "B"

moves = [[0,0],[1,1]]
assert tictactoe(moves) == "Pending"

moves = [[2,2],[1,2],[2,1],[1,1],[2,0]]
assert tictactoe(moves) == "A"

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
assert tictactoe(moves) == "A"

moves = [[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]
assert tictactoe(moves) == "A"

moves = [[1,0],[2,2],[2,0],[0,1],[1,1]]
assert tictactoe(moves) == "Pending"

moves = [[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]
assert tictactoe(moves) == "A"

