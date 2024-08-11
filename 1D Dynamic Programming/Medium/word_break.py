class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True # Base case of the DP (Supposing I got to the end of the word).

        wordDict.sort(key=lambda word: len(word))
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]: # If we have found a way to word break, we can go to the next index.
                    break

        return dp[0]
