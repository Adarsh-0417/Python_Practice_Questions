
def prefixSum(arr):
    total = 0
    result = []

    for num in arr:
        total += num
        result.append(total)

    return result


arr = [1, 2, 3, 4]
print(prefixSum(arr))
