last_data = {'гироскутер': 70, 'автобус': 80, 'трамвай': 90}

with open('magazine.txt', 'a+', encoding='utf-8') as file:
    for key, value in last_data.items():
        file.write(f"{key} = {value}\n")

    file.seek(0)

    print(file.read())
