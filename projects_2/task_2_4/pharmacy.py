# 1. ВВОД ДАННЫХ
total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_size = int(input("Введите количество капсул в одной упаковке: "))

# 2. РАСЧЕТ УПАКОВОК И ОСТАТКА
full_packs = total_capsules // pack_size
remaining_capsules = total_capsules % pack_size

# 3. ВЫВОД ОТЧЕТА
print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packs}")
print(f"Остаток капсул:\t\t{remaining_capsules}")