class Solution:
    def spiralOrder(matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        x, y, dx, dy = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "."

            if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        
        return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output = [1,2,3,6,9,8,7,4,5]
assert Solution.spiralOrder(matrix) == Output

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = [1,2,3,4,8,12,11,10,9,5,6,7]
assert Solution.spiralOrder(matrix) == Output

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output = [1,2,3,4,8,12,11,10,9,5,6,7]
assert Solution.spiralOrder(matrix) == Output