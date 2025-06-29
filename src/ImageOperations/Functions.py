import cv2
import numpy


def int_check():
    num = input()
    while True:
        try:
            num = int(num)
            return num
        except ValueError:
            print("Вы ввели не число")
            num = input("Попробуйте снова: ")

def crop(img: numpy.ndarray):
    img_for_redact = img.copy()
    while True:
        height, width = img_for_redact.shape[:2]
        print(f"Размер изображения: ширина={width}, высота={height}")
        print("Введите левый верхний угол: ")
        a1 = int_check()
        print("Введите правый верхний угол: ")
        b1 = int_check()
        print("Введите левый нижний угол: ")
        a2 = int_check()
        print("Введите правый нижний угол: ")
        b2 = int_check()
        if a1 >= 0 and b1 >= 0 and a2 <= width and b2 <= height and a1 < a2 and b1 < b2:
            crop_img = img_for_redact[b1:b2, a1:a2]
            cv2.imshow("Результат", crop_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return
        else:
            print("Ошибка! убедись в правильности введенных границ")

def rotation(img: numpy.ndarray):
    img_for_redact = img.copy()
    height, width = img_for_redact.shape[:2]
    center = (int(width / 2), int(height / 2))
    print("Вращение будем производить относительно центра, по часовой стрелки")
    while True:
        print("Введите угол поворота в градусах: ")
        a = int_check()
        if a > 360:
            print("Вы ввели угол, превышающий 360 градусов, введите угол меньше")
            continue
        else:
            rotation_matrix = cv2.getRotationMatrix2D(center, a, 0.6)
            rotate_image = cv2.warpAffine(img, rotation_matrix, (width, height))
            cv2.imshow("Результат", rotate_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

def rectangle(img: numpy.ndarray):
    img_for_redact = img.copy()
    while True:
        height, width = img_for_redact.shape[:2]
        print(f"Размер изображения: ширина={width}, высота={height}")
        print("Введите координату по высоте для левого верхнего угла: ")
        a1 = int_check()
        print("Введите координату по ширине для левого верхнего угла: ")
        b1 = int_check()
        print("Введите координату по высоте для правого нижнего угла: ")
        a2 = int_check()
        print("Введите координату по ширине для правого нижнего угла: ")
        b2 = int_check()
        if a1 >= 0 and b1 >= 0 and a2 <= height and b2 <= width and a1 < a2 and b1 < b2:
            rectrangle_img =cv2.rectangle(img_for_redact, (a1, b1), (a2, b2), (255, 0, 0), thickness=3)
            cv2.imshow("Результат", rectrangle_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return
        else:
            print("Ошибка! убедись в правильности введенных границ")
