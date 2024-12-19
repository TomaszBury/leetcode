class Solution:
    def isRobotBounded(instructions: str) -> bool:
        position:list[int] = [0,0]
        direction:str = "North"
        
        l_movment:dict[str:str] = {
            "North":"West",
            "West":"South",
            "South":"East",
            "East":"North"
        }

        r_movment:dict[str:str] = {
            "North":"East",
            "East":"South",
            "South":"West",
            "West":"North"
        }

        for instruction in instructions:
            print(f"direction:{direction} position:{position}, intstuctions:{instruction}")
            if instruction in "L":
                direction = l_movment[direction]
            elif instruction == "R":
                direction = r_movment[direction]
            elif direction == "North" and instruction == "G":
                position[1] += 1
            elif direction == "South" and instruction == "G":
                position[1] -= 1
            elif direction == "East" and instruction == "G":
                position[0] += 1
            elif direction == "West" and instruction == "G":
                position[0] -= 1

        print(f"direction:{direction} position:{position}, intstuctions:{instructions}")

        if position != [0,0] and direction != "North":
            return True 
        elif position == [0,0]:
            return True

        # l_turns:int = instructions.count("L")
        # r_turns:int = instructions.count("R")

        # if "G" in instructions:
        #     print(f"l truns:{l_turns} r turns:{r_turns} r-l:{l_turns - r_turns} ratio:{(l_turns-r_turns)/instructions.count("G")}")
        #     print(f"g:{instructions.count("G")}")

        # if "G" in instructions and l_turns - r_turns > 0:
        #     if (l_turns - r_turns) / instructions.count("G") % 0.5 == 0:
        #         return True
        
        # if l_turns + r_turns == len(instructions):
        #     return True 

        return False
    

instructions = "GGLLGG"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True

instructions = "GG"
print(f"instrutcions:{instructions} {False}")
assert Solution.isRobotBounded(instructions) == False

instructions = "GL"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True

instructions = "LGR"
print(f"instrutcions:{instructions} {False}")
assert Solution.isRobotBounded(instructions) == False

instructions = "GLRLLGLL"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True

instructions = "LLL"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True

instructions = "RRR"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True

instructions = "GLGLGGLGL"
print(f"instrutcions:{instructions} {False}")
assert Solution.isRobotBounded(instructions) == False

instructions = "GLRLGLLGLGRGLGL"
print(f"instrutcions:{instructions} {True}")
assert Solution.isRobotBounded(instructions) == True
