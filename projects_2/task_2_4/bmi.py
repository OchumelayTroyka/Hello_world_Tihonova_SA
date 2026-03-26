# 1. ВВОД ДАННЫХ
weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))

# 2. РАСЧЕТ ИМТ (рост в метрах)
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

# 3. ВЫВОД ОТЧЕТА
print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t\t{height_cm:.1f} см")
print(f"Вес:\t\t{weight:.1f} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")