def ratFood(r, unit, arr):

    if arr is None:
        return -1

    required_food = r * unit
    total = 0

    for i in range(len(arr)):
        total += arr[i]

        if total >= required_food:
            return i + 1

    return 0
