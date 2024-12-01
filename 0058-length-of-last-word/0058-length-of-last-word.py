class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        Strip whitespace
        Split into words
        Return the last one
        '''
        return len(s.strip().split()[-1])