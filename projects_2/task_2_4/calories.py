# 1. ВВОД ДАННЫХ
proteins = float(input("Введите массу белков (г): "))
fats = float(input("Введите массу жиров (г): "))
carbohydrates = float(input("Введите массу углеводов (г): "))

# 2. РАСЧЕТ КАЛОРИЙНОСТИ
calories = (proteins * 4) + (fats * 9) + (carbohydrates * 4)

# 3. ВЫВОД РЕЗУЛЬТАТА
print(f"Калорийность продукта: {calories:.1f} ккал")