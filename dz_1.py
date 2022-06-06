import random

list, list_1 = [], []

nouns = {1: "автомобиль", 2: "лес", 3: "огонь", 4: "город", 5: "дом"}
adverbs = {1: "сегодня", 2: "вчера", 3: "завтра", 4: "позавчера", 5: "ночью"}
adjectives = {1: "веселый", 2: "яркий", 3: "зеленый", 4: "утопичный", 5: "мягкий"}

n = int(input())

def get_jokes(n):
    for i in range(n):
        list.append(nouns[random.randint(1, 5)]), list.append(adverbs[random.randint(1, 5)]),
        list.append(adjectives[random.randint(1, 5)])
        f = ' '.join(list)
        list_1.append(f)
        list.clear()
    return list_1

print(get_jokes(n))