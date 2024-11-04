from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6 import uic
from Camera import CameraWidget
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 动态加载 .ui 文件
        uic.loadUi("form.ui", self)  # 直接加载 .ui 文件并设置到当前窗口
        self.camera_widget = CameraWidget()
        self.verticalLayout.addWidget(self.camera_widget)  # 假设你在 .ui 中有一个垂直布局
        self.start.clicked.connect(self.start_camera)
    def start_camera(self):
        camera_index = self.camera_index.value()  # 获取用户选择的摄像头编号

              # 清空 verticalLayout 中的所有控件
        while self.verticalLayout.count() > 0:
            item = self.verticalLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

              # 创建新的 CameraWidget 并添加到布局
        self.camera_widget = CameraWidget(camera_index)
        self.verticalLayout.addWidget(self.camera_widget)  # 添加到布局
        self.camera_widget.timer.start()  # 启动相机

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
