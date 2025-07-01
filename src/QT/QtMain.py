import cv2
from PyQt5.QtWidgets import *

from src.QT.QtInput import CoordInputDialog, RotationInputDialog


class BaseWindow(QWidget):
    """Базовое окно с общими настройками стилей."""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Устанавливает стили для виджетов."""
        self.setStyleSheet("""
            QWidget { font-size: 14px; }
            QPushButton { min-width: 120px; min-height: 30px; }
            QSpinBox { min-width: 100px; font-size: 14px; padding: 5px; }
        """)


class QtInterface:
    """Интерфейс для взаимодействия между Qt и логикой приложения."""

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
        """Инициализирует окна и их макеты."""
        self.main_layout = QVBoxLayout(self.main_window)
        self.main_window.setWindowTitle("Редактор изображений")
        self.operations_layout = QVBoxLayout(self.operations_window)
        self.operations_window.setWindowTitle("Доступные операции")
        self.camera_layout = QVBoxLayout(self.camera_window)
        self.camera_window.setWindowTitle("Фото")
        label = QLabel("(ESC для выхода)")
        self.camera_layout.addWidget(label)

    def show_operations_window(self):
        """Показывает окно операций с изображениями."""
        self.operations_window.show()
        self.main_window.hide()

    def show_main_window(self):
        """Показывает главное окно."""
        self.main_window.show()
        self.operations_window.hide()

    @staticmethod
    def add_button(text, callback):
        """Создаёт кнопку с заданным текстом и обработчиком.

        Args:
            text (str): Текст кнопки.
            callback (function): Функция-обработчик.

        Returns:
            QPushButton: Созданная кнопка.
        """
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    @staticmethod
    def show_file_dialog():
        """Открывает диалог выбора файла.

        Returns:
            tuple: (Путь к файлу, выбранный фильтр).
        """
        return QFileDialog.getOpenFileName(
            None, "Выберите изображение", "",
            "Images (*.png *.jpg);;All Files (*)",
            options=QFileDialog.DontUseNativeDialog)

    def show_error(self, message):
        """Показывает сообщение об ошибке.

        Args:
            message (str): Текст ошибки.
        """
        QMessageBox.critical(self.main_window, "Ошибка", message)

    def show_image(self, title, image):
        """Отображает изображение в отдельном окне.

        Args:
            title (str): Заголовок окна.
            image (np.ndarray): Изображение в формате OpenCV.
        """
        cv2.imshow(title, image)

    def get_coords(self, title, img_size, mode: str):
        """Возвращает координаты через диалоговое окно.

        Args:
            title (str): Заголовок окна.
            img_size (tuple): Размер изображения.
            mode (str): Режим ('crop' или 'rectangle').

        Returns:
            tuple: Координаты или None.
        """
        dialog = CoordInputDialog(self.main_window, title, img_size)
        return dialog.get_coordinates(mode)

    def get_rotation_angle(self, img_size):
        """Возвращает угол поворота через диалоговое окно.

        Args:
            img_size (tuple): Размер изображения.

        Returns:
            int: Угол поворота или None.
        """
        dialog = RotationInputDialog(self.main_window, "Поворот", img_size)
        return dialog.get_angle()
