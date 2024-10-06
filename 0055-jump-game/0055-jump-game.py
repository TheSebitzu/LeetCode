class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_power = 0
        for i in range(len(nums)):
            if jump_power < 0:
                return False
            elif nums[i] > jump_power:
                jump_power = nums[i]

            if jump_power > len(nums) - 1 - i:
                return True

            jump_power -= 1

        return True