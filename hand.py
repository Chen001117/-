import cv2
import mediapipe as mp
import serial
import time

serialPort = "COM10"  # 此处输入串口号
baudRate = 9600  # 波特率9600可不变
ser = serial.Serial(serialPort, baudRate, timeout=0.5)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For static images:
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5)

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
while cap.isOpened():
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    # If loading a video, use 'break' instead of 'continue'.
    continue

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
  image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
  image.flags.writeable = False
  results = hands.process(image)

  # Draw the hand annotations on the image.
  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS) # 可以在屏幕上显示侦测到的手部框架
        # 在此处添加识别手势代码
        # hand_landmarks.landmark[i].x 可以得到第i个关键点的x坐标(y,z坐标同理)
    # 通过serial向UNO板发送数据(格式为: b"数字")
    ser.write(b"1")
    print("send ", "1")
  cv2.imshow('MediaPipe Hands', image)
  if cv2.waitKey(5) & 0xFF == 27:
    break
hands.close()
cap.release()
