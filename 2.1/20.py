# Мухи отдельно, котлеты отдельно

N, M, K1, K2 = map(int, (input() for i in range(4)))

a = N * (M - K1) // (K2 - K1)

print(N - a, a)