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
            answer.append(list_of_partitions)
            return

        for i in range(1, len(s) + 1):
            # Check to see whether the current partition is a palindrome.
            # If that is not the case, then I can already prune the search tree.
            # When I reach the base case of this recursive function, I already verified
            # that all partitions are palindromes. Therefore, I can safely mark this as
            # an answer.
            curr_partition = s[:i]
            if self.isPalindrome(curr_partition): 
                self.generatePartitions(s[i:], list_of_partitions + [curr_partition], answer)


    def partition(self, s: str) -> List[List[str]]:
        answer = []
        n = len(s)
        curr_partition = []

        self.generatePartitions(s, [], answer)

        return answer