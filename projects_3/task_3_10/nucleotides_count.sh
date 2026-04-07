#!/bin/bash
echo "Файл                    A     T     G     C"
echo "-----------------------------------------------"
for file in fasta_files/*.fasta; do
# Пропускаем пустые файлы
if [ ! -s "$file" ]; then
echo "$(basename "$file")  ПУСТОЙ"
continue
fi
# Объединяем последовательность в одну строку
seq=$(grep -v "^>" "$file" | tr -d '\n')
# Считаем нуклеотиды
a=$(echo "$seq" | grep -o "A" | wc -l)
t=$(echo "$seq" | grep -o "T" | wc -l)
g=$(echo "$seq" | grep -o "G" | wc -l)
c=$(echo "$seq" | grep -o "C" | wc -l)
printf "%-20s %-5s %-5s %-5s %-5s\n" "$(basename "$file")" "$a" "$t" "$g" "$c"
done
