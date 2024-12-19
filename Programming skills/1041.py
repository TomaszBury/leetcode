class Solution:
    def isRobotBounded(instructions: str) -> bool:
        # position:list[int] = [0,0]
        # direction:str = "North"
        # l_movment:dict[str:str] = {
        #     "North":"West",
        #     "West":"South",
        #     "South":"East",
        #     "East":"North"
        # }
        # r_movment:dict[str:str] = {
        #     "North":"East",
        #     "East":"South",
        #     "South":"West",
        #     "West":"North"
        # }
        # for instruction in instructions:
        #     if instruction in "L":
        #         direction = l_movment[direction]
        #     elif instruction == "R":
        #         direction = r_movment[direction]
        #     elif direction == "North" and instruction == "G":
        #         position[1] += 1
        #     elif direction == "South" and instruction == "G":
        #         position[1] -= 1
        #     elif direction == "East" and instruction == "G":
        #         position[0] += 1
        #     elif position[0] == "West" and instruction == "G":
        #         position[0] -= 1
        # print(f"direction:{direction} position:{position}, intstuctions:{instructions}")
        # if position != [0,0] and direction != "North":
        #     return True 
        # elif position == [0,0] and direction != "North":
        #     return True
        l_turns:int = instructions.count("L")
        r_turns:int = instructions.count("R")
        if l_turns != r_turns and "G" in instructions:
            return True
        elif not "G" in instructions:
            return True
        return False
    

instructions = "GGLLGG"
assert Solution.isRobotBounded(instructions) == True

instructions = "GG"
assert Solution.isRobotBounded(instructions) == False

instructions = "GL"
assert Solution.isRobotBounded(instructions) == True

instructions = "LGR"
assert Solution.isRobotBounded(instructions) == False

instructions = "GLRLLGLL"
assert Solution.isRobotBounded(instructions) == True

instructions = "LLL"
assert Solution.isRobotBounded(instructions) == True

instructions = "RRR"
assert Solution.isRobotBounded(instructions) == True

instructions = "GLGLGGLGL"
assert Solution.isRobotBounded(instructions) == False
