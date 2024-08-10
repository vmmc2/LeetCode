class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        else:
            canReach = [False for _ in range(n)]
            canReach[0] = True
            globalLargestReachable = None

            for i in range(0, n - 1):
                if canReach[i]:
                    currLargestReachable = i + nums[i]
                    if not globalLargestReachable:
                        globalLargestReachable = currLargestReachable
                        for j in range(i + 1, min(globalLargestReachable + 1, n)):
                            canReach[j] = True
                    elif currLargestReachable > globalLargestReachable:
                        for j in range(globalLargestReachable + 1, min(currLargestReachable + 1, n)):
                            canReach[j] = True
                        globalLargestReachable = currLargestReachable
                else:
                    return False

            return canReach[-1]
