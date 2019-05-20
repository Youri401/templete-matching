# -*- coding: utf-8 -*-
import cv2

flame = cv2.imread('E:\pubgdata\separate\ImgPositionTrue\H31sanhok298,845,HP52.jpg')
maplist = []
namelist = ['erangel','miramar','sanhok']
maxtemp = 0
mapNumber = 0
maplist.append(cv2.imread('map\\erangel.png'))
maplist.append(cv2.imread('map\\miramar.png'))
maplist.append(cv2.imread('map\\sanhok2.png'))
maptemplate = flame[530:700,1085:1255]
remaptemplate=cv2.resize(maptemplate,(97,97))
hight=remaptemplate.shape[0]
width=remaptemplate.shape[1]
cv2.imwrite("outputMap.png",remaptemplate)
    
# テンプレートマッチング（OpenCVで実装）
for i in range(3):
    match = cv2.matchTemplate(maplist[i], remaptemplate, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    if(maxtemp < max_value):
        maxtemp = max_value
        maxPtTemp = max_pt
        mapNumber = i

# テンプレートマッチングの結果を出力
cv2.rectangle(maplist[mapNumber], (maxPtTemp[0], maxPtTemp[1]), (maxPtTemp[0] + width, maxPtTemp[1] + hight), (0,0,200), 9)
cv2.circle(maplist[mapNumber],(int(maxPtTemp[0]+width/2),int(maxPtTemp[1]+hight/2)),1,(0,200,0), 3)
cv2.imwrite("output2.png", maplist[mapNumber])

print(namelist[mapNumber]+str(int(maxPtTemp[0]+width/2))+','+str(int(maxPtTemp[1]+hight/2)))
