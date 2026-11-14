class Solution:
    def maxSum(self, nums):
        n = len(nums)
        ans = -1

        for i in range(n):
            for j in range(i + 1, n):

                max1 = max(str(nums[i]))
                max2 = max(str(nums[j]))

                if max1 == max2:
                    total = nums[i] + nums[j]
                    ans = max(ans, total)

        return ans
