from PIL import Image, ImageFilter

message = "\n----- Выведен предварительный просмотр фотографии -----"


class Filter:
    name = ""
    description = ""

    def apply(self, image):
        pass


class Red_Filter(Filter):
    name = "Красный фильтр"
    description = "Плавно усиливает красный оттенок на изображении."

    def apply(self, image):
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                r = min(255, r + 30)  # увеличиваем красный канал
                pixels[i, j] = (r, g, b)
        print(message)
        image.show()
        return image


class Green_Filter(Filter):
    name = "Зелёный фильтр"
    description = "Плавно усиливает зелёный оттенок на изображении."

    def apply(self, image):
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                g = min(255, g + 30)  # увеличиваем зелёный канал
                pixels[i, j] = (r, g, b)
        print(message)
        image.show()
        return image


class Blue_Filter(Filter):
    name = "Синий фильтр"
    description = "Плавно усиливает синий оттенок на изображении."

    def apply(self, image):
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                b = min(255, b + 30)  # увеличиваем синий канал
                pixels[i, j] = (r, g, b)
        print(message)
        image.show()
        return image


class Gray_Filter(Filter):
    name = "Серый фильтр"
    description = "Преобразует изображение в оттенки серого."

    def apply(self, gray_image):
        image = gray_image.convert("L")
        print(message)
        image.show()
        return image


class Vintage_Filter(Filter):
    name = "Фильтр пленки коричневого цвета"
    description = "Применяет эффект пленки коричневого цвета к изображению."

    def apply(self, image):
        width, height = image.size
        pixels = image.load()

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # Применяем формулу сепии для каждого пикселя
                sepia_r = min(255, int(0.393 * r + 0.769 * g + 0.189 * b))
                sepia_g = min(255, int(0.349 * r + 0.686 * g + 0.168 * b))
                sepia_b = min(255, int(0.272 * r + 0.534 * g + 0.131 * b))

                pixels[i, j] = (sepia_r, sepia_g, sepia_b)
        print(message)
        image.show()
        return image


class Inversion_Filter:
    name = "Инверсия"
    description = "Инвертирует цвета на изображении."

    def apply(self, image):
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                pixels[i, j] = (255 - r, 255 - g, 255 - b)
        print(message)
        image.show()
        return image


class Blur_Filter(Filter):
    name = "Фильтр Размытия"
    description = "Применяет размытие к изображению."

    def apply(self, blurred_image):
        image = blurred_image.filter(ImageFilter.GaussianBlur(20))
        print(message)
        image.show()
        return image


class Brightness_Filter:
    name = "Фильтр с увеличенной яркостью"
    description = "Плавно усиливает яркость изображения."

    def apply(self, image):
        width, height = image.size
        pixels = image.load()

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # Увеличиваем значение каждого цветового канала на заданный коэффициент яркости
                r = min(255, int(r * 1.5))
                g = min(255, int(g * 1.5))
                b = min(255, int(b * 1.5))

                pixels[i, j] = (r, g, b)
        print(message)
        image.show()
        return image


class Turn_90_Filter:
    name = "Фильтр поворота на 90°"
    description = "Переворачивает изображение на 90°."

    def apply(self, converted_img):
        image = converted_img.transpose(Image.ROTATE_270)
        print(message)
        image.show()
        return image


class Turn_180_Filter:
    name = "Фильтр поворота на 180°"
    description = "Переворачивает изображение на 180°."

    def apply(self, converted_img):
        image = converted_img.transpose(Image.ROTATE_180)
        print(message)
        image.show()
        return image


class Turn_270_Filter:
    name = "Фильтр поворота на 270°"
    description = "Переворачивает изображение на 270°."

    def apply(self, converted_img):
        image = converted_img.transpose(Image.ROTATE_90)
        print(message)
        image.show()
        return image


class Mirror_Filter:
    name = "Зеркальный фильтр"
    description = "Переворачивает изображение слева направо, в результате чего получается зеркальное отображение."

    def apply(self, converted_img):
        image = converted_img.transpose(Image.FLIP_LEFT_RIGHT)
        print(message)
        image.show()
        return image


class Detecting_Boundaries_Filter:
    name = "Фильтр обнаружения границ"
    description = "Фильтр обнаружения границ у изображения на чёрном фоне."

    def apply(self, converted_img):
        image = converted_img.filter(ImageFilter.FIND_EDGES)
        print(message)
        image.show()
        return image


class Detecting_Boundaries_2_Filter:
    name = "Фильтр обнаружения границ со сглаживанием"
    description = "Фильтр обнаружения границ у изображения и с добавлением эффекта сглаживания краёв на чёрном фоне."

    def apply(self, converted_img):
        img_gray_smooth = converted_img.filter(ImageFilter.SMOOTH)
        image = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
        print(message)
        image.show()
        return image


class Detecting_Boundaries_White_Filter:
    name = "Фильтр обнаружения границ на белом фоне"
    description = "Фильтр обнаружения границ у изображения на белом фоне."

    def apply(self, converted_img):
        image = converted_img.filter(ImageFilter.EMBOSS)
        print(message)
        image.show()
        return image


class Black_White_Filter:
    name = "Чёрно-белый фильтр"
    description = "Фильтр преобразования изображения в чёрно-белые оттенки."

    def apply(self, gray_image):
        converted_img = gray_image.convert("L")
        image = converted_img.point(lambda x: 255 if x > 90 else 0)
        print(message)
        image.show()
        return image
