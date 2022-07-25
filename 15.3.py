def expr(x, y, A):
    return (y < 2 * x - 4) or (y >= 2 ** x - A) \
           or (pow(x - 1, 2) + pow(y - 3, 2) > 10)


ans, A = None, -100
while ans is None:
    if all(expr(x, y, A) for x in range(-100, 100) \
           for y in range(-100, 100)):
        ans = A
    else:
        A += 1
print(ans)
