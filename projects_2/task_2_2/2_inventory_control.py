# Программа учета реактивов
# Запрос данных у пользователя
reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество (шт.): "))

# Формирование отчета
report = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."

# Вывод в консоль
print(report)

# Запись в файл
with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("Данные сохранены в файл inventory.txt")