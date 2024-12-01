class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        # Empty string for result
        result = ""

        # From big to low (wrote the dict like this)
        for key in numbers.keys():

            # If num can still be written as roman numerals
            while num >= key:

                # Subtract the biggest roman numeral possible
                num -= key

                # Append the letter/s to the result
                result += numbers[key]

        return(result)