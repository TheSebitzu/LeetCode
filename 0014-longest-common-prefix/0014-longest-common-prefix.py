class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Zip *strs give us a matrix with with the letters of every word
        (f,f,f)
        (l,l,l)
        (o,o,i)
        (w,w,g)

        Enumerate give use the indexes of every group.
        Use set to remove duplicates.
        If there is more than 1 element in the set,
        we stop and print the previous one.
        '''

        
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                # Return first word up to the i-th letter
                return strs[0][:i]

        # If we dont find a mismatch
        # Return the shortest word in strings
        return min(strs, key=len)