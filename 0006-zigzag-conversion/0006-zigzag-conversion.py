class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If one row, there is no zigzag
        if numRows == 1:
            return s
        
        # We go down so need to add 1 to row_count
        direction = 1 # down
        row_count = 0

        # Make numRows empty strings
        rows = [""] * numRows

        for c in s:
            # Put every character in right row
            rows[row_count] += c

            # Increment or decrement, depending on direction
            row_count += direction

            # If all the way down or all the way up, change direction
            if row_count == 0 or row_count == numRows - 1:
                direction *= -1

        # Join rows to get output
        return "".join(rows)