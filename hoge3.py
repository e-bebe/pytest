def double(x):
    return x * x

a = [2, 5, 8]
print map(double, a)

print map(lambda x:x * x, a)
