# 2. Посчитать четные и нечетные цифры введенного натурального числа

a = input("Введите число: ")
a = int(a)

even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print(f"Четных чисел {even}. Нечетных чисел {odd}")


#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран
n1 = int(input("Введите число: "))
n2 = 0

while n1 > 0:
    d = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + d

print('"Обратное" число:',n2)
