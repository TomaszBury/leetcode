class Solution:
    def diagonalSum(mat: list[list[int]]) -> int:
        sum:int = 0
        for i,j,k,l in zip(range(len(mat)),range(len(mat)),range(len(mat)-1,-1,-1),range(0,len(mat),1)):
            print(f"mat:{mat[i][j]} i:{i} j:{j}")
            print(f"mat:{mat[k][l]} k:{k} l:{l}")
            if (i,j) != (k,l):
                sum += mat[i][j]
                sum += mat[k][l]
            else:
                sum += mat[i][j]
        # print("\n")
        # for i,j in zip(range(len(mat)-1,-1,-1),range(0,len(mat),1)):
        #     print(f"i:{i} j;{j}")
        #     sum += mat[i][j]
        
        print(sum)
        return sum
    

mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
assert Solution.diagonalSum(mat) == 25


mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
assert Solution.diagonalSum(mat) == 8

mat = [[5]]
assert Solution.diagonalSum(mat) == 5