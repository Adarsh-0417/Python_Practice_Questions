class Solution:
    def reverseString(self, s):
        arr = []

        for ch in s:
            if ch.isalpha():
                arr.append(ch)

        arr.reverse()

        result = []
        index = 0

        for ch in s:
            if ch.isalpha():
                result.append(arr[index])
                index += 1
            else:
                result.append(ch)

        return ''.join(result)
