import heapq

n = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

total_cost = 0.0

while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    cost = first + second
    total_cost += cost * 0.05
    heapq.heappush(arr, cost)

print(f"{total_cost:.2f}")


#2 version TL

n = int(input())
arr = list(map(int, input().split()))

nums = {}

for num in arr:
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

cost = 0.0

while True:
    if len(nums) < 2 and list(nums.values())[0] < 2:
        break

    first_val = min(nums)
    if nums[first_val] > 1:
        pairs_count = nums[first_val] // 2
        nums[first_val] %= 2

        if first_val * 2 in nums:
            nums[first_val * 2] += pairs_count
        else:
            nums[first_val * 2] = pairs_count

        cost += first_val * pairs_count * 2

        if nums[first_val] == 0:
            del nums[first_val]
        continue

    if len(nums) > 1:
        second_val = min(k for k in nums if k != first_val)

        cost += first_val + second_val
        nums[second_val] -= 1

        if nums[second_val] == 0:
            del nums[second_val]

        new_val = first_val + second_val
        if new_val in nums:
            nums[new_val] += 1
        else:
            nums[new_val] = 1

        del nums[first_val]

print(f"{cost * 0.05:.2f}")
