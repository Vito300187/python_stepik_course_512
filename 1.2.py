objects = [1, 0, 30, 31, True, False, 1, 0, 30, 32]
list2 = []
ans = 0

for obj in range(len(objects)):
    if objects[obj] not in list2:
        list2.append(objects[obj])
        ans += 1
print(ans)
