def knapsack_max_biodiversity(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for w in range(capacity + 1):
            if wi > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], vi + dp[i - 1][w - wi])

    chosen = []
    w = capacity
    i = n
    while i > 0:
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i)
            w -= weights[i - 1]
        i -= 1

    chosen.reverse()
    return dp[n][capacity], chosen

weights = [6, 4, 5, 3, 7]
values = [1600, 1000, 1800, 1200, 2000]
capacity = 18

best_score, chosen_items = knapsack_max_biodiversity(weights, values, capacity)
print(best_score)
print(chosen_items)
