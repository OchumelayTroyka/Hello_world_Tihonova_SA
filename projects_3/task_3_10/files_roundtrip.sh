#!/bin/bash
# Скрипт files_roundtrip.sh
# Создает 10 файлов test1.txt ... test10.txt, затем удаляет их в обратном порядке
echo "=== Файловый круговорот ==="
echo ""
work_dir="test_files"
mkdir -p "$work_dir"
cd "$work_dir"
echo "1. СОЗДАНИЕ ФАЙЛОВ "
echo "-------------------------------"
# Цикл for для создания файлов
for i in {1..10}; do
filename="test$i.txt"
echo "Содержимое файла test$i.txt" > "$filename"
echo "  Создан файл: $filename"
done
echo ""
echo "Все созданные файлы:"
ls -la
echo ""
echo "2. УДАЛЕНИЕ ФАЙЛОВ (цикл while в обратном порядке)"
echo "-------------------------------"
# Счетчик для обратного порядка
counter=10
# Цикл while для удаления в обратном порядке
while [ $counter -ge 1 ]; do
filename="test$counter.txt"
if [ -f "$filename" ]; then
echo "  Удаляю файл: $filename"
rm "$filename"
else
echo "  Файл $filename не найден"
fi
# Уменьшаем счетчик
((counter--))
done
echo ""
echo "Оставшиеся файлы:"
ls -la 2>/dev/null || echo "  (директория пуста)"
echo ""
echo "Очистка рабочей директории..."
cd ..
rmdir "$work_dir" 2>/dev/null || echo "Директория не пуста или удалена ранее"
echo ""
echo "=== Работа скрипта завершена ==="
