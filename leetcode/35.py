# https://leetcode.com/problems/search-insert-position/ 

nums = list(map(int,input().split()))
targat = int(input())

for i in range(len(nums)):
    if targat == nums[i]:
        print(i)
