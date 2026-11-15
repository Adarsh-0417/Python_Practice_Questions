
def tallest_tree(trees):
    if not trees:
        return -1

    max_height = 0

    for feet, inches in trees:
        height = feet * 12 + inches
        if height > max_height:
            max_height = height

    return max_height

n = int(input())
trees = []
for i in range(n):
    feet, inches = map(int, input().split())
    trees.append((feet, inches))

result = tallest_tree(trees)

print(result)
