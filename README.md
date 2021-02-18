# 最终项目提示

* 提供代码

  * interupt: 

    * 中断: 文件中实现中断函数调用，可直接修改interupt()函数
    * 串口通信: 因为输入被占用，因此无法使用Serial.print，这里给了用LED debug的方法，可以在端口13插入LED灯，即可检测数据传输是否正常

  * hand.py: 手势识别代码

    * 运行方式: 必须安装python -> 打开cmd(输入以下指令)

    ```
    cd 存放hand.py所在文件夹
    pip install opencv-python
    pip install mediapipe
    pip install numpy
    pip install pyserial
    ```

    * 接着输入下述语句即可运行

    ```
    python hand.py
    ```
    
    * 手部关键点如图
    
    ![hand_landmarks](hand_landmarks.png)
    
    * 源代码来自: https://google.github.io/mediapipe/solutions/hands.html

* 要求
* 传感器 - 温度传感器(要求转速与温度成正比)
  * 控制 - 风扇、舵机
  * 中断 - 温控风扇(将马达转速控制写在中断函数中)
  * 串口 - 与python脚本以串口交互(以提供源码)
  * python - 手势识别(能够根据手势改变舵机转向、转速)(手势可自己规定)
