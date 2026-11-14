class Solution:
    def arraySum(self, arr):
        n = len(arr)
        total = 0

        for i in range(0, n):
            if arr[i] % 2 ==0:
                total += arr[i]
        return total