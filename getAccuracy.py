#-*- coding:utf-8 -*-
import os
import cv2


def main():
    
    templeteList = []
    weaponNameIndex =[]
    fileNameTmp=""
    weaponNameTmp=""
    maxTmp = 0
    indexNumber=1
    weaponNameTmp=""
    output_path_true = 'D:\separate\ImgTrue2\C'
    output_path_false = 'D:\separate\ImgFalse2\D'
    img_count_true = 0  # 保存した候補画像数
    img_count_false=0
    frame_count = 0  # 読み込んだフレーム画像数
    num_cut=60
    
    for file in os.listdir(r'sozai'):       #銃の子ディレクトリのsozaiの中のデータを取得
        for num in os.path.splitext(file):  
               fileNameTmp += num
               if(num != ".png"):
                    weaponNameTmp+=num
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
        pixelValue1 = trimgUsingGun[21,70]               #銃の真ん中付近の画素値を取得        
        pixelValue2 = trimgUsingGun[23,70]               #銃の真ん中付近の画素値を取得
        if(pixelValue1 < pixelValue2):
            pixelValue = pixelValue2
        else:
            pixelValue = pixelValue1

        trimgUsingGun[trimgUsingGun<(pixelValue-40)]=0  #取得した画素値-20以外を黒
        trimgUsingGun[trimgUsingGun>=(pixelValue+40)]=0 #取得した画素値+20以外を黒
        
        # フレームを表示
        #cv2.imshow("Flame", frame)
        
        #TM_CCOEFF_NORMED
        for i in range(len(templeteList)):
            match_TM_CCOEFF_NORMED = cv2.matchTemplate(trimgUsingGun, templeteList[i], cv2.TM_CCOEFF_NORMED)
            min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match_TM_CCOEFF_NORMED)
            if(maxTmp < max_value):
                maxTmp = max_value
                indexNumber = i
        
        #if(weaponNameIndex[indexNumber] != weaponNameTmp):
        if frame_count % num_cut == 0:
            if(maxTmp > 0.3):
                #print('%s :%f' %(weaponNameIndex[indexNumber],maxTmp))
                img_file_name = output_path_true+str(img_count_true)+weaponNameIndex[indexNumber]+".jpg"
                print(img_file_name)
                cv2.imwrite(img_file_name, frame)
                img_count_true += 1
            else:
                img_file_name = output_path_false+str(img_count_false)+weaponNameIndex[indexNumber]+".jpg"
                cv2.imwrite(img_file_name, frame)
                img_count_false += 1

        frame_count += 1
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