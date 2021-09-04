# จับคู่คำทักทาย
'''
greeting = ["สวัสดี", "HI", "hello", "goodbye"]
people = ["เพชร", "ฟิล์ม", "พ่อแม่"]
result = []

for i in greeting:
    for j in people:
        result.append(i+j)
print(result)

# อีกวิธี
result = [i+j for i in greeting for j in people]
print(result)
'''
# จับคู่สินค้าและราคา
fruit = ["แตงโม", "กีวี", "ฝรั่ง"]
price = [50, 30, 15]

for x,y in zip(fruit,price[::-1]) :
    print("สินค้า =",x ,"ราคา =", y)