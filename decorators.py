def decorator(func):
    def decorated(a,b):
        if a > 0 and b > 0:
            return func(a,b)
        else:
            print('error')
    return decorated


@decorator
def triangle(a, b):
    return 1/2 * a * b


@decorator
def square(a, b):
    return a*b

res = triangle(10, -10)
print(res)

