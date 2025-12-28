"""
Сюжет:
Алон планирует модернизировать свой ПК, используя свои навыки программирования.
У него имеется словарь из 20 товаров с указанием их цен.
Его задача — отфильтровать словарь и выбрать товары, стоимость которых больше или равна 15000,
но меньше или равна 20000.
Алон осознает, что эту задачу можно решить различными методами,
но решил сосредоточиться на применении генераторных выражений для закрепления соответствующих навыков.

computer_products = {
    "Процессор Intel Core i7-11700K": 30000,
    "Процессор AMD Ryzen 5 5600X": 20000,
    "Видеокарта NVIDIA GeForce RTX 3060": 40000,
    "Видеокарта AMD Radeon RX 6700 XT": 45000,
    "Материнская плата ASUS ROG Strix B550-F": 15000,
    "Материнская плата MSI MPG Z490 Gaming Edge": 18000,
    "Оперативная память Corsair Vengeance LPX 16GB": 8000,
    "Оперативная память G.Skill Trident Z RGB 32GB": 16000,
    "SSD Samsung 970 EVO Plus 1TB": 12000,
    "SSD Kingston A2000 500GB": 5000,
    "Жесткий диск Seagate Barracuda 2TB": 6000,
    "Жесткий диск Western Digital Blue 1TB": 4000,
    "Блок питания Corsair RM750x": 10000,
    "Блок питания be quiet! Straight Power 11 750W": 9000,
    "Корпус NZXT H510": 7000,
    "Корпус Cooler Master MasterBox Q300L": 4000,
    "Монитор Dell UltraSharp U2720Q": 50000,
    "Монитор ASUS TUF Gaming VG27AQ": 30000,
    "Клавиатура Logitech G Pro X": 12000,
    "Мышь Razer DeathAdder V2": 5000
}


Задание:
Словарь computer_products уже создан волшебным образом.
Используйте генераторное выражение и создайте генератор, который будет состоять из имён товаров,
которые по цене больше или равны 15000, но меньше или равны 20000.
Выведите на экран имена всех подходящих условию товаров (см. Sample Output).
Советы:

В генераторном выражении используется обычный цикл for и с ним можно делать всё, что вы уже делали ранее.

Вспомните, как с помощью цикла можно обращаться одновременно и к ключу, и к значению словаря.
"""

computer_products = {
    "Процессор Intel Core i7-11700K": 30000,
    "Процессор AMD Ryzen 5 5600X": 20000,
    "Видеокарта NVIDIA GeForce RTX 3060": 40000,
    "Видеокарта AMD Radeon RX 6700 XT": 45000,
    "Материнская плата ASUS ROG Strix B550-F": 15000,
    "Материнская плата MSI MPG Z490 Gaming Edge": 18000,
    "Оперативная память Corsair Vengeance LPX 16GB": 8000,
    "Оперативная память G.Skill Trident Z RGB 32GB": 16000,
    "SSD Samsung 970 EVO Plus 1TB": 12000,
    "SSD Kingston A2000 500GB": 5000,
    "Жесткий диск Seagate Barracuda 2TB": 6000,
    "Жесткий диск Western Digital Blue 1TB": 4000,
    "Блок питания Corsair RM750x": 10000,
    "Блок питания be quiet! Straight Power 11 750W": 9000,
    "Корпус NZXT H510": 7000,
    "Корпус Cooler Master MasterBox Q300L": 4000,
    "Монитор Dell UltraSharp U2720Q": 50000,
    "Монитор ASUS TUF Gaming VG27AQ": 30000,
    "Клавиатура Logitech G Pro X": 12000,
    "Мышь Razer DeathAdder V2": 5000
}

gen = (k for k, v in computer_products.items() if 20000 >= v >= 15000)
print(*gen, sep='\n')
