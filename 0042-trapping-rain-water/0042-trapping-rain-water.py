class Solution:
    def trap(self, height: List[int]) -> int:
        height_len = len(height)
        # Left[i] = tallest bar to the left of i
        left = [0] * height_len

        # Right[i] = tallest bar to the right of i
        right = [0] * height_len

        # Find 

        # Left array
        left[0] = height[0]
        for i in range(1, height_len):
            left[i] = max(left[i - 1], height[i])

        # Right array
        right[height_len - 1] = height[height_len - 1]
        for i in range(height_len - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Result
        res = 0
        for i in range(0, height_len):
            res += min(left[i], right[i]) - height[i]

        return(res)
