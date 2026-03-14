class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[1]*len(nums)
        ans = 1
        for i in range(len(nums)):
            for l in range(i):
                if nums[l]<nums[i]:
                    if res[l]+1>res[i]:
                        res[i]=res[l]+1
            ans=max(ans,res[i])
        return ans

            
        