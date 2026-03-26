# 1. ЗАПРОС ДАННЫХ
volume = float(input("Введите нужный объем физиологического раствора (мл): "))

# 2. РАСЧЕТ КОМПОНЕНТОВ
salt_mass = volume * 0.009  # 0.9% концентрация

# 3. ФОРМИРОВАНИЕ ОТЧЕТА И ЗАПИСЬ В ФАЙЛ
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume:.2f} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {volume:.2f} мл\n")

# 4. ПОДТВЕРЖДЕНИЕ
print("Рецепт успешно сохранен в файл recipe.txt")