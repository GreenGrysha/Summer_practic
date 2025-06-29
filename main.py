import cv2
from PyQt5.QtWidgets import QFileDialog, QApplication
import sys

app = QApplication(sys.argv)
file_path, _ = QFileDialog.getOpenFileName(
    None, "Выберите изображение", "",
    "Images (*.png *.jpg);;All Files (*)"
)

def img_current(func):
    def wrapper(file_path, *args, **kwargs):
        if not file_path:
            print("Файл не выбран!")
            return None
        img = cv2.imread(file_path)
        if img is None:
            print("Не удалось загрузить изображение!")
            return None
        return func(img, *args, **kwargs)
    return wrapper

