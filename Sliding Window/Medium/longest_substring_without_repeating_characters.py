from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        n = len(s)

        left, right = 0, 0
        answer = ""

        while right < n:
            if left == right:
                freq[s[right]] += 1
                answer = s[left:right+1]
            else:
                freq[s[right]] += 1
                canUpdate = True
                for ch, count in freq.items():
                    if count > 1:
                        canUpdate = False
                        break
                if canUpdate:
                    if len(s[left:right+1]) > len(answer):
                        answer = s[left:right+1]
                else:
                    freq[s[left]] -= 1
                    left += 1
            right += 1

        return len(answer)
