v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8]

print(v1 + v2)  # [1, 3, 5, 9, 2, 6, 4, 8]

print(map(lambda x,y: x+y, v1, v2))  # [3, 9, 9, 17]
