N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
s = N * M

for w1 in range(N):
    if (w1 * K1 + (N - w1) * K2) == s:
        print(w1, N - w1)
        break