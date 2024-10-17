arr = []

def fibonacci(num, cal, k):
    if num <= 1:
        return 1

    ret = fibonacci(num - 1, "A", k + 1) + fibonacci(num - 2, "B", k + 1)

    arr.append({'idx': k, 'val': ret})

    if k == 0:
        arr2 = []
        ks = 0
        for s in arr:
            if s['idx'] > ks:
                ks = s['idx']

        for i in range(ks + 1):
            vals = []
            for s in arr:
                if s['idx'] == i:
                    vals.append(s['val'])

            if len(vals) >= 2:
                for s in vals:
                    if s not in arr2:
                        arr2.append(s)

        arr2.append(1)
        arr2.append(1)
        arr2.reverse()
        arr2.append(ret)

        return arr2

    return ret

seq = fibonacci(10, "C", 0)

print(seq)