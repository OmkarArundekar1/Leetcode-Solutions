class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res