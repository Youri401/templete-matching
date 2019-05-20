#-*- coding:utf-8 -*-
import cv2


def main():
    
    output_path = 'E:\pubgdata\separate\HP\H'
    num_cut =120
    frame_count = 0
    img_count = 0
    restHp = 0
    

    # 動画の読み込み
    cap = cv2.VideoCapture("PUBGPlay.mp4")

    # 動画終了まで繰り返し
    while(cap.isOpened()):

        # フレームを取得
        ret, frame = cap.read()

        if frame_count % num_cut == 0:         
            trimg = frame[684:700,503:778]
            gray = cv2.cvtColor(trimg, cv2.COLOR_BGR2GRAY)
            hpPixelValue = gray[0,0]
            gray[gray<(hpPixelValue-50)]=0
            gray[gray>=(hpPixelValue+50)]=0
            for i in range (100):
                if((gray[0,int(i*2.75)] < (hpPixelValue+50))&(gray[0,int(i*2.75)]>(hpPixelValue-50))):
                    restHp = (i+1)
                    continue
                else: break;
            img_file_name = output_path + str(img_count)+",P"+str(restHp)+".jpg"
            print(img_file_name)
            cv2.imwrite(img_file_name, frame)
            img_count += 1
            
        frame_count += 1
        restHp = 0

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()