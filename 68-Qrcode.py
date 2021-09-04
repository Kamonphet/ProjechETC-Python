def CreatQrCode (link,name) :
    import png
    import pyqrcode
    import os
    url = pyqrcode.create(link)
    creat = url.png(name,scale= 6)
    os.system(name)

CreatQrCode('https://drive.google.com/file/d/1BNqVjF_r4lGbisMkQ10DnLdCEDQcUkyw/view?usp=sharing','QrcodeTest.png')