# -*- coding: utf-8 -*-
import cv2

restHp = 0
im = cv2.imread('E:\pubgdata\separate\ImgTrue2\C1242akm.jpg',flags=0)
trimg = im[684:700,503:778]
cv2.imwrite('output2.png',trimg)
hpPixelValue = trimg[8,0]
trimg[trimg<(hpPixelValue-50)]=0
trimg[trimg>=(hpPixelValue+50)]=0
cv2.imwrite('output.png',trimg)
for i in range (100):
    if((trimg[0,int(i*2.75)] < (hpPixelValue+50))&(trimg[0,int(i*2.75)]>hpPixelValue-50)):
        restHp = (i+1)
        continue
    else: break;
print(restHp)