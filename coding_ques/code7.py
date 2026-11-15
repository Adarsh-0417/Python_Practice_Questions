class Solution:
    def missingEven(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1)

        actual_sum = sum(nums)

        return expected_sum - actual_sum
