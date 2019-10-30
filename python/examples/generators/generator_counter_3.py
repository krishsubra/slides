def counter():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for c in counter():
    print(c)
# 1
# 2
# 3
