#สร้างตารางหมากฮอส

'''
หลักการคิดคือ เรานำความรู้จากการวาดภาพสี่เหลี่ยมมาใช้ โดยเราาจะแทนสีให้เหมือนกับตารางหมากฮอส ดังนี้
x= สีน้ำตาล
o= สีขาว
จากนั้นก็ไปเพิ่มเงื่อนไข if โดยแยกว่าถ้าเป็นเลขคู่ให้แสดง " o " ถ้าเป็นเลขคี่ให้แสดง " x "
'''

number=int(input("ป้อนขนาด = "))

for row in range (number) :
    for column in range (number) :
        if (row+column)%2==0 :
           print("o",end="") 
        else :
            print("x",end="")
    print(" ")
print('เป็นสี่เหลี่ยมขนาด =',number,'x',number)
print("ขนาดของสี่เหลี่ยมจัตุรัสนี้ = ",number*number)
print("จบโปรแกรม")

#สร้างขอบตาราง

#นำเงื่อนไขจากเหตุการณ์ที่แล้วโดยจะทำการเลือกให้ x แสดงผลตามที่เรากำหนดในเงื่อนไข if เท่านั้น
'''
xxxx
x  x
x  x
x  x
x  x
xxxx
'''
for row in range (number) :
    for column in range (number) :
        if row==0 or row==number-1 or column==0 or column==number-1 :
            print("x",end="")
        else :
            print(" ",end="")
    print(" ")
print(" ")
print('เป็นสี่เหลี่ยมขนาด =',number,'x',number)
print("ขนาดของสี่เหลี่ยมจัตุรัสนี้ = ",number*number)
print("จบโปรแกรม")
