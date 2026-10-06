"""Alice and Bob are playing a game with three piles of stones. Initially, Alice has a
 stones, Bob has b
 stones, and the third pile contains c
 stones.

Alice and Bob take turns, with Alice going first. On each turn, the current player may take any number of stones from the third pile, possibly zero, and add them to their own pile.

If both players take zero stones on two consecutive turns, the game ends.

Let A
 and B
 be the final numbers of stones Alice and Bob have, respectively. The score of the game is |A-B|
.

Alice wants to maximize the score, while Bob wants to minimize it. Assuming both players play optimally, find the final score."""

def three_piles(a, b, c):
    # If the total number of stones is even, the score will be 0
    if (a + b + c) % 2 == 0:
        return 0
    else:
        # If the total number of stones is odd, the score will be 1
        return 1


print(three_piles(4, 5, 2))  # Output: 0 or 1 depending on the values of a, b, and c

