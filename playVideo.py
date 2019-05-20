#-*- coding:utf-8 -*-
import os
import cv2


def main():
    
    templeteList = []
    weaponNameIndex =[]
    fileNameTmp=""
    weaponNameTmp=""
    maxTmp = 0;
    indexNumber=1;
    weaponNameTmp=""
    
    for file in os.listdir(r'sozai'):       #銃の子ディレクトリのsozaiの中のデータを取得
        for num in os.path.splitext(file):  
               fileNameTmp += num
               if(num != ".png"):
                    weaponNameTmp+=num;
        weaponNameIndex.append(weaponNameTmp)
        imgTmp=cv2.cvtColor(cv2.imread('sozai\\'+fileNameTmp),cv2.COLOR_RGB2GRAY)
        imgTmp[imgTmp<1]=0
        imgTmp[imgTmp>=1]=255
        templeteList.append(imgTmp)
        fileNameTmp=""
        weaponNameTmp=""
    
        # テンプレート画像の高さ・幅
    h, w = templeteList[0].shape

    # 動画の読み込み
    cap = cv2.VideoCapture("PUBGPlay.mp4")

    # 動画終了まで繰り返し
    while(cap.isOpened()):

        # フレームを取得
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #フレームをグレースケールで取得
        trimgUsingGun = gray[600:650,580:700]           #銃のUIの箇所をトリミング        
        pixelValue = trimgUsingGun[25,70]               #銃の真ん中付近の画素値を取得
        trimgUsingGun[trimgUsingGun<(pixelValue-20)]=0  #取得した画素値-20以外を黒
        trimgUsingGun[trimgUsingGun>=(pixelValue+20)]=0 #取得した画素値+20以外を黒
        
        # フレームを表示
        cv2.imshow("Flame", frame)
        
        #TM_CCOEFF_NORMED
        for i in range(len(templeteList)):
            match_TM_CCOEFF_NORMED = cv2.matchTemplate(trimgUsingGun, templeteList[i], cv2.TM_CCOEFF_NORMED)
            min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match_TM_CCOEFF_NORMED)
            if(maxTmp < max_value):
                maxTmp = max_value
                indexNumber = i
        
        #if(weaponNameIndex[indexNumber] != weaponNameTmp):
        if(maxTmp > 0.3):
            print('%s :%f' %(weaponNameIndex[indexNumber],maxTmp))
        #weaponNameTmp = weaponNameIndex[indexNumber]
        maxTmp = 0
        indexNumber=1

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()