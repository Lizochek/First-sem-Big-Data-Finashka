# Задание:
# Распознавание двухзначного числа

#!pip install num2words
from num2words import num2words

цифра = [0] * 3 * 5  # заполненная нулями матрица 3х5
цифры = цифра * 10  # резервируем память под маски 10-ти цифр
название = [""] * 10  # резервируем память под идентификаторы 10-ти цифр

числа = {
    "ноль": 0,
    "единица": 1,
    "двойка": 2,
    "тройка": 3,
    "четвёрка": 4,
    "пятёрка": 5,
    "шестёрка": 6,
    "семёрка": 7,
    "восьмёрка": 8,
    "девятка": 9
}

название[0] = "ноль"  # задаём перцептрону начальное знание трёх шаблонов цифр
цифра[0] = \
    [0, 1, 0,
     1, 0, 1,
     1, 0, 1,
     1, 0, 1,
     0, 1, 0]
название[1] = "единица"
цифра[1] = \
    [0, 1, 0,
     1, 1, 0,
     0, 1, 0,
     0, 1, 0,
     1, 1, 1]
название[2] = "двойка"
цифра[2] = \
    [1, 1, 1,
     1, 0, 1,
     0, 0, 1,
     0, 1, 0,
     1, 1, 1]

знает = 3  # сколько цифр теперь знает перцептрон
state = {

}


def read_digit():
    # резервируем память под переменную (список из 0 элементов заполненный нулями)
    искомое = [0] * 0
    for i in range(0, 5):  # повторяем 5 раз
        # формируем приглашение для ввода каждой строки
        приглашение = "Введите " + str(i + 1) + "-ую строку образа: "
        # пользователь вводит данные в переменную СТРОКА
        строка = list(map(int, input(приглашение).split()))
        if строка[0] == 5:
            exit()
        искомое = искомое + строка  # добавляем строку к переменной ИСКОМОЕ
    return искомое


def recognition_digit(искомое: list, iter: int, известна: int = 0) -> None:
    '''
    Функция для распознавания цифры
    известна =0
    картинка нам неизвестна (пока не искали)
    '''
    global знает
    global числа
    for i in range(0, знает):  # перебираем все цифры, которые ЗНАЕТ программа
        несовпадение = 0  # предполагаем что ИСКОМОЕ совпадает с проверяемой ЦИФРОЙ
        k = 0  # счётчик несовпадений
        for j in range(0, 14):  # для всех 15-ти элементов ЦИФРЫ
            if искомое[j] != цифра[i][j]:  # если найдены неравные элементы
                несовпадение = 1  # отмечаем НЕСОВПАДЕНИЕ
                k += 1
        степень_уверенности = ((15 - k) / 15)
        # если все 15 элементов ЦИФРЫ совпали с ИСКОМЫМ
        if (несовпадение == 0) or (несовпадение == 1 and k <= 2):
            известна = 1  # отмечаем, что цифра нам известна и обучение не нужно
            state[iter] = {'название': числа[название[i]],
                           'степень_уверенности': степень_уверенности}
            break
    if известна == 0:  # если цифра неизвестна
        print("Эта цифра мне неизвестна.")  # печатаем сообщение
        # сохраняем, полученное от пользователя НАЗВАНИЕ
        название[знает] = input("Введите её название: ")
        # копируем содержимое введённого пользователем образа в пустое место списка ЦИФРЫ
        цифра[знает] = искомое
        знает = знает + 1  # увеличиваем счётчик известных цифр на 1
        print("Спасибо, теперь я её знаю.\n")  # выводим сообщение


бесконечно = 0
while бесконечно == 0:  # бесконечный повтор программы

    # пользователь вводит образ для распознования
    print(""" 
\nВведите построчно визуальный образ цифры по три элемента в строке.
Чёрные точки обозначайте единицами, белые точки нулями.
Цифры разделяйте пробелом.
Для выхода из программы введите 5\n
    """)
    for i in range(2):
        искомое = read_digit()
        # теперь проводим поиск ИСКОМОГО среди известных программе образов
        # известна = 0

        recognition_digit(искомое, i)

        print()
        dvoich_number = str()
        new_stepin = float(1)
    for k, v in state.items():
        dvoich_number += str(v['название'])
        new_stepin *= v['степень_уверенности']

    print("Степень уверенности для двухначного числа:",
          round((new_stepin*100), 2))
    print("Число:", num2words(dvoich_number, lang='ru'))
# возвращаемся к выполнению бесконечного цикла

# Задание:
# 1. Измените программу так, чтобы она распознавала цифры, если при вводе образа допущено не более двух ошибок.
# 2. Измените программу так, чтобы она выводила степень уверенности в распознавании введённой цифры.
# 3. Измените программу так, чтобы она распознавала полутоновые образы цифр с градациями тона от 0 до 255
#
