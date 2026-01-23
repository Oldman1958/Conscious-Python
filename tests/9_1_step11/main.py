"""with open('new_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write("Это первая строка.\n")
    new_file.write("Это вторая строка.\n")"""

"""with open('my_files/new_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write("Это первая строка.\n")
    new_file.write("Это вторая строка.\n")"""

"""with open('my_files/new_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write("Удалили весь текст.\n")"""

with open('my_files/new_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write("Буря мглою, ")
    new_file.write("небо кроет\n")

with open('my_files/new_text.txt', 'r', encoding='utf-8') as new_file:  # режим чтения
    print(new_file.read())


