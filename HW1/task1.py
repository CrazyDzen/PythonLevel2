import os
import chardet


# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
# Unicode и также проверить тип и содержимое переменных.


def task_one(word):
    print('задание первое')
    for el in word:
        print(f'Тип: {type(el)} и содержание: {el}')
    print('-' * 20)


task_one(["разработка", "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430", "сокет",
          "\u0441\u043e\u043a\u0435\u0442", "декоратор", "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"])


# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


def task_two(word):
    print('задание второе')
    for el in word:
        print(f'Тип: {type(el)}, содержание: {el} и длина {len(el)}')
    print('-' * 20)


task_two(["\x63\x6c\x61\x73\x73", "\x66\x75\x6e\x63\x74\x69\x6f\x6e", "\x6d\x65\x74\x68\x6f\x64"])


# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


def task_three(word):
    print('задание третье')
    for el in word:
        try:
            print(f"'{el}' - в байтовом виде: {bytes(el, encoding = 'ASCII')}")
        except UnicodeEncodeError:
            print(f"'{el}' - не может быть представлен в байтовом виде")
    print('-' * 20)


task_three(["attribute", "класс", "функция", "type"])


# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).


def task_four(word):
    print('задание четвертое')
    for el in word:
        el_dec = el.encode('utf-8')
        print(f"{el_dec} - {el_dec.decode('utf-8')}")
    print('-' * 20)


task_four(["разработка", "администрирование", "protocol", "standard"])


# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового
# в строковый тип на кириллице.


print('задание пятое')
recourse = "yandex.ru"
print(os.system("ping -n 1 " + recourse))
print('-' * 20)


# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode
# и вывести его содержимое.

print('задание шестое')
file_name = 'test_file.txt'
with open(file_name, 'rb') as f:
    res = chardet.detect(f.read())['encoding']
    print(f'кодировка - {res}')
with open(file_name, 'r', encoding=res) as f:
    print(f.read())
