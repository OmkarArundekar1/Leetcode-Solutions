class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                res.append(abs(num))
            else:
                nums[i] *= -1
        return res