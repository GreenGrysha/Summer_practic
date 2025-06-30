import cv2


class ImageDownload:
    """Класс для загрузки изображений из файла или с камеры устройства.

    Args:
        qt_instance (QtInterface):
         Экземпляр QtInterface для взаимодействия с GUI.
    """

    def __init__(self, qt_instance):
        self.qt = qt_instance
        self.img = None
        self.cap = None

    def load_image(self):
        """Загружает изображение из файла через диалоговое окно."""
        file_path, _ = self.qt.show_file_dialog()
        if file_path:
            try:
                self.img = cv2.imread(file_path)
                if self.img is not None:
                    self.qt.show_image("Загруженное изображение", self.img)
                else:
                    self.qt.show_error("Не удалось загрузить изображение!")
            except Exception as e:
                self.qt.show_error(f"Ошибка загрузки: {str(e)}")
                self.img = None

    def video(self):
        """Запускает видеозахват с камеры и позволяет сделать снимок."""
        if self.cap is not None:
            print("Камера уже запущена!")
            return

        self.cap = cv2.VideoCapture(0)
        try:
            if not self.cap.isOpened():
                print("Ошибка: не удалось открыть камеру")
                return
            button = self.qt.add_button("Сделать снимок",
                                        lambda: self.save_frame())
            self.qt.camera_layout.addWidget(button)
            self.qt.camera_window.show()
            while True:
                ret, frame = self.cap.read()
                if ret:
                    cv2.imshow('', frame)
                    key = cv2.waitKey(1)
                    if key == 27 or not self.qt.camera_window.isVisible():
                        break
                else:
                    print("Ошибка чтения камеры")
                    break
        finally:
            button.deleteLater()
            cv2.destroyWindow('')
            if self.cap is not None:
                self.cap.release()
            self.cap = None
            self.qt.camera_window.hide()

    def save_frame(self):
        """Сохраняет текущий кадр с камеры как изображение."""
        if self.cap is None:
            return None
        ret, frame = self.cap.read()
        if ret:
            try:
                self.img = frame.copy()
                self.qt.show_image("Снимок с камеры", self.img)
            except Exception as e:
                self.qt.show_error(f"Ошибка сохранения: {str(e)}")
        return None
