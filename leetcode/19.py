class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        left=0
        right=sum(nums)
        for i in range(n-1):
            left+=nums[i]
            right-=nums[i]  
            if left>=right : cnt+=1
        return cnt