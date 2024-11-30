n, w, l = map(int, input().split())
total_area = w * l
height_events = []

for i in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    block_area = (x2 - x1) * (y2 - y1)
    height_events.append((z1, block_area, i))
    height_events.append((z2, -block_area, i))

height_events.sort()

min_block_count = n + 1
current_covered_area = 0
current_blocks_set = set()

for z, delta_area, block_index in height_events:
    current_covered_area += delta_area
    if delta_area > 0:
        current_blocks_set.add(block_index)
    else:
        current_blocks_set.remove(block_index)

    if current_covered_area >= total_area:
        if len(current_blocks_set) < min_block_count:
            min_block_count = len(current_blocks_set)
            final_blocks = current_blocks_set.copy()

if min_block_count == n + 1:
    print('NO')
else:
    print('YES')
    print(min_block_count)
    for block_index in sorted(final_blocks):
        print(block_index + 1)
