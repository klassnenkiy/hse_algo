s = input()
length = len(s)
palindrome_radius = [1] * (length * 2 + 1)
s = ' ' + ' '.join([char for char in s]) + ' '
right_bound, left_bound = 0, 0
transformed_length = 2 * length + 1

for center in range(1, transformed_length):
    left, right = 0, 0

    if center > right_bound:
        left = right = center
    else:
        mirrored_center = right_bound + left_bound - center
        left = center - palindrome_radius[mirrored_center] + 1
        right = center + palindrome_radius[mirrored_center] - 1

        if right > right_bound:
            delta = right - right_bound
            right -= delta
            left += delta

    while (left - 1 >= 0) and (right + 1 < transformed_length) and s[left - 1] == s[right + 1]:
        left -= 1
        right += 1

    palindrome_radius[center] = right - center + 1

    if right > right_bound:
        right_bound, left_bound = right, left

count_palindromes = 0
for radius in palindrome_radius:
    count_palindromes += radius // 2

print(count_palindromes)
