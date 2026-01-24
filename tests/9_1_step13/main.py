with open('my_files/new_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.write("Буря мглою ")
    new_file.write("небо кроет\n")

with open('my_files/new_text.txt', 'a', encoding='utf-8') as new_file:
    new_file.write('Вихри снежные крутя;\n')
    new_file.write('То, как зверь, она завоет,\n')
    new_file.write('То заплачет, как дитя,\n')
    new_file.write('То по кровле обветшалой\n')

"""with open('my_files/new_text.txt', 'x', encoding='utf-8') as new_file:
    new_file.write('Вихри снежные крутя;\n')
    new_file.write('То, как зверь, она завоет,\n')
    new_file.write('То заплачет, как дитя,\n')"""

with open('my_files/new_text.txt', 'a+', encoding='utf-8') as new_file:
    new_file.write("Вдруг соломой зашумит,\n")
    new_file.write("То, как путник запоздалый,\n")
    new_file.write("К нам в окошко застучит.\n")
    new_file.seek(0)  # вернём курсор в начало, чтобы прочитать полностью
    print(new_file.read())

data = ['Наша ветхая лачужка\n', 'И печальна и темна.\n',
        'Что же ты, моя старушка,\n', 'Приумолкла у окна?\n',
        'Или бури завываньем\n', 'Ты, мой друг, утомлена,\n',
        'Или дремлешь под жужжаньем\n', 'Своего веретена?']

with open('my_files/new_text.txt', 'a', encoding='utf-8') as new_file:
    new_file.writelines(data)

with open('my_files/new_text.txt', 'r', encoding='utf-8') as text:
    data = text.readlines()

with open('my_files/some_text.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(data)
