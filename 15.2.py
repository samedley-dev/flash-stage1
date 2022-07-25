def expr(x, y, A):
    return (x / 3 + y < 6) or (y - 3 * x > 4) \
           or (abs(x) + abs(y) > A)


ans = None
for A in range(1, 100):
    flag = 1
    for x in range(-100, 100):
        for y in range(-100, 100):
            flag *= expr(x, y, A)
    if flag:
        ans = max(A, ans)
print(ans)
