# 1. ВВОД ПОСЛЕДОВАТЕЛЬНОСТИ
dna_seq = input("Введите последовательность ДНК: ")

# 2. ПРИВЕДЕНИЕ К ВЕРХНЕМУ РЕГИСТРУ
dna_upper = dna_seq.upper()

# 3. ПОДСЧЕТ НУКЛЕОТИДОВ
count_A = dna_upper.count('A')
count_T = dna_upper.count('T')
count_G = dna_upper.count('G')
count_C = dna_upper.count('C')

# 4. ОБЩАЯ ДЛИНА
total_length = len(dna_upper)

# 5. РАСЧЕТ ПРОЦЕНТОВ
percent_A = (count_A / total_length) * 100 if total_length > 0 else 0
percent_T = (count_T / total_length) * 100 if total_length > 0 else 0
percent_G = (count_G / total_length) * 100 if total_length > 0 else 0
percent_C = (count_C / total_length) * 100 if total_length > 0 else 0

# 6. ВЫВОД РЕЗУЛЬТАТОВ
print("\n=== Анализ последовательности ДНК ===\n")
print(f"Введите последовательность ДНК: {dna_seq}")
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
print(f"\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")
print(f"\nОбщая длина: {total_length} нуклеотидов")
print(f"\nПроцентное содержание:")
print(f"A: {percent_A:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"C: {percent_C:.1f}%")