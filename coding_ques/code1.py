def ans(nums):
    sum = 0

    for i in range(len(nums)):
        modified = nums[i]

        modified -= (i % 7) * 3

        if nums[i] % 11 == 0:
            modified += nums[i] // 11

        print(modified, end=" ")
        sum += modified

    return sum


nums = [22, 5, 14]
result = ans(nums)

print()
print("Total Sum", result)