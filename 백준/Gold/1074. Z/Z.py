def z_search(N, x, y):
    if N == 1:
        return 2 * x + y
    xd, xr = divmod(x, (2 ** (N - 1)))
    yd, yr = divmod(y, (2 ** (N - 1)))
    base = (2 * xd + yd) * (2 ** (2 * N - 2))
    return base + z_search(N - 1, xr, yr)

N, x, y = map(int, input().split())
print(z_search(N, x, y))