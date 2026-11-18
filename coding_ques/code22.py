def countVowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for ch in word:
        if ch in vowels:
            count += 1

    return count
