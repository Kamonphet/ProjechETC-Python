'''
การใช้งาน python turtle
เป็นเครื่องมือ(module)ชนิดหนึ่งของโปรแกรม python ที่จะทำให้เห็นการเขียนโปรแกรม เป็นรูปแบบภาพวาด
'''
#สั่งใช้งาน python turtle และประกาศฟังก์ชั่นให้เป็นปากกา
import turtle
tao = turtle.pen()

#กำหนดรูปร่างของปากกา EX.เป็นรูปเต๋า
tao.shape('turtle')

#forward() = สั่งให้ไปข้างหน้า (ระยะพิกเซล)
#left() = สั่งให้เลี้ยวซ้าย (องศา)
#right() = สั่งให้เลี้ยวขวา (องศา)
#clear , reset ()= ลบเส้นที่วาดไปแล้ว
#circle() = สั่งให้ไปเป็นวงกลม (ระยะพิกเซล)
#goto() = ไปยังตำแหน่งที่กำหนดเป็น X,Y
#random.choice([])= สุ่มโดยเลือกจาก list
#random.randint () = สุ่มจากเลขจำนวนเต็ม
#penup pendown()= การยกปากกาขึ้นลง
#bgcolor() = เปลี่ยนสีพื้นหลัง
#undo = การย้อนกลับจากเส้นล่าสุด
#stamp() = เพิ่มจำนวนรูปร่างที่เรากำหนด
#การใช้การวนลูปและเรียกฟังก์ชั่นเพื่อวาดรูปได้ง่ายและประหยัดโค้ดมากขึ้น
#Ex.การวาดรูปสี่เหลี่ยม โดยใช้ for loop
for tao in range (4) :
	tao.forward(50)                     #ให้ไปข้่างหน้า 50 พิกเซล
	tao.left(90)                        #ให้เลี้ยวซ้าย 90 องศา


#Ex.การวาดสี่เหลี่ยมหลายขนาด โดยใช้ for loop
for i in range (4) :                        #เป็นฟังก์ชั่นซ้อนฟังก์ชั่น
	for j in range(4) :                 
		tao.forward((i+1)*50)       #ให้ไปข้างหน้าเพิ่มขึ้นจากขนาดรูปแรก * 50
		tao.left (90)

#EX.การวาดรูปสี่เหลี่ยม โดยใช้ def
def rect_size(size=30) :                    #ตั้งชื่อตัวแปลว่า rect_size(กำหนดขนาดเอง/30)
	for i in range (4):
		tao.forward(size)
		tao.left(90)
#-เรียกใช้
print rect_size(size)

#Ex.การวาดวงกลม โดยใช้ for loop
for i in range (20):
	tao.ciecle(50)                     #ให้ไปข้่างหน้าเป็นวงกลม 50 พิกเซล 
	tao.left(20)                       #ให้เลี้ยวซ้าย 90 องศา

#การเรียกใช้สีและการสุ่มสี
#ประกาศตัวแปร
color = ['red','green','blue','yellow']    #มีสีแดง เขียว น้ำเงิน เหลือง
for c in color:
	print(c)
import random
color = ['red','green','blue','yellow']
print (random.choice(color))

#มาลองประยุกต์กับการวาดรูป
for i in range (12):                       #กำหนดให้วนลูป12ครั้ง
	rect_size(80)                      #ฟังก์ชั่นที่เราเขียนไปเเล้วใน def
	clr= random.choice(color)          #ประกาศตัวแปรค่าสีให้เป็ฯการสุ่มสี
	tao.color(clr)                     #ทำให้เส้นมีสี(สุ่มสี)
	tao.circle(80)                     
	tao.left(30)

#การไปยังตำแหน่งที่กำหนด (แต่ยังมีเล้นตามตัวปากกาอยู่)
tao.goto(100,100)	                   #ไปตำแหน่ง x=100 y=100

#การยกปากกาขึ้น,ลง (เพื่อให้ไม่มีเส้นชั่วคราว)
tao.penup()
tao.pendown()

#มาประยุกต์ใช้กัน
for i in range (20):                                #วนลูป 20 ครั้ง
        x = random.randint(-200,200)                #กำหนด x คือแกน x
	y = random.randint(-200,200)                #กำหนด y คือแกน y
	tao.penup()                                 #ยกปากกาขึ้น
	tao.goto(x,y)                               #ให้ปากกาเราไปยังตำแหน่งที่กำหนดใน x,y
	tao.pendown()                               #วางปากกาลง
	color = ['red','green','blue','yellow']     #กำหนดตัวแปรสี
	clr = random.choice(color)                  #กำหนดตัวแปรสุ่มสี
	tao.color(clr)                              #สุ่มสี
	multisize = random.choice([50,100])         #กำหนดตัวแปรสุ่มขนาดตามlistที่เรากำหนด
	rect_size(multisize)                        #ฟังก์ชั่นที่เราเขียนไปเเล้วใน def (การวาดรูปเป็นสี่เหลี่ยมตามขนาดlist)
        tao.circle (multisize)                      #การวาดรูปเป็นวงกลมตามขนาดlist
