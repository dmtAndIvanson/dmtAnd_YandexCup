# Программа-решение задачи 1 YandexCup.
# Версия 3.0 
# + Добавить функцию, которая находит маршрут для машины. Маршрут должен брать максимальное количество самокатов и развозить их все.
# + Обновить функции catch_scooter() и settle_scooter()
# + Убрать свойство half_length
# Автор: Андреев Дмитрий

import sys

class Car():
    def __init__(self, id, cur_place=0, scooter=0, vis_place=[], max_root=0):
        self.id = id
        self.cur_place = cur_place # Изначальное положение самоката.
        self.scooter = scooter # Количество самокатов.
        self.vis_place = vis_place # Посещённые места.
        self.root_length = max_root # Длина маршрута. Вычитать длину пути при передвижении. Обновить при возвращении в начальную точку.

    def change_place(self, new_place, distance):
        """
        Обновляет координату машины.
        Обновляет список посещённых мест.
        Уменьшает оставшуюся длину пути.
        """
        self.cur_place = new_place
        self.vis_place.append(new_place)
        self.root_length -= distance # Длина пути до точки.

    def add_scooter(self):
        """Добавляет самокат."""
        self.scooter += 1

    def rem_scooter(self):
        """Удаляет самокат."""
        self.scooter -= 1

    def count_places(self):
        """Считает сколько точек посетил автомобиль."""
        return len(self.vis_place)


def create_scooter_list(scooters):
    """Создать список мест с самокатами."""
    return [x for x in range(1, scooters + 1)]


def create_parking_list(scooters, parking_places):
    """Создать список доступных парковочных мест."""
    return [x for x in range(scooters + 1, scooters + parking_places + 1)]


def create_matrix(file, size):
    """Создать матрицу (список списков) с расстояниями от точки A до точки B."""
    matrix = []

    for i in range(0, size + 1):
        temp = file.readline() # Прочитать строку.
        temp = temp.split() # Преобразовать в список.
        temp = [int(x) for x in temp]
        # for j in range(0, size): # Преобразовать значения к числовому виду.
        #    temp[j] = int(temp[j])

        matrix.append(temp) # Добавить i-ую строку к матрице.

    return matrix


def find_new_place(cur_place, root_length, places, roots):
    """
    Возвращает координату ближайшего места.
    Если такой координаты нет, или если бензин кончился возвращает -1.
    """

    length = float("inf") # Сколько надо ехать до точки.
    new_place = -1
    # Найти ближайшее место, которое подходит по условиям.
    for place in places:
        temp_length = roots[cur_place][place]
        if  temp_length < length and temp_length <= root_length and temp_length != 0:
            length = temp_length
            new_place = place
    
    return new_place


def catch_scooter(car, scooters, roots, times):
    """Взять самокат в машину."""
    for i in range(times):
        new_place = find_new_place(car.cur_place, car.root_length, scooters, roots)
        distance = roots[car.cur_place][new_place] # Найти длину этого маршрута.
        roots[car.cur_place][new_place] = 0 # 0 значит, что в этом месте мы уже были.
        roots[new_place][car.cur_place] = 0 # 0 значит, что в этом месте мы уже были.
        scooters.remove(new_place) # Убрать найденное место из доступных мест.
        car.change_place(new_place, distance)
        car.add_scooter()


def settle_scooter(car, parkings, roots):
    """Оставить самокат на парковке."""
    while car.scooter > 0: # > 0 - Если менять функцию, надо учесть это условие.
        # Найти ближайшую парковку.
        new_place = find_new_place(car.cur_place, car.root_length, parkings, roots)
        distance = roots[car.cur_place][new_place] # Найти длину этого маршрута.
        roots[car.cur_place][new_place] = 0 # 0 значит, что в этом месте мы уже были.
        roots[new_place][car.cur_place] = 0 # 0 значит, что в этом месте мы уже были.
        parkings.remove(new_place) # Убрать найденное место из доступных мест.
        car.change_place(new_place, distance)
        car.rem_scooter()

def find_scooters_amount(car, scooters, parkings, roots):
    """Найти, сколько самокатов можно взять и отвезти по местам."""
    length = car.root_length
    place = car.cur_place
    ctr = 0

    for i in range(1,26):
        # Сначала забрать самокат.
        new_place = find_new_place(place, length, scooters, roots)
        if new_place == -1:
            return ctr
        # Обновить переменные.
        distance = roots[place][new_place] # Найти длину этого маршрута.
        length -= distance
        roots[place][new_place] = 0 # 0 значит, что в этом месте мы уже были.
        roots[new_place][place] = 0 # 0 значит, что в этом месте мы уже были.
        scooters.remove(new_place) # Убрать найденное место из доступных мест.
        place = new_place

        # Создать временные переменные для развоза самокатов.
        t_place = place
        t_length = length
        t_parkings = parkings[:]
        t_roots = []
        for row in roots:
            t_roots.append(row[:])

        # Развезти самокаты.
        for j in range(i):
            new_place = find_new_place(t_place, t_length, t_parkings, t_roots)
            if new_place == -1:
                return ctr
            
            # Обновить переменные.
            distance = t_roots[t_place][new_place] # Найти длину этого маршрута.
            t_length -= distance
            t_roots[t_place][new_place] = 0 # 0 значит, что в этом месте мы уже были.
            t_roots[new_place][t_place] = 0 # 0 значит, что в этом месте мы уже были.
            t_parkings.remove(new_place) # Убрать найденное место из доступных мест.
            t_place = new_place

            # Проверить, что ещё есть топливо.
            if t_length < 0:
                return ctr

        # Увеличить ctr, если прошлись через сбор и развоз самокатов.
        ctr += 1

    return ctr


def write_data(file, car):
    """Записать значения автомобиля в файл."""
    line = ""
    line += f"{car.count_places()} "
    for place in car.vis_place:
        line += f"{place} "
    file.write(line[:-1])


def main():
    # Открыть файл с данными.
    file = open(sys.argv[1], "r")

    # Прочитать первую строку вида: <scooters> <parking_places> <cars>
    line = file.readline()
    scooters, parking_places, cars = line.split()
    # Преобразовать к числовому виду.
    scooters = int(scooters) # Количество самокатов.
    parking_places = int(parking_places) # Количество парковочных мест.
    cars = int(cars) # Количество машин.
    size = scooters + parking_places 

    # Создать списки с данными.
    scooter_list = create_scooter_list(scooters) # Это места с самокатами.
    pp_list = create_parking_list(scooters, parking_places) # pp for parking place. Это места парковок.
    roots = create_matrix(file, size) # Маршруты.
    
    # Прочитать последнюю строку с длиной маршрута для каждой машины.
    root_length = file.readline()
    root_length = root_length.split()
    for i in range(0, cars):
        root_length[i] = int(root_length[i])

    # Закрыть файл с данными.
    file.close()

    # Инициализировать список автомобилей.
    cars_list = []
    for i in range(0, cars):
        temp = Car(id=(i + 1), cur_place=0, vis_place=[], max_root=root_length[i]) # Если явно не инициализировать vis_place=[], при обновлении vis_place, обновятся cis_place всех машин.
        cars_list.append(temp)
    # Надо отсортировать список автомобилей по их длинам.
    cars_list_1 = cars_list[:] # Запомнить исходную расстановку.
    cars_list.sort(key=lambda x: x.root_length)

    # Для каждого автомобиля найти маршрут.
    for car in cars_list:
        # Сделать временную матрицу.
        t_roots = []
        for row in roots:
            t_roots.append(row[:])

        # Найти сколько самокатов можно развести.
        amount = find_scooters_amount(car, scooter_list[:], pp_list[:], t_roots)

        # Развозить самокаты, пока можно.
        while amount > 0:
            catch_scooter(car, scooter_list, roots, amount)
            settle_scooter(car, pp_list, roots)
            # Сделать временную матрицу.
            t_roots = []
            for row in roots:
                t_roots.append(row[:])
            amount = find_scooters_amount(car, scooter_list[:], pp_list[:], t_roots)
                

    file = open(sys.argv[2], "w")

    ctr = cars
    for car in cars_list_1:
        write_data(file, car)
        ctr -= 1
        if ctr != 0:
            file.write("\n")
    file.close()
    

main()