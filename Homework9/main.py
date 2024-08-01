import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount = amount % coin
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    i = amount
    while i > 0:
        for coin in reversed(coins):
            if i >= coin and dp[i] == dp[i - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                i -= coin
                break
    return result


# Testing the functions
print("Greedy Algorithm result: ", end="")
print(find_coins_greedy(113))  # Output: {50: 2, 10: 1, 2: 1, 1: 1}

print("Dynamic Programming Algorithm result: ", end="")
print(find_min_coins(113))  # Output: {1: 1, 2: 1, 10: 1, 50: 2}

test_amounts = [113, 1000, 5678, 12345, 100000]
for amount in test_amounts:
    print(f"\nTesting {amount}:")

    time_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=20)
    print(f"{"Greedy Algorithm:":<30} {"{:.10f}".format(time_greedy)}")

    # print("{:.10f}".format(time_greedy))
    # print("Dynamic Programming Algorithm:", end="")
    time_dp = timeit.timeit(lambda: find_min_coins(amount), number=20)
    print(f"{"Dynamic Programming Algorithm:":<30} {"{:.10f}".format(time_dp)}")
    # print("{:.10f}".format(time_dp))
