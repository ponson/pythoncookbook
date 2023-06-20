from collections import ChainMap


a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
#Case 1: 檢查b的型別與merged的型別，發現都是class dict，這有可能是新版python有改的 
# print(type(b))
# merged = dict(b)
# print(type(merged))
# merged.update(a)
# print(f"x={merged['x']}, y={merged['y']}, z={merged['z']}")

b.update(a)
print(f"x={b['x']}, y={b['y']}, z={b['z']}")

#Case 2:
merged = ChainMap(a, b)
print(merged['x'])
a['x'] = 42
print(merged['x'])