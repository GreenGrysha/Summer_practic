import cv2
import numpy as np

def int_check():
    num = input()
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print("Вы ввели не число")
            num = input("Попробуйте снова: ")

def crop(img: np.ndarray, qt):
    img_for_redact = img.copy()
    height, width = img_for_redact.shape[:2]

    coords = qt.get_coords("Обрезка изображения", (width, height), mode='crop')
    if coords is None:
        return

    x1, y1, x2, y2 = coords

    if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
        qt.show_error("Некорректные координаты для обрезки!")
        return

    crop_img = img_for_redact[y1:y2, x1:x2]
    qt.show_image("Результат обрезки", crop_img)

def rotation(img: np.ndarray, qt):
    img_for_redact = img.copy()
    height, width = img_for_redact.shape[:2]

    angle = qt.get_rotation_angle((width, height))
    if angle is None:
        return

    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 0.6)
    rotate_image = cv2.warpAffine(img_for_redact, rotation_matrix, (width, height))
    qt.show_image("Результат поворота", rotate_image)

def rectangle(img: np.ndarray, qt):
    img_for_redact = img.copy()
    height, width = img_for_redact.shape[:2]

    coords = qt.get_coords("Прямоугольник", (width, height),mode='rectangle')
    if coords is None:
        return

    x1, y1, x2, y2 = coords

    if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
        qt.show_error("Некорректные координаты прямоугольника!")
        return

    rectangle_img = cv2.rectangle(img_for_redact, (x1, y1), (x2, y2), (255, 0, 0), 3)
    qt.show_image("Прямоугольник", rectangle_img)


def red_channel(img: np.ndarray, qt):
    b, g, r = cv2.split(img)
    red = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
    qt.show_image("Красный канал", red)


def green_channel(img: np.ndarray, qt):
    b, g, r = cv2.split(img)
    green = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
    qt.show_image("Зеленый канал", green)


def blue_channel(img: np.ndarray, qt):
    b, g, r = cv2.split(img)
    blue = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])
    qt.show_image("Синий канал", blue)