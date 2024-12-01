class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        Strip whitespace, split in words, then reverse the words string
        '''
        return " ".join(s.strip().split()[::-1])