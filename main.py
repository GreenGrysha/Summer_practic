import cv2
from PyQt5.QtWidgets import QFileDialog, QApplication, QPushButton, QVBoxLayout, QWidget

"""
Пока что переменная 'img' будет реализована через global, в будущих версиях это исправится
"""

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()


img = None

def img_not_none(func):
    def wrapper(*args, **kwargs):
        if img is None:
            print("Не удалось загрузить изображение!")
            return None
        else:
            return func(img, *args, **kwargs)
    return wrapper


def load_img():
    global img
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Выберите изображение", "",
        "Images (*.png *.jpg);;All Files (*)")
    if not file_path:
        print("Файл не выбран!")
        return None
    img = cv2.imread(file_path)
    if img is None:
        print("Не удалось загрузить изображение!")
        return None
    return img

def video():
    global img
    cap = cv2.VideoCapture(0)
    button = QPushButton("Сделать снимок")
    button.clicked.connect(lambda: save_frame(cap))
    layout.addWidget(button)
    window.setLayout(layout)
    window.show()
    while (True):
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            print("Не удалось считать кадр")
    cap.release()
    cv2.destroyAllWindows()
    return img

def save_frame(cap):
    global img
    ret, frame = cap.read()
    if ret:
        current_img = frame.copy()
        cv2.imshow("Сохранённый снимок", current_img)
    else:
        print("Не удалось сделать снимок!")

if __name__ == "__main__":
    choice = int(input())
    if choice == 1:
        video()
    if choice == 2:
        load_img()