#เกมทายลูกเต๋า

'''
หลักการคิดคือ การทายเลขโดยการสุ่ม โดยจะนำฟังก์ชัน import คือการนำ pugin ของโปรแกรม python มาใช้ นั่นคือ random
และตั้งเงื่อนไขที่ให้ผู้ใช้ป้อนเลขเพื่อมาทายเลขที่ถูกโปรแกรม random อยู่ 
'''

import random

#print(myrandom)
myrandom = random.randrange(1,7)
k=1
correct=False
print("มีโอกาสตอบ 3 ครั้ง")
while True :
    number=int(input("ป้อนค่าลูกเต่าที่คุณต้องจะทาย :"))
    correct=(number==myrandom)
    if number <0 or number>=7 :
        break
    if not correct :
        if(number>myrandom) :
            print("น้อยกว่า")
        if(number<myrandom) :
            print("มากกว่า")
    if correct :
        print ("ถูก")
        break
    if k==3 :
        break
    k+=1
if not correct :
    print("ผิดๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆๆ")
print("เฉลย = ", myrandom)
