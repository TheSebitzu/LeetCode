class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        length = len(s)

        count = 0
        for i in range(length - 1, -1, -1):
            # Break at the "last" space
            if s[i] == " ":
                break
            count += 1

        return count