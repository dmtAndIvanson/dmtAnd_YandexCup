# Программа находит сколько самокатов можне развести по местам города.

# Создать класс автомобиля с атрибутами: имя, текущее положение, наибольшая длина маршрута, посещённые точки, количество самокатов (<= 25).
# Методами: изменить координату автомобиля (также добавляет координату в посещённые точки; также указывает доступность), считает длину точек, убирает самокат, добавляет самокат.

# Создать список доступных самокатов и доступных парковочных мест.

# Создать матрицу (список списков) с расстояниями от точки A до точки B.

# Инициализировать список с автомобилями.

# Перебрать каждый автомобиль.
    # Пока длина маршрута больше нуля.
        # Пока меньше 25 самокатов или длина маршрута <= 1/2 исходной длины маршрута.
            # Найти ближайшую точку с самокатами. приехать туда, взять самокат.
        # Пока самокатов больше 0 и длина больше 0.
            # Найти ближайшую парковку. Оставить там самокат.
            # Если нашлось 0 возможных варианто. Значит топливо закончилось. Длина мрашрута = 0.

