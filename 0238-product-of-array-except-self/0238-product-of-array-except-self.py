class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        p=1
        for i in range(n):
            res[i]=p
            p*=nums[i]
        s=1
        for j in range(n-1,-1,-1):
            res[j]*=s
            s*=nums[j]
        return res
