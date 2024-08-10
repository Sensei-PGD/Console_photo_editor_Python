from PIL import Image  # библиотека изображений
import re              # библиотека регулярных выражений
from filters import Red_Filter, Green_Filter, Blue_Filter, Gray_Filter, Vintage_Filter, Inversion_Filter, Blur_Filter, \
    Brightness_Filter, Turn_90_Filter, Turn_180_Filter, Turn_270_Filter, Mirror_Filter, Detecting_Boundaries_Filter,   \
    Detecting_Boundaries_2_Filter, Detecting_Boundaries_White_Filter, Black_White_Filter  # импорт файла и его фильтров


def main():
    print("Добро пожаловать в консольный фоторедактор.")

    # Запрос пути к изображению
    while True:
        # Запрос пути к изображению
        print("❕ Напоминание: путь к файлу должен примерно выглядеть так: G:/folder/sample.jpeg")
        image_path = input("Введите путь к файлу: ")

        try:
            # Открытие изображения и конвертация в формат RGB
            image = Image.open(image_path).convert("RGB")
            break  # Если файл успешно открыт, выходим из цикла
        except IOError:
            print("\n❌ Ошибка: не удалось открыть файл.")
            print("Попробуйте заново ввести путь к файлу.")

    while True:
        # Вывод меню фильтров
        print("\nМеню фильтров:")
        print("1: Красный фильтр")
        print("2: Зелёный фильтр")
        print("3: Синий фильтр")
        print("4: Серый фильтр")
        print("5: Коричневый фильтр")
        print("6: Инверсия")
        print("7: Фильтр размытия")
        print("8: Фильтр яркости")
        print("9: Фильтр переворота на 90°")
        print("10: Фильтр переворота на 180°")
        print("11: Фильтр переворота на 270°")
        print("12: Зеркальный фильтр")
        print("13: Фильтр обнаружения границ")
        print("14: Фильтр обнаружения границ со сглаживанием")
        print("15: Фильтр обнаружения границ на белом фоне")
        print("16: Чёрно-белый фильтр")
        print("0: Выход")

        # Выбор фильтра
        choice = input("\nВыберите фильтр (или 0 для выхода): ")

        if choice == "0":
            print("\nДо свидания! 👋")
            break

        if choice == "1":
            filter_class = Red_Filter
        elif choice == "2":
            filter_class = Green_Filter
        elif choice == "3":
            filter_class = Blue_Filter
        elif choice == "4":
            filter_class = Gray_Filter
        elif choice == "5":
            filter_class = Vintage_Filter
        elif choice == "6":
            filter_class = Inversion_Filter
        elif choice == "7":
            filter_class = Blur_Filter
        elif choice == "8":
            filter_class = Brightness_Filter
        elif choice == "9":
            filter_class = Turn_90_Filter
        elif choice == "10":
            filter_class = Turn_180_Filter
        elif choice == "11":
            filter_class = Turn_270_Filter
        elif choice == "12":
            filter_class = Mirror_Filter
        elif choice == "13":
            filter_class = Detecting_Boundaries_Filter
        elif choice == "14":
            filter_class = Detecting_Boundaries_2_Filter
        elif choice == "15":
            filter_class = Detecting_Boundaries_White_Filter
        elif choice == "16":
            filter_class = Black_White_Filter
        else:
            print("\n❗ Неверный выбор фильтра! Повторите ещё раз")
            continue

        # Создание экземпляра фильтра
        filter_instance = filter_class()

        # Описание фильтра
        print("\n" + filter_instance.name + ":")
        print(filter_instance.description)

        # Применение фильтра
        while True:
            apply_filter = input("\nПрименить фильтр к картинке? (Да/Нет): ")
            if apply_filter.lower() == "да" or apply_filter.lower() == "нет":
                break
            else:
                print("\n❗ Неверный выбор! Повторите ещё раз.")

        if apply_filter.lower() == "да":
            filtered_image = filter_instance.apply(image)

            # Сохранение обработанного изображения
            print("❕ Напоминание: изображение сохраняется в выбираемую директорию (в файл 📄, primer.*).")
            while True:
                savepath = input("\nКуда сохранить: ")
                if not re.match(r'^[a-zA-Z]', savepath):
                    print("\n❗ Некорректный ввод! Попробуйте снова.")
                    continue
                try:
                    with open(savepath):  # Открываем файл для записи, чтобы проверить его доступность
                        break
                except IOError:
                    print("\n❗ Некорректный ввод! Попробуйте снова.")
                    continue
            try:
                filtered_image.save(savepath)
                print("\n✔ Изображение успешно сохранено.")

            except FileNotFoundError:
                print("\n❌ Ошибка: не удалось сохранить файл.")

        # Обработка другого изображения или завершение работы программы
        while True:
            repeat = input("\n❔ Ещё раз? (Да/Нет): ")
            if repeat.lower() == "да" or repeat.lower() == "нет":
                break
            else:
                print("\n❗ Некорректный ввод! Попробуйте снова.")

        if repeat.lower() == "нет":
            print("\nДо свидания! 👋")
            break


if __name__ == "__main__":
    main()
