from ImageOperations.ImageDownload import ImageDownload
import cv2
from QT.Qt import QtInterface

def main():

    qt = QtInterface()
    img = ImageDownload(qt)
    current_image = None

    def img_not_none(func):
        def wrapper(*args, **kwargs):
            if current_image is None:
                print("Не удалось загрузить изображение!")
                return None
            else:
                return func(img, *args, **kwargs)
        return wrapper

    def load_image():
        nonlocal current_image
        img.load_image()
        current_image = img.img

    def video():
        nonlocal current_image
        img.video()
        current_image = img.img

    def exit_app():
        cv2.destroyAllWindows()
        qt.app.quit()

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