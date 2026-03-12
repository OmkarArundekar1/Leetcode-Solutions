class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s,total,c=0,0,0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            total+=diff
            c+=diff
            if c<0:
                s=i+1
                c=0
        return s if total>=0 and s<len(gas) else -1