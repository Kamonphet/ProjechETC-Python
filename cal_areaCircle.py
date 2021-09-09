'''
โปรแกรมคำนวณพื้นที่วงกลม เมื่อจะหาคำตอบ พิมพ์ cal_area (เส้นผ่านศูนย์กลาง)
'''
def cal_area (diameter) :
    pi = 3.1416
    radius = diameter/2
    area = pi * ( radius **2 )
    print ("diameter cup: {} cm." .format(diameter))
    print ('this is Area of a cup:{:.1f} sq.cm.'.format(area))

