class Solution:
    def findErrorNums(self, nums):
        d= -1
        for num in nums:
            i= abs(num) - 1
            if nums[i] < 0:
                d = abs(num)
            else:
                nums[i] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return [d, i + 1]