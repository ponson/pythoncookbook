a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}


b = {
    'w' : 12,
    'x' : 11,
    'y' : 2
}

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
c = {key:a[key] for key in a.keys() - ['z', 'w']}
print(c)