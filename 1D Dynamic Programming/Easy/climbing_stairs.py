class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            numDistinctWays = [0 for i in range(n + 1)]
            for i in range(n + 1):
                if i == 1:
                    numDistinctWays[i] = 1
                elif i == 2:
                        numDistinctWays[i] = 2
                elif i >= 3:
                    numDistinctWays[i] = numDistinctWays[i - 1] + numDistinctWays[i - 2]

        return numDistinctWays[n]
