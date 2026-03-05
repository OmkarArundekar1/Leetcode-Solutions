class Solution:
    def sos(self,n:int) -> int:
        return sum(int(digit)**2 for digit in str(n))

    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.sos(n)
        while fast!=1 and slow!=fast:
            slow=self.sos(slow)
            fast=self.sos(self.sos(fast))
        return fast==1
          