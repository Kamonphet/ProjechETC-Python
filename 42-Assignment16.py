# กลุ่มสมาชิกเลขยกกกำลัง

number = [1, 2, 3, 4, 5, 6, 7]
print(number)
for i in range(len(number)):
    number[i] = number[i]**2
print(number)

# อีกวิธี
number = [i*i for i in number]
print(number)
