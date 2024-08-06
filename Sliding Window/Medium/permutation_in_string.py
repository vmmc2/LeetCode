from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        windowSize = len(s1)
        s2Len = len(s2)
        answer = False

        s1Freq = defaultdict(int)
        currS2SubstrFreq = defaultdict(int)

        for ch in s1:
            s1Freq[ch] += 1

        for i in range(0, windowSize):
            currS2SubstrFreq[s2[i]] += 1
    
        left, right = 0, windowSize - 1

        while True:
            if s1Freq == currS2SubstrFreq:
                answer = True
                break
            if right == len(s2) - 1:
                break
            currS2SubstrFreq[s2[left]] -= 1
            if currS2SubstrFreq[s2[left]] == 0:
                del currS2SubstrFreq[s2[left]]
            left += 1

            right += 1
            currS2SubstrFreq[s2[right]] += 1

        return answer
