class Solution:
    def armstrongNumber(self, n: int) -> bool:
        num = str(n)
        power = len(num)

        total = 0

        for digit in num:
            total += int(digit) ** power

        if total == n:
            return True
        else:
            return False