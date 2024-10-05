class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        
        k = len(nums) - 1
        while i <= k:
            while nums[i] == val and i <= k:
                nums[i], nums[k] = nums[k], nums[i]

                k -= 1
            i += 1
        k += 1
        return k
