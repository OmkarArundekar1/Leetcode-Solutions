class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dd=defaultdict(int)
        for each in s:
            dd[each]+=1
        for each in dd:
            if dd[each]!=dd[s[0]]:
                return False
        return True
        