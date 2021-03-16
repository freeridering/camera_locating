# 基于tensorflow1.9GPU版本的目标识别与定位

环境：python3.5，tensorflow-GPU1.9.0，opencv3.3.1(with contrib)<br>

## 0 相机标定

参考代码：https://blog.csdn.net/qq_32159463 主页下

参考视频：https://www.bilibili.com/video/BV1sK4y1s7Qs?from=search&seid=18016486112252965013

## 1 目标检测

### 1-1 图片采集
建议与识别的图片分辨率一致。

存在问题：
    
    是否需要对从摄像机获取的图片进行去畸变，并剪切边缘。
    
### 1-2 图片标注
参考链接：https://blog.csdn.net/shuiyixin/article/details/82623613
使用工具：LabelImg
### 1-3 模型训练
参考链接：https://github.com/YunYang1994/tensorflow-yolov3

替换其中的VOC文件即可
### 1-4 目标检测
根据1-3中生成的pb模型，检测目标并画框

