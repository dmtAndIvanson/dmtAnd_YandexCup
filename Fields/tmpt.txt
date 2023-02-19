"""
https://contest.yandex.ru/yacup/contest/42199/problems/A/
решение неверное
"""

def check_input(n, k):
    """Проверяет правильность ввода."""
    if (n**2 / k) < 1:
        return False
    elif (n**2 % k) != 0:
        return False
    elif k == 1:
        return False
    else:
        return True


def create_matrix(size):
    """Создаёт квадратную матрицу."""
    matrix = []
    for i in range(size):
        temp = [0 for x in range(size)]
        matrix.append(temp)
    return matrix


def fill_matrix(matrix, colors, size):
    """Заполняет матрицу цветами."""
    temp = []
    for i in range(int(size**2 / len(colors))):
        temp += colors
    colors = temp

    for i in range(size):
        for j in range(size):
            if i > 0 and colors[-1] == matrix[i-1][j]:
                colors = [colors[-1]] + colors[:-1]       
            matrix[i][j] = colors.pop()
    #else:
    return matrix


def write_answer(lst, file, last):
    """Записывает ответ в файл."""
    line = ""
    for i in lst:
        line += str(i)
        line += ' '

    if last == False:
        file.write(line[:-1] + "\n")
    else:
        file.write(line[:-1])


def main():
    file = open("input.txt", "r")

    size, colors = file.readline().split()
    
    file.close()

    size = int(size)
    colors = int(colors)

    file = open("output.txt", "w")

    if check_input(size, colors) == False:
        file.write("No")
        file.close()
        return

    file.write("Yes\n")

    # Список доступных цветов.
    c_list = [x for x in range(1, colors + 1)]
    
    # Создать матрицу nxn.
    matrix = create_matrix(size)

    # Заполнить матрицу цветами.
    matrix = fill_matrix(matrix, c_list[:], size)
    
    last = False
    for i in range(size):
        if i == size - 1:
            last = True
        write_answer(matrix[i], file, last)

    file.close()


main()
