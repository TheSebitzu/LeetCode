class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort in ascending order
        nums.sort()
        i = 0
        end = len(nums) - 1
        n = len(nums)
        length = 1
        maj_elem = nums[0]
        while i < end:
            if nums[i] == nums[i + 1]:
                length += 1
                if length > int(n/2):
                    maj_elem = nums[i]
                    break
            else:
                length = 1
            i += 1
        return maj_elem