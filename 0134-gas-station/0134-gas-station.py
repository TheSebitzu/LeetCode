class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_total = 0
        cost_total = 0
        gas_left = 0
        pos_start = 0

        for i in range(len(gas)):
            gas_total += gas[i]
            cost_total += cost[i]

            gas_left += gas[i] - cost[i]

            # Trip failed
            if gas_left < 0:
                # Reset start
                pos_start = i + 1

                # Reset gas
                gas_left = 0

        # If the trip isnt possible
        if gas_total < cost_total:
            return -1
        else:
            # Use this as there is only one solution
            return pos_start