class Solution:
    def setZeroes(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cortiantes:list[tuple[int:int]] = []
        rows, columns = len(matrix), len(matrix[0])

        # Total number of elements in the matrix
        total_elements = rows * columns

        # Iterate over each element using a single index
        for index in range(total_elements):
            # Calculate row and column from the flat index
            i = index // columns  # row index
            j = index % columns   # column index
            if matrix[i][j] == 0:
                cortiantes.append((i,j))

        for i,j in cortiantes:
            for column in range(columns):
                matrix[i][column] = 0
            for row in range(rows):
                matrix[row][j] = 0
                
        return matrix



matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output = [[1,0,1],[0,0,0],[1,0,1]]
assert Solution.setZeroes(matrix) == Output

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
assert Solution.setZeroes(matrix) == Output



        