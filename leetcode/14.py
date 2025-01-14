class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ln = len(A)
        flag = [0] * (ln+1)
        res = []
        count = 0
        for i in range(0, ln):
            flag[A[i]]+=1
            if flag[A[i]] == 2:
                count+=1
            flag[B[i]]+=1
            if flag[B[i]]==2:
                count+=1
            res.append(count)
        return res
        