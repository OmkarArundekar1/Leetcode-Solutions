class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin=cmax=r=nums[0]
        l=len(nums)
        for i in range(1,l):
            if nums[i]<0:
                cmax,cmin=cmin,cmax
            cmax=max(nums[i],cmax*nums[i])
            cmin=min(nums[i],cmin*nums[i])
            r=max(cmax,r)
        return r
            