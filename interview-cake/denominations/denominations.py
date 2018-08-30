from typing import Tuple


def count_combinations1(
        amount: int, denominations: Tuple[int], combinations: int = 0,
        current_combo: tuple = None
        ):
    """
    denominations is assumed to be sorted.

    """
    # print(amount, denominations, combinations, current_combo)
    current_combo = current_combo or tuple()

    for idx, coin in enumerate(denominations):
        if coin > amount:
            # won't find any additional combinations
            return combinations

        fit_times = amount // coin
        other_coins = denominations[idx + 1:]

        for multiplier in range(1, fit_times + 1):
            remainder = amount - (coin * multiplier)
            this_combo = current_combo + ((coin,) * multiplier)

            # print(this_combo)
            if remainder == 0:
                # print(amount, coin, fit_times, multiplier, remainder)
                print(this_combo)
                combinations += 1
                break

            combinations = count_combinations1(
                remainder, other_coins, combinations, this_combo)

    return combinations


print(count_combinations1(6, (1, 2, 3)))
