class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""] * numRows
        if numRows == 1:
            return s
        strs = [s[i:i + (numRows - 1) * 2] for i in range(0, len(s), (numRows - 1) * 2)]

        for s in strs:
            if len(s) != (numRows - 1) * 2:
                s += " " * ((numRows - 1) * 2 - len(s))
            rows[0] += s[0]
            first = 1
            last = len(s) - 1
            row = 1
            while row != numRows and first <= last:
                if first == last:
                    rows[row] += s[first]
                else:
                    rows[row] += s[first] + s[last]
                rows[row] = rows[row].strip()
                first += 1
                last -= 1
                row += 1

        return "".join(rows)