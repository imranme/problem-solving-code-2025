class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        res = float('inf')
        indices = {mat[i][j]: (i, j)for i in range(len(mat)) for j in range(len(mat[0]))}
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])

        for i in range(len(arr)):
            x, y = indices[arr[i]]
            rows[x] += 1
            cols[y] += 1

            if rows[x] == len(mat[0]):
                return i
            if cols[y] == len(mat):
                return i
        