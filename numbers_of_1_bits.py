n = 11
ans = 3

n = 128
ans = 1

n = 2147483645
ans = 30

# straight forward solution
# res = 0

# while n:
#     res += n % 2
#     n //= 2

# print(ans == res)

# bit manipulation solution
res = 0

while n:
    res += 1
    n &= n - 1

    """
    remove the last 1 bit from n
    10001
    10000
    -----
    10000
    01111
    -----
    00000
    """

print(ans == res)