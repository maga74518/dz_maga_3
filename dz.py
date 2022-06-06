a = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'Ноль', 'Один', 'Два',
     'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять']
b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'Zero',
     'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
num = input()


def num_translate():
    for i in range(len(b)):
        if b[i] == num:
            return print(a[i])


def num_translate_1():
    for i in range(len(a)):
        if a[i] == num:
            return print(b[i])


num_translate() if num in b else num_translate_1()
