#!/bin/bash
echo "Калькулятор ИМТ"
echo ""
read -p "Введите вашу массу(в кг): " weight
read -p "Введите ваш рост (в метрах, например 1.70): " height
if [ -z "$weight" ] || [ -z "$height" ]; then
echo "Ошибка: Масса и рост не могут быть пустыми!"
exit 1
fi
if ! [[ "$weight" =~ ^[0-9]+\.?[0-9]*$ ]] || ! [[ "$height" =~ ^[0-9]+\.?[0-9]*$ ]]; then
echo "Ошибка: Введите корректные числовые значения!"
exit 1
fi
bmi=$(echo "scale=0; $weight / ($height * $height)" | bc)
echo ""
echo "Результат рассчета:"
echo "Масса: $weight кг"
echo "Рост: $height м"
echo "Ваш ИМТ: $bmi"
