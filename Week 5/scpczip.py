'''Let f(s)
 be the compressed version of a string s
, formed by replacing every maximal contiguous block of identical characters with a single copy of that character. For example, f(
"aabbcc") = 
"abc".

Let |s|
 denote the length of a string s
. Following this, |f(s)|
 denotes the length of the compressed string. For example:

|f("aabbcc")|=|"abc"| =3
If the string is empty, its length is 0
.
Richard has given you a string s
 consisting of n
 lowercase Latin letters. You must delete exactly one character s_i
 (2≤i≤n-1
) to form a new string s'
, and then find the minimum possible value of |f(s')|
.

Note that you cannot delete s1
 or sn
.

Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases.

The first line of each test case contains an integer n
 (3≤n≤2⋅105
) — the length of the string.

The second line of each test case contains a string s
 (|s|=n
), consisting of lowercase Latin letters.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the minimum possible length of the resulting compressed string after deleting one character.

'''

def min_compressed_length(s):
    n = len(s)
    min_length = float('inf')

    for i in range(1, n - 1):
        new_s = s[:i] + s[i + 1:]
        compressed_length = len(f(new_s))
        min_length = min(min_length, compressed_length)

    return min_length

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        result = min_compressed_length(s)
        print(result)

