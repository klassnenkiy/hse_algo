def is_valid_width(road_width, cracked_x_coords, prefix_min_y, prefix_max_y, suffix_min_y, suffix_max_y):
    last_uncovered = 0
    for current_right in range(num_cracked):
        while cracked_x_coords[last_uncovered] <= cracked_x_coords[current_right] - road_width:
            last_uncovered += 1

        if last_uncovered != 0:
            max_y_in_prefix = prefix_max_y[last_uncovered - 1]
            min_y_in_prefix = prefix_min_y[last_uncovered - 1]
        else:
            max_y_in_prefix = -1
            min_y_in_prefix = height + 1

        if current_right != num_cracked - 1:
            max_y_in_suffix = suffix_max_y[current_right + 1]
            min_y_in_suffix = suffix_min_y[current_right + 1]
        else:
            max_y_in_suffix = -1
            min_y_in_suffix = height + 1

        max_y = max(max_y_in_suffix, max_y_in_prefix)
        min_y = min(min_y_in_suffix, min_y_in_prefix)
        if max_y - min_y + 1 <= road_width:
            return True
    return False

width, height, num_cracked = map(int, input().split())

cracked_tiles = []
for _ in range(num_cracked):
    cracked_tiles.append(tuple(map(int, input().split())))
cracked_tiles.sort()

cracked_x_coords = []
cracked_y_coords = []
for i in range(num_cracked):
    cracked_x_coords.append(cracked_tiles[i][0])
    cracked_y_coords.append(cracked_tiles[i][1])

prefix_max_y = [cracked_y_coords[0]]
prefix_min_y = [cracked_y_coords[0]]
for i in range(1, num_cracked):
    prefix_max_y.append(max(prefix_max_y[i - 1], cracked_y_coords[i]))
    prefix_min_y.append(min(prefix_min_y[i - 1], cracked_y_coords[i]))

suffix_max_y = [0] * num_cracked
suffix_min_y = [0] * num_cracked
suffix_min_y[-1] = cracked_y_coords[-1]
suffix_max_y[-1] = cracked_y_coords[-1]
for i in range(num_cracked - 2, -1, -1):
    suffix_max_y[i] = max(suffix_max_y[i + 1], cracked_y_coords[i])
    suffix_min_y[i] = min(suffix_min_y[i + 1], cracked_y_coords[i])

left, right = 0, min(height, width)
while right - left > 1:
    middle = (left + right) // 2
    if is_valid_width(middle, cracked_x_coords, prefix_min_y, prefix_max_y, suffix_min_y, suffix_max_y):
        right = middle
    else:
        left = middle

print(right)
