class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        k = len(nums)
        # We need to have i - 2 >= 0 so we have i >= 2
        while i >= 2:
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums[i:] = nums[i + 1:] + nums[i:i]
                k -= 1
            i -= 1
        return k