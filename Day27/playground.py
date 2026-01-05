def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)



calculate(add=3)