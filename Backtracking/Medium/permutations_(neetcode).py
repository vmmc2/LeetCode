class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        answer = []
        for perm in perms:
            for i in range(0, len(perm) + 1):
                p_copy = perm.copy()
                p_copy.insert(i, nums[0])
                answer.append(p_copy)

        return answer
