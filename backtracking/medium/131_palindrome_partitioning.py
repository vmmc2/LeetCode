class Solution:
    def isPalindrome(self, s) -> bool:
        n = len(s)
        left = 0
        right = n - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def generatePartitions(self, s, list_of_partitions, answer) -> None:
        if s == "":
            all_partitions_are_palindrome = True
            for partition in list_of_partitions:
                if not self.isPalindrome(partition):
                    return
            answer.append(list_of_partitions)

        for i in range(1, len(s) + 1):
            curr_partition = s[:i]
            self.generatePartitions(s[i:], list_of_partitions + [curr_partition], answer)


    def partition(self, s: str) -> List[List[str]]:
        answer = []
        n = len(s)
        curr_partition = []

        self.generatePartitions(s, [], answer)

        return answer