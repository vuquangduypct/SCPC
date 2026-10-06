'''Alp loves carrots. Since he hasn't eaten lunch yet, he wants to buy a carrot salad to eat outside. However, he has a weird obsession: all the carrots must be the exact same length; otherwise, the salad doesn't look aesthetically pleasing to him. Since he is in the middle of the street and doesn't have a knife, he can't cut the carrots himself. You need to divide all the carrots using your machine and sell them to Alp.

You are given n
 delicious carrots with sizes a1,a2,…,an
. You are also given a cutting machine, which works as follows.

For each operation, you choose a set of carrots (you can choose chopped carrots again) and a positive integer x
 (not necessarily the same for each operation).
After that, consider every chosen carrot, let its length be l
. If l <= x
, this carrot is unaffected; otherwise, it is divided into two carrots of sizes x
 and l-x
.
We'll sell some of the final carrots to an interesting guy who wants them all to be the same length.

We are asking you to determine the maximum number of carrots we can sell after using this machine exactly k
 times. Solve the problem for only k=1
.'''

def carrot_chopdown(n, k, carrots):
    if k != 1:
        raise ValueError("This function only supports k=1.")
    
    max_carrots = 0
    for x in range(1, max(carrots) + 1):
        count = 0
        for carrot in carrots:
            if carrot >= x:
                count += carrot // x
        max_carrots = max(max_carrots, count)
    
    return max_carrots

print (carrot_chopdown(5, 1, [4, 5, 6, 7, 8]))  # Example usage
print (carrot_chopdown(3, 1, [10, 15, 20]))  # Example usage
