import os

import cv2
from QT.Qt import QtInterface


"""
Пока что переменная 'img' будет реализована через global, в будущих версиях это исправится
"""

qt = QtInterface()
img = None
cap = None

def img_not_none(func):
    def wrapper(*args, **kwargs):
        if img is None:
            print("Не удалось загрузить изображение!")
            return None
        else:
            return func(img, *args, **kwargs)
    return wrapper


def load_image():
    global img
    file_path, _ = qt.show_file_dialog()
    if file_path:
        img = cv2.imread(os.path.normpath(file_path))
        if img is not None:
            cv2.imshow("Загруженное изображение", img)
        else:
            print("Ошибка загрузки изображения!")


def video():
    global cap
    if cap is not None:
        print("Камера уже запущена!")
        return
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Ошибка: не удалось открыть камеру")
        return
    button = qt.add_button("Сделать снимок", lambda: save_frame())
    qt.camera_layout.addWidget(button)
    qt.camera_window.show()

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Камера (ESC для выхода)', frame)
            key = cv2.waitKey(1)
            if key == 27 or not qt.camera_window.isVisible():
                break
        else:
            print("Ошибка чтения камеры")
            break

    button.deleteLater()
    cv2.destroyWindow('Камера (ESC для выхода)')
    cap.release()
    cap = None
    qt.camera_window.hide()

def save_frame():
    global img, cap
    ret, frame = cap.read()
    if ret:
        current_img = frame.copy()
        cv2.imshow("Сохранённый снимок", current_img)
    else:
        print("Не удалось сделать снимок!")

def exit_app():
    cv2.destroyAllWindows()
    qt.app.quit()


def main():
    menu_items = [
        ("Загрузить изображение", load_image),
        ("Сделать снимок с камеры", video),
        ("Выход", exit_app)
    ]

    for text, callback in menu_items:
        qt.main_layout.addWidget(qt.add_button(text, callback))

    qt.show_main_window()


if __name__ == "__main__":
    main()