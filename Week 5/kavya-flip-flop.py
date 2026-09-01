'''Our vice-president, Kavya, set up a battle with n
 monsters in order to increase his combat power. Each monster has a combat power ai
 and Kavya has a combat power of c
. He has k
 flip flops and can perform the following operations:

Kill an alive monster i
 if ai≤c
; then c
 becomes c+ai
.
Throw a flip flop at an alive monster i
; the flip-flop will be broken and the monster will become angrier, then ai
 becomes ai+1
.
Help Kavya obtain the maximum possible c  
 after the battle.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains three integers n
, c
 and k
 (1≤n≤100
, 0≤c,k≤109
).

The second line contains n
 integers a1,a2,…,an
 (0≤ai≤109
).

Output
For each test case, output an integer — the maximum possible combat power.'''

def kavya_battle(t, test_cases):
    results = []
    for case in test_cases:
        n, c, k, a = case
        a.sort()
        for i in range(n):
            if a[i] <= c:
                c += a[i]
            elif k > 0:
                k -= 1
                a[i] += 1
                if a[i] <= c:
                    c += a[i]
            else:
                break
        results.append(c)
    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []
    for _ in range(t):
        n, c, k = map(int, input().split())
        a = list(map(int, input().split()))
        test_cases.append((n, c, k, a))
    
    results = kavya_battle(t, test_cases)
    for result in results:
        print(result)

