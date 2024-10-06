class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current = None

        for element in nums:
            if count == 0:
                current = element
            if element == current:
                count += 1
            else:
                count -= 1

        return current