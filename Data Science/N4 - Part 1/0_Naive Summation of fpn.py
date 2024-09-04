N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
# print(sum(N))


def alg_sum(x):  # x == x[:n]
    s = 0.
    for x_i in x:  # x_0, x_1, \ldots, x_{n-1}
        s += x_i
    return s


# print(alg_sum(N))
t = [0.0] * len(N)
n = 0.1
# print(x)

for i in range(len(N)):
  # print(i)
  t[i]=(N[i] * n)
print(t)

