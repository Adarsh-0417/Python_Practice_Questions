def growthDays(arr, K):
    count = 0
    previous = None

    for num in arr:
        if num == 0:
            continue

        if previous is not None:
            if num >= previous + K:
                count += 1

        previous = num

    return count