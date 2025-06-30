import sys

from ImageOperations.ImageDownload import ImageDownload
from QT.QtMain import QtInterface
from ImageOperations.Functions import *


def main():

    img = ImageDownload(qt)
    current_image = None

    def load_image():
        nonlocal current_image
        img.load_image()
        current_image = img.img

    def video():
        nonlocal current_image
        img.video()
        current_image = img.img

    def show_operations():
        if current_image is None:
            qt.show_error("Сначала загрузите изображение!")
            return
        else:
            while qt.operations_layout.count():
                item = qt.operations_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            btn_crop = qt.add_button("Обрезать", lambda: crop(current_image, qt))
            btn_rotate = qt.add_button("Повернуть", lambda: rotation(current_image, qt))
            btn_rect = qt.add_button("Прямоугольник", lambda: rectangle(current_image, qt))
            btn_red = qt.add_button("Красный канал", lambda: red_channel(current_image, qt))
            btn_green = qt.add_button("Зеленый канал", lambda: green_channel(current_image, qt))
            btn_blue = qt.add_button("Синий канал", lambda: blue_channel(current_image, qt))
            btn_back = qt.add_button("Назад", qt.show_main_window)

            for btn in [btn_crop, btn_rotate, btn_rect, btn_red, btn_green, btn_blue, btn_back]:
                qt.operations_layout.addWidget(btn)

            qt.show_operations_window()

    def exit_app():
        cv2.destroyAllWindows()
        qt.app.quit()

    menu_items = [
        ("Загрузить изображение", load_image),
        ("Сделать снимок с камеры", video),
        ("Операции с изображениями", show_operations),
        ("Выход", exit_app)
    ]

    for text, callback in menu_items:
        qt.main_layout.addWidget(qt.add_button(text, callback))

    qt.show_main_window()


if __name__ == "__main__":
    qt = QtInterface()
    main()
    sys.exit(qt.app.exec_())