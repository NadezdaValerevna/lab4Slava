def count_elements(lists):
    if not lists:
        return 0

    # Создаем множество из элементов первого списка
    common_elements = set(lists[0])

    # Перебираем оставшиеся списки и обновляем множество общих элементов
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)

n = int(input("Введите количество списков: "))
lists = []

for _ in range(n):
    lst = list(map(int, input("Введите элементы списка, разделенные пробелами: ").split()))
    lists.append(lst)

print("Количество одинаковых элементов в списках:", count_elements(lists))