'''
# เรียงลำดับตัวเลข

number = []
while True:
    x = int(input("ป้อนตัวเลข = "))
    if x < 0:
        break
    number.append(x)
print("ก่อนเรียง =", number)
number.sort()  # คำสั่งsort ไว้เรียงน้อยไปมาก
print("หลังเรียงจากน้อยไปมาก =", number)
number.reverse() #คำสั่งreverse ไว้เรียงมากไปน้อย
print("หลังเรียงจากมากไปน้อย =", number)

#เรียงค่าตัวเลขต่ำสุง-สูงสุด
#ใช้ min-max ในการระบุเลขต่ำ-สูง
print ("ค่าที่น้อยที่สุด =", min(number))
print ("ค่าที่มากที่สุด =", max(number))

#ผมรวม ใช้ sum
print("ผลรวม =", sum(number))


# หากลุ่มเลขคู่-คี่

number = []
odd = []
even = []
while True:
    x = int(input("ป้อนตัวเลข = "))
    if x < 0:
        break
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    number.append(x)

print("เลขในlist = ", number)
print("เลขคู่ = ", even)
print("เลขคี่ = ", odd)


# เรียงลำดับชื่อ
student = ["เพชร", "ก้อง", "พิง", "จี", "ภูมิ"]
print(student)

student.sort()
print(student)

#เรียงสมาชิกจากหลังสุด -> หน้าสุด
fruit = ["มะม่วง" , "มะนาว" , "ทุเรียน" , "กล้วย"]
print(fruit)
fruit=fruit[::-1] #ให้list แสดงข้อมูลจากข้างหลังสุดก่อน
print(fruit)
'''
