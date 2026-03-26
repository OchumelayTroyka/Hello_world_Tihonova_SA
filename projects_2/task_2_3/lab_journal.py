# 1. СБОР ДАННЫХ
researcher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
experiment_conclusion = input("Введите вывод: ")

# 2. РАБОТА С ФАЙЛОМ
with open("journal.txt", "w", encoding="utf-8") as journal:
    
    # 3. ФОРМИРОВАНИЕ РАМКИ И ЗАПИСЬ ДАННЫХ
    journal.write("+" + "-" * 50 + "+\n")
    journal.write(f"|{'Электронный лабораторный журнал':^50}|\n")
    journal.write("+" + "-" * 50 + "+\n")
    journal.write(f"| {'ФИО исследователя':<20}: {researcher_name:<27} |\n")
    journal.write(f"| {'Дата':<20}: {experiment_date:<27} |\n")
    journal.write(f"| {'Эксперимент':<20}: {experiment_name:<27} |\n")
    journal.write("+" + "-" * 50 + "+\n")
    journal.write(f"| {'Вывод:':<50} |\n")
    
    # Разбиваем длинный вывод на строки по 47 символов (с учетом отступов)
    words = experiment_conclusion.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= 47:
            if line:
                line += " " + word
            else:
                line = word
        else:
            journal.write(f"| {line:<47} |\n")
            line = word
    if line:
        journal.write(f"| {line:<47} |\n")
    
    journal.write("+" + "-" * 50 + "+\n")

# 4. ПОДТВЕРЖДЕНИЕ
print("Файл 'journal.txt' успешно сформирован!")