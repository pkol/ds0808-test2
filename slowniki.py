def suma(*args):
    s = 0
    d = {1:3, 4:'kotek'}
    for i in args:
        s += i+1
    return s

def kroczaco(n):
    """ta funkcja coś na pewno policzy"""
    k = []
    for i in range(n):
        k.append(suma(*list(range(i))))
    print(k)

kroczaco(6)
a=45
