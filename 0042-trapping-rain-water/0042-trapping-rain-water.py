class Solution:
    def trap(self, height: List[int]) -> int:
        # Left[i] = tallest bar to the left of i
        left = [0] * len(height)

        # Right[i] = tallest bar to the right of i
        right = [0] * len(height)

        # Find 

        # Left array
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])

        # Right array
        right[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Result
        res = 0
        for i in range(0, len(height)):
            res += min(left[i], right[i]) - height[i]

        return(res)
