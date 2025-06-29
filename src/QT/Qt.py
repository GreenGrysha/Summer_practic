from PyQt5.QtWidgets import QFileDialog, QPushButton, QVBoxLayout, QWidget, QApplication

class QtInterface:
    def __init__(self):
        self.app = QApplication([])
        self.main_window = QWidget()
        self.camera_window = QWidget()
        self.main_layout = QVBoxLayout()
        self.camera_layout = QVBoxLayout()
        self.main_window.setLayout(self.main_layout)
        self.camera_window.setLayout(self.camera_layout)

    def add_button(self, text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    @staticmethod
    def show_file_dialog():
        return QFileDialog.getOpenFileName(
            None, "Выберите изображение", "",
            "Images (*.png *.jpg);;All Files (*)",options=QFileDialog.DontUseNativeDialog)

    def show_main_window(self):
        self.main_window.show()
        return self.app.exec_()

    def show_camera_window(self):
        self.camera_window.show()
        return self.app.exec_()