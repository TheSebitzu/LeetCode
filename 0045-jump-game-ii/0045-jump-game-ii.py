class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        max_pos = 0
        max_range = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            max_pos = max(i + nums[i], max_pos)
            if i == max_range:
                steps += 1
                max_range = max_pos

                if max_range >= len(nums) - 1:
                    break
        return steps