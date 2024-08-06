class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        nums.sort()
        validTriplets = {}

        i = 0
        while i <= n - 3:
            left, right = i + 1, n - 1

            while left <= right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if (i != left and i != right and left != right) and ((nums[i], nums[left], nums[right]) not in validTriplets):
                        validTriplets[(nums[i], nums[left], nums[right])] = True
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
            i += 1

        for triplet, presence in validTriplets.items():
            answer.append([triplet[0], triplet[1], triplet[2]])

        return answer
