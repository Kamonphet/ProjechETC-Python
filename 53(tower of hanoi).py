#Tower of Hanoi

def Hanoi (n,a,b,c): #(0จำนวน,aย้าย,bไป,cพัก)
    if (n==0):
        return
    Hanoi(n-1,a,c,b) #ย้าย a (ล,ก) -> b | c จุดพัก(ย้ายa,พักc,ไปb)
    print("จานที่ =",n,"จาก =",a,"ไป",c)
    Hanoi(n-1,b,a,c)

Hanoi(3,"A","B","c")