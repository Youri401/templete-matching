# -*- coding: utf-8 -*-

import cv2


def main():
    # 入力画像とテンプレート画像をで取得
    # im = cv2.imread("output.jpg")
    #temp = cv2.cvtColor(cv2.imread(r'sozai\scar.png'), cv2.COLOR_RGB2GRAY)
    im = cv2.imread(r'C:\Users\kengo\Downloads\470.png')
    #temp[temp<1]=0
    #temp[temp>=1]=255
    
    temp = cv2.imread(r'C:\Users\kengo\Downloads\4693.png')
    #trimg = im[600:650,580:700]
    #pixelValue = trimg[25,70]
    #trimg[trimg<(pixelValue-15)]=0
    #trimg[trimg>=(pixelValue+15)]=0


    # テンプレート画像の高さ・幅
    h, w,t = temp.shape
    
    # テンプレートマッチング（OpenCVで実装）
    match = cv2.matchTemplate(im, temp, cv2.TM_CCOEFF_NORMED)
    min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    pt = min_pt
    
    # テンプレートマッチングの結果を出力
    cv2.rectangle(im, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0,0,200), 3)
    cv2.imwrite("output2.png", im)
    
    print(max_value)

if __name__ == "__main__":
    main()