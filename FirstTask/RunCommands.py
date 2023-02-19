# Программа запускает другую программу заданное количество раз.
# Автор: Андреев Дмитрий

import os


def main():
    for i in range(1,31):
        # Поменять строку, чтобы запустить другую программу.
        os.system(f"python3 findWay_3.py input{i}.txt outputs3/output{i}.txt")


main()