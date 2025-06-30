import cv2
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel

from src.QT.QtInput import CoordInputDialog, RotationInputDialog


class BaseWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget { font-size: 14px; }
            QPushButton { min-width: 120px; min-height: 30px; }
            QSpinBox { min-width: 100px; font-size: 14px; padding: 5px; }
        """)

class QtInterface:

    def __init__(self):
        self.app = QApplication([])
        self.main_window = BaseWindow()
        self.camera_window = BaseWindow()
        self.operations_window = BaseWindow()
        self.main_layout = None
        self.operations_layout = None
        self.camera_layout = None
        self.setup_windows()

    def setup_windows(self):
        self.main_layout = QVBoxLayout(self.main_window)
        self.operations_layout = QVBoxLayout(self.operations_window)
        self.camera_layout = QVBoxLayout(self.camera_window)
        label = QLabel("(ESC для выхода)")
        self.camera_layout.addWidget(label)

    def show_operations_window(self):
        self.operations_window.show()
        self.main_window.hide()

    def show_main_window(self):
        self.main_window.show()
        self.operations_window.hide()

    @staticmethod
    def add_button(text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    @staticmethod
    def show_file_dialog():
        return QFileDialog.getOpenFileName(
            None, "Выберите изображение", "",
            "Images (*.png *.jpg);;All Files (*)",
            options=QFileDialog.DontUseNativeDialog)

    def show_error(self, message):
        QMessageBox.critical(self.main_window, "Ошибка", message)


    def show_image(self, title, image):
        cv2.imshow(title, image)

    def get_coords(self, title, img_size, mode: str):
        dialog = CoordInputDialog(self.main_window, title, img_size)
        return dialog.get_coordinates(mode)

    def get_rotation_angle(self, img_size):
        dialog = RotationInputDialog(self.main_window, "Поворот", img_size)
        return dialog.get_angle()