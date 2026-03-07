class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars=set()
        len=0
        for c in s:
            if c in chars:
                chars.remove(c)
                len+=2
            else:
                chars.add(c)
        if chars:
            len+=1
        return len