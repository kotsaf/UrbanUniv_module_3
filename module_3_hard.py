def allover_sum(n):
    s = 0
    if isinstance(n, (list, set, tuple)):
        for i in n:
            s += allover_sum(i)
    elif isinstance(n, dict):
        for key, value in n.items():
            s += allover_sum(key)
            s += allover_sum(value)
    elif isinstance(n, str):
        s += len(n)
    elif isinstance(n, (int, float)):
        s += n
    return s

n = (
    [[1, 2, 3],
     {'a': 4, 'b': 5},
     (6, {'cube': 7, 'drum': 8}),
     "Hello",
     ((), [{(2, 'Urban', ('Urban2', 35))}])])

result = allover_sum(n)
print(result)