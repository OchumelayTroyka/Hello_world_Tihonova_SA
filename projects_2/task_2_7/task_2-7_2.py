seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for sequence in seq:
    print(f"\nПоследовательность целиком: {sequence}")  # Выводим целиком
    print("Вывод построчно:")
    for letter in sequence:  # Вложенный цикл для символов строки
        print(letter)
    print("---")  # Разделитель между последовательностями

print("Цикл выполнен.")