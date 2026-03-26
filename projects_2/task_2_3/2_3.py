# 1. СБОР ДАННЫХ
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

# 2. РАБОТА С ФАЙЛОМ
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    
    # 3. ЗАПИСЬ ДАННЫХ
    recipe.write(f"{medium_name}\n")           # Название среды — заголовок
    recipe.write(f"Параметры:\n")              # Заголовок списка параметров
    recipe.write(f"  - Концентрация агара: {agar_concentration} %\n")
    recipe.write(f"  - Температура стерилизации: {sterilization_temp} °C\n")

# 4. ПОДТВЕРЖДЕНИЕ
print("Файл 'recipe.txt' успешно сформирован!")