a = slice(5, 50, 2)
print(a)
s = "Hello! Welcome to fantasy novels."
a.indices(len(s)) #沒作用
print(a)
for i in range(*a.indices(len(s))):
    print(s[i])