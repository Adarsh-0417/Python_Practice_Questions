class Solution:
    def countValidBlocks(self, arr):
        n = len(arr)
        count = 0
        i = 0

        while i < n:
            j = i

            while j < n and arr[j] == arr[i]:
                j += 1

            length = j - i
            value = arr[i]

            if length >= value:
                count += length - value + 1

            i = j

        return count
