class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        n = len(intervals)

        if n == 0:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        idx = 0

        while idx < n:
            if newInterval[0] > intervals[idx][1]:
                answer.append(intervals[idx])
                if idx + 1 < n and newInterval[0] < intervals[idx + 1][0] and newInterval[1] < intervals[idx + 1][0]:
                    answer.append(newInterval)
                    idx += 1
                    break
            else: # Found the merge point
                mergedInterval = [None, None]
                mergedInterval[0] = min(newInterval[0], intervals[idx][0])
                mergedInterval[1] = max(newInterval[1], intervals[idx][1])

                idx += 1

                while idx < n and mergedInterval[1] > intervals[idx][1]:
                    idx += 1
                
                if idx < n and mergedInterval[1] >= intervals[idx][0]:
                    mergedInterval[1] = max(mergedInterval[1], intervals[idx][1])
                    idx += 1

                answer.append(mergedInterval)
                break

            idx += 1
       
        return answer + intervals[idx:]
