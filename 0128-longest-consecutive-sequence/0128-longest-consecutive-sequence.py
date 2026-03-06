class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = defaultdict(int)
        r = 0
        for i in nums:
            if not (m[i]):
                m[i]=m[i-1]+m[i+1]+1
                m[i-m[i-1]]=m[i]
                m[i+m[i+1]]=m[i]
                r = max(r,m[i])
        return r
        