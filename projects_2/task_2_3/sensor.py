# 1. СБОР ДАННЫХ
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

# 2. РАБОТА С ФАЙЛОМ
with open("sensor_log.txt", "w", encoding="utf-8") as log:
    
    # 3. ЗАПИСЬ ДАННЫХ В ФОРМАТЕ ТАБЛИЦЫ
    log.write("ОПЕРАТОР\tЗНАЧЕНИЕ (Па)\n")  # Заголовки таблицы
    log.write(f"{operator_name}\t{pressure_value}\n")

# 4. ПОДТВЕРЖДЕНИЕ
print("Данные успешно сохранены в sensor_log.txt")