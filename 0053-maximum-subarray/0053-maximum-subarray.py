class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs=res=nums[0]
        for i in nums[1:]:
            res=max(res+i,i)
            maxs=max(res,maxs)
        return maxs 