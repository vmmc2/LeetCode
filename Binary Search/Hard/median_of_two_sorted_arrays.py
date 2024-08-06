class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2 # This tells us the total numbers that must be in the left partition of the combined sorted list obtained from 'a' and 'b'.

        if len(b) < len(a):
            a, b = b, a
        
        left, right = 0, len(a) - 1
        while True:
            midA = (left + right) // 2  # This is the index of A's left partition
            midB = half - midA - 2 # This is the index of B's left partition. We need to subtract 2 due to index offset error

            aLeft = a[midA] if midA >= 0 else float("-inf")
            aRight = a[midA + 1] if (midA + 1) < len(a) else float("inf")
            bLeft = b[midB] if midB >= 0 else float("-inf")
            bRight = b[midB + 1] if (midB + 1) < len(b) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 1: # odd length
                    return min(aRight, bRight)
                else: # even length
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                right = midA - 1
            else:
                left = midA + 1
