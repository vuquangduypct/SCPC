''' A subarray is a continuous part of array.

One of our SCPC execs, Ryan (aka Lim Zi-Heng), recently found an array a
 of n
 elements and became very interested in finding the maximum sum of a non empty subarray. However, Ryan doesn't like consecutive integers with the same parity, so the subarray he chooses must have alternating parities for adjacent elements.

For example, [1,2,3] is acceptable, but [1,2,4]is not, as 2 and 4 are both even and adjacent.

You need to help Ryan by finding the maximum sum of such a subarray.

Input
The first line contains an integer t
 (1≤t≤104)
 — number of test cases. Each test case is described as follows.

The first line of each test case contains an integer n
 (1≤n≤2⋅105)
 — length of the array.

The second line of each test case contains n
 integers a1,a2,…,an
 (-103≤ai≤103)
 — elements of the array.

It is guaranteed that the sum of n
 for all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the answer to the problem.
'''

import sys

def find_max_alternating_subarray_sum(array):
    max_sum = float('-inf')
    current_sum = 0
    last_parity = None

    for num in array:
        current_parity = num % 2
        if last_parity is None or current_parity != last_parity:
            current_sum += num
            last_parity = current_parity
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = num
            last_parity = current_parity

    for _ in range(number_of_digit):
            n = int(input())
            array = list(map(int, input().split()))
            result = find_max_alternating_subarray_sum(array)
            print(result)
    
    max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    number_of_digit = int(sys.argv[1])
    array = sys.argv[2:2+number_of_digit]
    print(find_max_alternating_subarray_sum(array))
