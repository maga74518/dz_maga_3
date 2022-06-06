b = {}

def asdf(*args):
    a = {}
    for i in args:
        x = i[:1]
        b.setdefault(x, [])
        b[x].append(i)
    return b
print(asdf("Иван", "Мария", "Петр", "Илья"))