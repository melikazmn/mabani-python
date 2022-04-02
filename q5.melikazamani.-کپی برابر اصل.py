def deepcopy(l):
    if type(l[0]) != list:
        return [l[0]]
    return  deepcopy[l[0]] + deepcopy(l[1:])

def check(a, b):
    if type(a) is int and type(b) is int:
        return a == b

    for x, y in zip(a, b):
        if (type(x) is type(y) is list and id(x) == id(y)) or \
        not check(x, y):
            return False

    return True



a = [0, 1, [2, [[], 4]]]
b = deepcopy(a)
print(check(a, b))
