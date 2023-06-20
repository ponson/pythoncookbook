mylist = [1, 4, -5, 10, -7, 1, 3, -1]
# print([n for n in mylist if n > 0])
genlist = (n for n in mylist if n > 0)

for item in genlist:
    print(item, end=', ')