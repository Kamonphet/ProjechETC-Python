#เช็คจำนวนตัวอักษร
'''
def checkletter (text) :
    result={"a":0,"b":0,"c":0}
    for i in text :
        if "a" in i:
            result["a"]+=1
        elif "b" in i:
            result["b"]+=1
        elif "c" in i:
            result["c"]+=1
        else :
            pass
    return result

text=input("input your text =>")
x= checkletter(text)
print(x)

#เช็คพิมพ์เล็ก-ใหญ่
def checkstring (message):
    result={"UPPER":0,"LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower() :
            result["LOWER"]+=1
        else :
            pass
    return result

message=input("input your message =>")
x=checkstring(message)
print(x)
'''

#ค้นหาเบอร์มือถือ
data={"191":"emergency","1668":"hospital","919":"firecar"}

def searchNumber (message) :
    for key , value in data.items():
        if value==message:
            print ("เบอร์ติดต่อ =",key)
        elif key==message :
            print ("เป็นหมายเลขของ =",value)
        else :
            print("not find")
            return

message=input("input dial or name to contact =>")
searchNumber(message)
