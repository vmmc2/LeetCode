class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = { }
        
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        kvPairs = [(value, key) for key, value in freqDict.items()]
        kvPairs = sorted(kvPairs)
        kvPairs.reverse()
        kvPairs = kvPairs[ : k]
        answer = [pair[1] for pair in kvPairs]

        return answer
