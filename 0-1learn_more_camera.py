# 打开外部usb摄像头并显示图像

import cv2


capture = cv2.VideoCapture(0)
# 打开自带的摄像头
# 设置分辨率
camera_length = 1280
camera_width = 720
n = 0
if capture.isOpened():
    # 以下两步设置显示屏的宽高，仅显示，没必要用太大地方
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, camera_length)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, camera_width)

    # 持续读取摄像头数据
    while True:
        read_code, frame = capture.read()
        # print(capture.get(3),capture.get(4))
        if not read_code:
            break
        cv2.imshow("screen_title", frame)
        # 输入 q 键，保存当前画面为图片
        if cv2.waitKey(1) == ord('q'):
            # 设置图片分辨率
            n +=1
            frame = cv2.resize(frame, (camera_length, camera_width))
            cv2.imwrite('./image/'+str(n)+'.jpg', frame)

    # 释放资源
    capture.release()
    cv2.destroyWindow("screen_title")
