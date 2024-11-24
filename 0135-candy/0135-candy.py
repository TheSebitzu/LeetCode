class Solution:
    def candy(self, ratings: List[int]) -> int:

        # Initialize candy list
        candy = [1] * len(ratings)

        # Iterate from left to right
        for i in range(1, len(ratings)):

            # Compare ratings
            if ratings[i] > ratings[i - 1]:

                # Increase candy to left_candy + 1
                candy[i] = candy[i - 1] + 1

        # Iterate from right to left
        for i in range(len(ratings) - 2, -1, -1):

            # Compare ratings
            if ratings[i] > ratings[i + 1]:

                # Increase candy to right_candy + 1 or keep it the same
                candy[i] = max(candy[i + 1] + 1, candy[i])

        return(sum(candy))