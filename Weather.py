# for i in range(5):
#     print('Python')
#
# for i in 'Python':
#     print(i)

# age = int (input('Сколько Вам лет?'))
#
# if age <=7:
#     print('В какой садик ты ходищь?')
# elif 7 <= age <= 18:
#     print('В какую школу ты ходишь ')
# else:
#     print('Пора сдохнуть')
# st = 'м.у$т^а>б(о@р'
# for i in st:
#     if not i.isalpha():
#         print('True')
#     else:
# #         print('False')
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
# for i in lst:
#     print(*i)

# my_dict = {'цвет': 'красный', 'артикул': 'ABC123', 'цена': 650}
# for k, v in my_dict.items():
#     print(f'{k} - {v}')


# for i in range(10):
#     print('*' * i)

ops = {'-':'a - b', '+':'a + b', '*': 'a * b', '/':'a / b'}
a, b = int(input('Введите значение a: ')), int(input('Введите значение b: '))
op = input('Введите знак операции: ')
if op in ops.keys():
    print(eval(ops[op]))
else:
    print('Поддерживаются операции +, -, * и /')