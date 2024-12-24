import copy


class Solution:
    def spiralOrder(matrix: list[list[int]]) -> list[int]:
        all_elements:list[int] = []
        left_rigth:bool = True

        total_lenght:int = sum([len(line) for line in matrix])

        for _ in range(total_lenght):
            
            for i,sublist in enumerate(matrix):
                print(f"i:{i}, sublist:{sublist} all_elements:{all_elements}")
                if i == 0 and sublist != all_elements[0:3]:
                    all_elements.extend(sublist)
                elif left_rigth and i != 0 and i != len(matrix) -1 :
                    left_rigth = False
                    all_elements.append(sublist[-1])
                    print(f"right:{sublist[-1]}")
                elif left_rigth == False and i != 0 and i != len(matrix) -1 :
                    left_rigth = True
                    all_elements.append(sublist[0])
                    print(f"Left:{sublist[0]}")
            
        return all_elements



matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output = [1,2,3,6,9,8,7,4,5]
assert Solution.spiralOrder(matrix) == Output

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = [1,2,3,4,8,12,11,10,9,5,6,7]
assert Solution.spiralOrder(matrix) == Output

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Output = [1,2,3,4,8,9,13]
assert Solution.spiralOrder(matrix) == Output