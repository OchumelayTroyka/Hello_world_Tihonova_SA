#!/bin/bash
LOG_FILE="report.log"
# Код ошибки для проверки
ERROR_CODE="0"
if [ -e "$LOG_FILE" ]; then
echo "Файл отчёта '$LOG_FILE' существует."
# Дополнительная проверка: не пуст ли файл?
if [ -s "$LOG_FILE" ]; then
echo "Файл не пустой, размер больше 0 байт."
else
echo "Внимание: файл существует, но он пуст."
fi
# Проверка кода ошибки
if [ "$ERROR_CODE" == "0" ]; then
echo "Код ошибки: $ERROR_CODE — выполнение успешно."
elif [ "$ERROR_CODE" -eq "1" ]; then
echo "Код ошибки: $ERROR_CODE — обнаружена ошибка 1."
elif [ "$ERROR_CODE" -eq "2" ]; then
echo "Код ошибки: $ERROR_CODE — обнаружена ошибка 2."
else
echo "Неизвестный код ошибки: $ERROR_CODE."
fi
else
echo "Ошибка: файл отчёта '$LOG_FILE' не найден!"
fi
