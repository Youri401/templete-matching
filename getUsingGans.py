# -*- coding: utf-8 -*-

import os
import cv2


def main():
    templeteList = []
    weaponNameIndex =[]
    fileNameTmp=""
    weaponNameTmp=""
    maxTmp = 0
    indexNumber=1
    
    
    # 入力画像とテンプレート画像をで取得
    for file in os.listdir(r'sozai'):           #子ディレクトリsozaiのデータを取得
        for num in os.path.splitext(file):      #取得したデータを拡張子とそれ以外で分割
                fileNameTmp += num              #ファイルの名前を一時格納
                if(num != ".png"):              #ファイルの名前が武器の名前なら
                    weaponNameTmp+=num;         #一時格納
        weaponNameIndex.append(weaponNameTmp)   #武器の名前リストに保存
        imgTmp=cv2.cvtColor(cv2.imread('sozai\\'+fileNameTmp),cv2.COLOR_RGB2GRAY)
        imgTmp[imgTmp<1]=0
        imgTmp[imgTmp>=1]=255
        templeteList.append(imgTmp) #ファイルを取得しグレースケールにしてテンプレートマッチングリストに保存
        fileNameTmp=""      #一時格納変数を初期化
        weaponNameTmp=""

    #im = cv2.imread('E:\sozai2\sozai4.jpg',flags=0)
    im = cv2.imread('D:\separate\ImgTrue2\C4459qbu.jpg',flags=0)
    trimg = im[600:650,580:700]
    pixelValue1 = trimg[21,70]               #銃の真ん中付近の画素値を取得        
    pixelValue2 = trimg[23,70]               #銃の真ん中付近の画素値を取得
    if(pixelValue1 < pixelValue2):
        pixelValue = pixelValue2
    else:
        pixelValue = pixelValue1
    trimg[trimg<(pixelValue-40)]=0
    trimg[trimg>=(pixelValue+40)]=0
    
        # テンプレート画像の高さ・幅
    h, w = templeteList[0].shape
    
    # テンプレートマッチング（OpenCVで実装）
    #TM_CCOEFF_NORMED
    for i in range(len(templeteList)):
        match_TM_CCOEFF_NORMED = cv2.matchTemplate(trimg, templeteList[i], cv2.TM_CCOEFF_NORMED)
        min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match_TM_CCOEFF_NORMED)
        print('%s :%f' %(weaponNameIndex[i],max_value))
        if(maxTmp < max_value):
            maxTmp = max_value
            indexNumber = i
    
    print('%s :%f' %(weaponNameIndex[indexNumber],maxTmp))

if __name__ == "__main__":
    main()