# from faker import Faker

# fake = Faker()
# print(fake.email())
# print(fake.country())
# print(fake.name())
# print(fake.text())
# print(fake.latitude(),fake.longitude())
# print(fake.url())

row = 1 #row คือ ตัวแปรที่ใช้เก็บค่า แถว 1-12
while row <= 12:
    num = 2 #num คือ ตัวแปรที่ใช้เก็บค่า แม่สูตรคูณ
    col = 1 #col คือ ตัวแปรที่ใช้เก็บค่า คอลัมน์ 1-6
    while col <= 6: #while นี้ใช้กำหนดการแสดงแถว
        print("%3dx%2d=%3d" % (num, row, num * row), end="")
        num += 1
        col += 1
 
    print("")
    row += 1
 
print(" ")
 
row = 1
while row <= 12: #while ที่ 2 จะแสดงคอลัมน์
    num = 8
    col = 1
    while col <= 6:
        print("%3dx%2d=%3d" % (num, row, num * row), end=" ")
        num += 1
        col += 1
 
    print(" ")
    row += 1