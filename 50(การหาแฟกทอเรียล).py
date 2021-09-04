# แฟกทอเรียล => n!= n * n = N
def factorial(number):
    if number == 1:
        return number
    elif number <1 :
        pass
    else:
        return number * factorial(number-1)


x = factorial(-6)
print(x)
