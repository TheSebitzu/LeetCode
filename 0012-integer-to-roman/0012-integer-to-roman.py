class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        # Empty string for result
        result = ""

        # From big to low
        for key in reversed(numbers.keys()):

            # If num can still be written as roman numerals
            while num >= key:

                # Subtract the biggest roman numeral possible
                num -= key

                # Append the letter/s to the result
                result += numbers[key]

        return(result)