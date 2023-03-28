def yield_generator(maximo):
    for i in range(maximo):
        yield i


val = yield_generator(6)
for i in enumerate(val):
    print(i[1])
