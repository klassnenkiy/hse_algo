num_caps, caps = int(input()), list(map(int, input().split()))
caps.sort()
num_shirts, shirts = int(input()), list(map(int, input().split()))
shirts.sort()
num_pants, pants = int(input()), list(map(int, input().split()))
pants.sort()
num_boots, boots = int(input()), list(map(int, input().split()))
boots.sort()

min_color = min(caps[0], shirts[0], pants[0], boots[0])
max_color = max(caps[0], shirts[0], pants[0], boots[0])
min_diff = abs(max_color - min_color)

cap_idx = shirt_idx = pant_idx = boot_idx = 0
best_cap, best_shirt, best_pants, best_boots = cap_idx, shirt_idx, pant_idx, boot_idx

while cap_idx < num_caps and shirt_idx < num_shirts and pant_idx < num_pants and boot_idx < num_boots:
    current_colors = [caps[cap_idx], shirts[shirt_idx], pants[pant_idx], boots[boot_idx]]
    current_min = min(current_colors)
    current_max = max(current_colors)
    current_diff = current_max - current_min

    if current_diff < min_diff:
        min_diff = current_diff
        best_cap, best_shirt, best_pants, best_boots = cap_idx, shirt_idx, pant_idx, boot_idx

    # если равна 0 - наилучший комплект
    if current_diff == 0:
        break

    # двигаем указатель на мин эл
    if current_min == caps[cap_idx]:
        cap_idx += 1
    elif current_min == shirts[shirt_idx]:
        shirt_idx += 1
    elif current_min == pants[pant_idx]:
        pant_idx += 1
    else:
        boot_idx += 1

print(caps[best_cap], shirts[best_shirt], pants[best_pants], boots[best_boots])
