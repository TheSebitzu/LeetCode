class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary for roman symbols
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0

        prev_value = 0
        # Go from right to left
        for char in reversed(s):
            curr_value = romans[char]
            
            # In case we have IV, IX, ...
            if curr_value < prev_value:
                # Subtract the lesser value (I, in case of V and X, ...)
                sum -= curr_value

            # Otherwise, no special case
            else:
                sum += curr_value

            # Update the current and previous value
            prev_value = curr_value

        return sum