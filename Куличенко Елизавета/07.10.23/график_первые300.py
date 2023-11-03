import numpy as np  # библиотека расширенной математики
import matplotlib as mp  # библиотека рисования растровых графиков
from matplotlib import pyplot as plt  # создаём короткий псевдоним
X = []  # создаем пустой массив X
Y = []  # создаем пустой массив Y
i = 0  # задаём начальное значение X
data = open('08.csv')  # открываем файл на чтение
while True:  # до тех пор пока файл не закончится
    line = data.readline()  # считываем строку
    if not line:  # если не удалось (закончился файл)
        data.close()  # закрываем файл
        break  # и прерываем цикл чтения
    else:  # если удалось (файл ещё не закончился)
        X.append(i)  # добавляем значение в массив аргументов
        Y.append(float(line))  # добавляем значение в массив значений функции
        i = i + 1  # увеличиваем значение аргумента
# график, размер в десятках процентов экрана
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(X, Y, c='g')  # нарисовать зелёный график значений
ax.grid()  # нарисовать координатную сетку
ax.set_title('График значений')  # подписать заголовок графика
# ограничить отображение по оси X (от; до)
ax.set_xlim(0-int(len(X)*0.05), len(X)*1.05)
# ограничить отображение оси Y (от; до)
ax.set_ylim(0-int(max(Y)*0.05), max(Y)*1.05)
plt.show()  # показать, что получилось
