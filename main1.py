# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

a = int(input('Ввведите сторону a: '))
b = int(input('Ввведите сторону b: '))
c = int(input('Ввведите сторону c: '))
if a <= 0 or b <= 0 or c <= 0:
    print('Такого треугольника не существует')
elif a + b < c or a + c < b or b + c < a:  
    print('Такого треугольника не существует')
elif a != b & b!= c & c != a:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')