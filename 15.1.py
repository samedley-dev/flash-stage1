def expr(x, a1, a2):
    return (81 <= x <= 112) <= ((not (7 <= x <= 97)) <= (a1 <= x <= a2))


min_len = float("inf")
for a1 in range(1, 500):
    for a2 in range(a1 + 1, 500):
        if all(expr(x, a1, a2) for x in range(1, 500)):
            min_len = min(min_len, a2 - a1)
print(min_len)
