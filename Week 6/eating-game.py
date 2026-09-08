def possible_winners(a):
    n = len(a)

    # Total number of dishes
    total = sum(a)

    # If there are no dishes, nobody wins.
    if total == 0:
        return 0

    # A player can be the winner if their number of dishes
    # is large enough to survive until the final round.
    #
    # The final dish must be eaten by a player who still has
    # a dish when all other players have exhausted theirs.

    max_dishes = max(a)

    winners = 0

    for x in a:
        if x == max_dishes:
            winners += 1

    return winners

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(possible_winners(a))

