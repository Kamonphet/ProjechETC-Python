# fibonacci number => fn = fn-1 + fn-2 โดยfnเริ่มต้น = 0 , 1

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)

for i in range(5):
    print (fibonacci(i))
