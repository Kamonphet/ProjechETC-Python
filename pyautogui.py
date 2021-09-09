'''
การใช้งาน pyautogui แพกเกจควบคุมเมาส์ คียบอร์ด
ติดตั้ง pip install pyautogui
เรียกใช้ import pyautogui
ห้าม run ไว้ดูโ้ค้ดเท่านั้น
'''
#position = ตำแหน่งของเมาส์
#size = ขนาดresolution_จอภาพ
#click = การคลิกของเมาส์
#moveTo = เคลื่อนที่ของเมาส์
#dragTO = ลาก
#duration = ภายในเวลา
#hotkey = กดคีย์ลัด
#press = กดครั้งเดียว
pyautogui.position()
pyautogui.size()
pyautogui.click()
pyautogui.moveTo(x=861, y=456)
pyautogui.drag(x=861, y=456,duration=2)
