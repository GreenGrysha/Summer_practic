from PyQt5.QtWidgets import *


class ImageInputDialog(QDialog):
    """Базовый класс диалоговых окон для работы с изображениями.

    Args:
        parent (QWidget): Родительский виджет.
        title (str): Заголовок окна.
        img_size (tuple): Размер изображения (ширина, высота).
    """

    def __init__(self, parent, title, img_size):
        super().__init__(parent)
        self.title = title
        self.img_size = img_size
        self.setup_ui()
        self.angle_input = None

    def setup_ui(self):
        """Настраивает интерфейс окна."""
        self.setWindowTitle(f"{self.title}(Размер:"
                            f" {self.img_size[0]}x{self.img_size[1]})")
        self.resize(400, 200)


class CoordInputDialog(ImageInputDialog):
    """Диалоговое окно для ввода координат (обрезка/прямоугольник)."""

    def __init__(self, parent, title, img_size):
        super().__init__(parent, title, img_size)

    def get_coordinates(self, mode: str):
        """Возвращает координаты в зависимости от режима (crop/rectangle).

        Args:
            mode (str): Режим работы ('crop' или 'rectangle').

        Returns:
            tuple: Координаты (x1, y1, x2, y2) или None, если отменено.
        """
        layout = QFormLayout(self)
        fields = {}
        if mode == 'crop':
            params = [
                ('left', "Левая граница:", 0, self.img_size[0] - 1),
                ('top', "Верхняя граница:", 0, self.img_size[1] - 1),
                ('right', "Правая граница:", 1, self.img_size[0]),
                ('bottom', "Нижняя граница:", 1, self.img_size[1])
            ]
        else:
            params = [
                ('x1', "X левого верхнего:", 0, self.img_size[0] - 1),
                ('y1', "Y левого верхнего:", 0, self.img_size[1] - 1),
                ('x2', "X правого нижнего:", 1, self.img_size[0]),
                ('y2', "Y правого нижнего:", 1, self.img_size[1])
            ]
        for name, label, min_val, max_val in params:
            spinbox = QSpinBox()
            spinbox.setMinimum(min_val)
            spinbox.setMaximum(max_val)
            fields[name] = spinbox
            layout.addRow(label, spinbox)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok |
                                   QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

        if self.exec_() == QDialog.Accepted:
            return tuple(fields[name].value() for name in fields)
        return None


class RotationInputDialog(ImageInputDialog):
    """Диалоговое окно для ввода угла поворота."""

    def __init__(self, parent, title, img_size):
        super().__init__(parent, title, img_size)
        self.setup_inputs()

    def setup_inputs(self):
        """Настраивает элементы ввода угла поворота."""
        layout = QVBoxLayout(self)
        self.angle_input = QSpinBox()
        self.angle_input.setMinimum(0)
        self.angle_input.setMaximum(360)
        layout.addWidget(QLabel("Угол поворота (0-360°):"))
        layout.addWidget(self.angle_input)
        layout.addSpacing(20)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok |
                                   QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_angle(self):
        """Возвращает выбранный угол поворота."""
        if self.exec_() == QDialog.Accepted:
            return self.angle_input.value()
        return None


class ChannelSelectDialog(ImageInputDialog):
    """Диалоговое окно для выбора цветового канала."""

    def __init__(self, parent, title, img_size):
        super().__init__(parent, title, img_size)
        self.channel_group = None
        self.setup_inputs()

    def setup_inputs(self):
        """Настраивает переключатели каналов."""
        layout = QVBoxLayout(self)
        self.channel_group = QButtonGroup(self)
        rb_red = QRadioButton("Красный канал")
        rb_green = QRadioButton("Зеленый канал")
        rb_blue = QRadioButton("Синий канал")
        self.channel_group.addButton(rb_red, 0)
        self.channel_group.addButton(rb_green, 1)
        self.channel_group.addButton(rb_blue, 2)
        layout.addWidget(rb_red)
        layout.addWidget(rb_green)
        layout.addWidget(rb_blue)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok |
                                   QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_selected_channel(self):
        """Возвращает индекс выбранного канала (0: red, 1: green, 2: blue)."""
        if self.exec_() == QDialog.Accepted:
            return self.channel_group.checkedId()
        return None
