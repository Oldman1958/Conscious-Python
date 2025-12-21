"""
Сюжет:
Алон создаёт программу отбора людей на определённую должность для компании "Пожилые акробаты".
В программу поступает список из анкет (словарей), состоящих из имени, возраста и вредных привычек.
Программа сортирует эти анкеты и размещает самых желанных людей выше по списку.
Компания хочет нанять людей без вредных привычек и чем старше человек, тем лучше.

Задание:
Уже создан список из словарей persons. Например:
persons = [{'name': 'Alisa', 'age': 29, 'bad_habits': False},
           {'name': 'Valera', 'age': 89, 'bad_habits': True},
           {'name': 'Kirill', 'age': 99, 'bad_habits': False}]


Нужно отсортировать этот список из словарей, по двум приоритетам:
- В самом начале списка всегда должны располагаться словари, с ключами 'bad_habits': False,
то есть люди не имеющие вредных привычек.
- Среди людей, не имеющих вредных привычек, первыми в списке должны идти люди старшего возраста, а затем более молодые.
Например:
{'name': 'Kirill', 'age': 99, 'bad_habits': False}
{'name': 'Alisa', 'age': 29, 'bad_habits': False}
{'name': 'Valera', 'age': 89, 'bad_habits': True}


Сначала идут люди без вредных привычек, затем с вредными.
Людей без вредных привычек двое, поэтому первым идёт человек более старшего возраста, а затем более молодого.
Таким образом, Kirill более предпочтительный кандидат для компании.
Отсортированный список из словарей, выведите на экран с помощью цикла (см. Sample Output).
"""
'''

persons = [{'name': 'Alisa', 'age': 29, 'bad_habits': False},
           {'name': 'Valera', 'age': 89, 'bad_habits': True},
           {'name': 'Kirill', 'age': 99, 'bad_habits': False}]
'''

persons = [{'name': 'Kenny', 'age': 18, 'bad_habits': False},
           {'name': 'Night', 'age': 66, 'bad_habits': True},
           {'name': 'West', 'age': 55, 'bad_habits': True},
           {'name': 'Tommy', 'age': 20, 'bad_habits': True},
           {'name': 'Jimmy', 'age': 100, 'bad_habits': False}]


def sort_two_key(d: dict) -> tuple:
    return d['bad_habits'], -d['age']

sorted_persons = sorted(persons, key=sort_two_key)
print(*sorted_persons, sep="\n")
