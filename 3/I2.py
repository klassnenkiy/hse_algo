num_caps, caps = int(input()), sorted(map(int, input().split()))
num_shirts, shirts = int(input()), sorted(map(int, input().split()))
num_pants, pants = int(input()), sorted(map(int, input().split()))
num_boots, boots = int(input()), sorted(map(int, input().split()))

cap_idx = shirt_idx = pant_idx = boot_idx = 0
min_diff = float('inf')
best_cap, best_shirt, best_pants, best_boots = -1, -1, -1, -1

while cap_idx < num_caps and shirt_idx < num_shirts and pant_idx < num_pants and boot_idx < num_boots:
    # тек эл
    current_caps = caps[cap_idx]
    current_shirts = shirts[shirt_idx]
    current_pants = pants[pant_idx]
    current_boots = boots[boot_idx]

    # мин и макс эл
    current_min = min(current_caps, current_shirts, current_pants, current_boots)
    current_max = max(current_caps, current_shirts, current_pants, current_boots)
    current_diff = current_max - current_min

    if current_diff < min_diff:
        min_diff = current_diff
        best_cap, best_shirt, best_pants, best_boots = cap_idx, shirt_idx, pant_idx, boot_idx

    #мин разн 0 - комплект найден
    if current_diff == 0:
        break

    #перемещ указ на мин эл
    if current_min == current_caps:
        cap_idx += 1
    elif current_min == current_shirts:
        shirt_idx += 1
    elif current_min == current_pants:
        pant_idx += 1
    else:
        boot_idx += 1

print(caps[best_cap], shirts[best_shirt], pants[best_pants], boots[best_boots])
