

def a():
    x = {'a':2}
    y=100
    return x,y


z = a()

print(type(z))
print(z[0]['a'])