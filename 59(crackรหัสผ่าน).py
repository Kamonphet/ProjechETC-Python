#แครกรหัสผ่าน
def crackpassword (ATM_password) :
    import random
    result="" #สำหรับเก็บผลลัพธ์

    while result!=ATM_password :
        result=""
        for letter in range(len(ATM_password)):
            list_number=random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            result="".join(list_number)+str(result)
            print("search =>",result)
    print("CRACK PASSWORD IS =>",result)

crackpassword("10")