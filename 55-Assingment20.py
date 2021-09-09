# โปรแกรมบัญชีธนาคาร

# data
account = {"นายA": 5000, "นายB": 0}


def getBalance():
    print("ยอดเงินคงเหลือในบัญชี :", account)


def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ระบุจำนวนเงินเป็นตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("เงินที่ฝากต้องมากกว่า 0 บาท")
    print("ฝากเงินเช้าบัญชี A :", money)
    account["นายA"] += money


def withdraw(money):
    if not type(money) is int:
        raise Exception("ระบุจำนวนเงินเป็นตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("เงินที่ถอนต้องมากกว่า 0 บาท")
    if money > account["นายA"]:
        raise Exception("ยอดเงินในบัญชีไม่พอสำหรับการถอนเงิน")
    print("ถอนเงินออกจากบัญชี A :", money)
    account["นายA"] -= money


def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ระบุจำนวนเงินเป็นตัวเลขเท่านั้น")
    if money <= 0:
        raise Exception("เงินที่โอนต้องมากกว่า 0 บาท")
    if money > account["นายA"]:
        raise Exception("ยอดเงินในบัญชีไม่พอสำหรับการโอนเงิน")
    print("ทำการโอนเงินไปที่บัญชี B :", money)
    account["นายB"] += money
    account["นายA"] -= money


try:
    getBalance()
    transfer(50.50)
    getBalance()
except Exception as e:
    print(e)
