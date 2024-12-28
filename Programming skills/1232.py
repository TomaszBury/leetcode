class Solution:
    def checkStraightLine(coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        print(f"({coordinates[1][1]} - {coordinates[0][1]}) / ({coordinates[1][0]} - {coordinates[0][0]})")
        print(f"{(coordinates[1][1] - coordinates[0][1]) }/ {(coordinates[1][0] - coordinates[0][0])}")
        # print((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]))
        if (coordinates[1][0] - coordinates[0][0]) != 0:
            slope:float = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for i in range(1,len(coordinates)):
                print(f"slope:{slope} ({coordinates[i-1][1]} -{ coordinates[i][1]} / {coordinates[i-1][0]} - {coordinates[i][0]}")
                if (coordinates[i-1][0] - coordinates[i][0]) == 0:
                    return False
                if slope != (coordinates[i-1][1] - coordinates[i][1]) / (coordinates[i-1][0] - coordinates[i][0]):
                    return False
                else:
                    slope = (coordinates[i-1][1] - coordinates[i][1]) / (coordinates[i-1][0] - coordinates[i][0])
        else:
            x:bool = True
            y:bool = True
            print(coordinates)
            for i in range(1,len(coordinates)):
                if coordinates[i][0] != coordinates[i-1][0]:
                    x = False
                    
                if coordinates[i][1] != coordinates[i-1][1]:
                    y = False
                    
            print(f"x:{x} y:{y}")
            return x or y

        return True

coordinates = [[1,2],[2,3]]
assert Solution.checkStraightLine(coordinates) == True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
assert Solution.checkStraightLine(coordinates) == True

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
assert Solution.checkStraightLine(coordinates) == False

coordinates = [[0,0],[0,1],[0,-1]]
assert Solution.checkStraightLine(coordinates) == True

coordinates = [[1,1],[2,2],[2,0]]
assert Solution.checkStraightLine(coordinates) == False

coordinates = [[0,0],[0,5],[5,5],[5,0]]
assert Solution.checkStraightLine(coordinates) == False