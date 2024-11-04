import sys
import cv2
from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class CameraWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.capture = cv2.VideoCapture(0)  # 使用默认摄像头
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.image = QImage()  # 初始化图像

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.flip(frame, 1)
            # 将图像从 BGR 转换为 RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = channel * width
            self.image = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            self.update()  # 请求重绘

    def paintEvent(self, event):
        if not self.image.isNull():
            painter = QPainter(self)
            painter.drawImage(0, 0, self.image)  # 绘制图像

    def closeEvent(self, event):
        self.capture.release()  # 释放相机资源
        super().closeEvent(event)


    def setCamera(self , index):
        self.capture = cv2.VideoCapture(index)
