class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        cuts = [0]*n
        for i in range(n):
            cuts[i] = i
        for end in range(n):
            for start in range(end+1):
                if s[start] == s[end] and (end-start <= 2 or dp[start+1][end-1]):
                    dp[start][end] = True

                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(cuts[end], cuts[start-1] + 1)

        return cuts[-1]