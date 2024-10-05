class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0

        j = 0

        k = 0

        if m == 0:
            nums1[:] = nums2[:]
        elif n:
            while i < m + n and j < n:
                if nums1[i] <= nums2[j] and any(value != 0 for value in nums1[i:]):
                    k += 1
                elif nums1[i] > nums2[j]:
                    nums1[i + 1 : m + n] = nums1[i : m + n - 1]
                    nums1[i] = nums2[j]
                    j += 1
                elif not nums1[i] and k == m:
                    nums1[i] = nums2[j]
                    j += 1
                i += 1