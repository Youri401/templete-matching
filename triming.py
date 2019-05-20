# -*- coding: utf-8 -*-
import cv2

im = cv2.imread('E:\pubgdata\separate\HP\H251,P100.jpg',flags=0)
weapon = cv2.imread('sozai\\akm.png')
trimg = im[600:650,580:700]
cv2.imwrite('output2.png',trimg)
pixelValue = trimg[22,70]
trimg[trimg<(pixelValue-30)]=0
trimg[trimg>=(pixelValue+30)]=0
cv2.imwrite('outputWeapon.png',trimg)
print(pixelValue)