MOD = 998244353
MAXN = 200000

# factorial[i] = i! % MOD
fact = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD

# inverse factorial array
inv_fact = [1] * (MAXN + 1)

# Modular inverse of MAXN!
inv_fact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)

# Build inverse factorials backwards
for i in range(MAXN, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


def ncr(n, r):
    if r < 0 or r > n:
        return 0

    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    ans = 0

    for val in range(1, n + 1):
        ans += pow(val - 1, k, MOD) * ncr(n - val, n - k - 1)
        ans %= MOD

    print(ans)

# Time Complexity:
# Precomputation: O(MAXN)
# Per Test Case: O(N log K)
# Overall: O(MAXN + Σ(N log K))

# Space Complexity:
# O(MAXN)
