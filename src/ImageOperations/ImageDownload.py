import os
import cv2

class ImageDownload:
    def __init__(self, qt_instance):
        self.qt = qt_instance
        self.img = None
        self.cap = None

    def load_image(self):
        file_path, _ = self.qt.show_file_dialog()
        if file_path:
            self.img = cv2.imread(os.path.normpath(file_path))
            if self.img is not None:
                cv2.imshow("Загруженное изображение", self.img)
            else:
                print("Ошибка загрузки изображения!")

    def video(self):
        if self.cap is not None:
            print("Камера уже запущена!")
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Ошибка: не удалось открыть камеру")
            return

        button = self.qt.add_button("Сделать снимок", lambda: self.save_frame())
        self.qt.camera_layout.addWidget(button)
        self.qt.camera_window.show()

        while True:
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow('Камера (ESC для выхода)', frame)
                key = cv2.waitKey(1)
                if key == 27 or not self.qt.camera_window.isVisible():
                    break
            else:
                print("Ошибка чтения камеры")
                break

        button.deleteLater()
        cv2.destroyWindow('Камера (ESC для выхода)')
        self.cap.release()
        self.cap = None
        self.qt.camera_window.hide()

    def save_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.img = frame.copy()
            cv2.imshow("Сохранённый снимок", self.img)
        else:
            print("Не удалось сделать снимок!")