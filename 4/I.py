def calculate_votes(party_index, parties, suffix_sum, threshold):
    # бипоиск для определения первого столба с голосами >= threshold
    l, r = -1, num_parties
    while r - l > 1:
        mid = (l + r) // 2
        if parties[mid][0] < threshold:
            l = mid
        else:
            r = mid

    additional_votes_needed = suffix_sum[r] - (num_parties - r) * threshold
    if parties[party_index][0] > threshold:
        additional_votes_needed -= (parties[party_index][0] - threshold)
    return additional_votes_needed


def simulate(party_index, parties, suffix_sum):
    # бипоиск по уровню стрижки голосов
    l, r = 0, max_votes + 1
    while r - l > 1:
        threshold = (l + r) // 2
        additional_votes_needed = calculate_votes(party_index, parties, suffix_sum, threshold)

        if additional_votes_needed + parties[party_index][0] > threshold:
            l = threshold
        else:
            r = threshold

    additional_votes_needed = calculate_votes(party_index, parties, suffix_sum, l)
    surplus_votes = max(0, (parties[party_index][0] + additional_votes_needed) - (l + 2))

    return additional_votes_needed - surplus_votes, l, surplus_votes

num_parties = int(input())
parties = []
bribe_costs = []
max_votes = 0
for i in range(num_parties):
    current_votes, bribe_cost = map(int, input().split())
    max_votes = max(max_votes, current_votes)
    parties.append([current_votes, i])
    bribe_costs.append(bribe_cost)
parties.sort()

# суффиксные суммы для быстрого подсчёта голосов над уровнем threshold
suffix_sum = [0] * (num_parties + 1)
suffix_sum[-2] = parties[-1][0]
for i in range(num_parties - 2, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + parties[i][0]

# поиск минимальной суммы для подкупа и агитации
min_total_cost = float('inf')
for i in range(num_parties):
    if bribe_costs[parties[i][1]] != -1:  # партии, которые можно подкупить
        additional_votes_needed, threshold, surplus_votes = simulate(i, parties, suffix_sum)
        total_cost = bribe_costs[parties[i][1]] + additional_votes_needed

        if total_cost < min_total_cost:
            min_total_cost = total_cost
            optimal_party = [parties[i][1], additional_votes_needed, threshold, surplus_votes]

# восстановление итогового распределения голосов
winning_party_index = optimal_party[0]
additional_votes_needed = optimal_party[1]
threshold = optimal_party[2]
surplus_votes = optimal_party[3]
final_votes = [0] * num_parties

for i in range(num_parties):
    if parties[i][1] == winning_party_index:
        final_votes[parties[i][1]] = parties[i][0] + additional_votes_needed
    elif parties[i][0] > threshold:
        if surplus_votes > 0:
            final_votes[parties[i][1]] = threshold + 1
            surplus_votes -= 1
        else:
            final_votes[parties[i][1]] = threshold
    else:
        final_votes[parties[i][1]] = parties[i][0]

print(min_total_cost)
print(winning_party_index + 1)
print(*final_votes)
