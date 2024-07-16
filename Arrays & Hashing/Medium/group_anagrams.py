class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [ ]
        sortedAnagrams = [ ]

        for i in range(0, len(strs)):
            sortedString = sorted(strs[i])
            if i == 0:
                anagrams.append( [strs[i]] )
                sortedAnagrams.append(sortedString)
            else:
                hasFoundGroup = False
                for j in range(0, len(sortedAnagrams)):
                    if sortedString == sortedAnagrams[j]:
                        hasFoundGroup = True
                        anagrams[j].append(strs[i])
                        break
                if hasFoundGroup == False:
                    anagrams.append( [strs[i]] )
                    sortedAnagrams.append(sortedString)

        return anagrams
