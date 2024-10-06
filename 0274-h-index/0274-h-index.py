class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        i = n - 1
        while i >= 0:
            if citations[i] >= n - i:
                h = n - i
            i -= 1
        return h