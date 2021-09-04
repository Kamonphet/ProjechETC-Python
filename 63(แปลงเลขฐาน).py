#convert decimal_number โปรแกรมแปลงเลขฐาน

def decimal_number(number):
    print("The decimal value of",number,"is :")
    print(bin(number), "in binary.")
    print(oct(number), "in octal.")
    print(hex(number), "in hexadecimal.")

def binary_number(number):
    print("The binary value of",number,"is :")
    print(oct(number), "in octal.")
    print(hex(number), "in hexadecimal.")

def octal_number(number):
    print("The octal value of",number,"is :")
    print(bin(number), "in binary.")
    print(hex(number), "in hexadecimal.")

def hexadecimal_number(number):
    print("The hexadecimal value of",number,"is :")
    print(bin(number), "in binary.")
    print(oct(number), "in octal.")

decimal_number(10)