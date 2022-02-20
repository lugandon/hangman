import random

word_list = ['яблоко','груша','', 'ручка','портфель','антена','стекло','учебник','стол','клавиатура']

rndm = random.randint(0, len(word_list)-1)
word = word_list.pop(rndm)
solve = list('_' * len(word))
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
attempts = 0

theme = {

}

if word == 'яблоко' or word == 'груша':
    print('Фрукт ростущий на дереве')
elif word == 'ручка' or word == 'портфель' or word == 'учебник':
    print('Школьная пренадлежность')
elif word == 'антена':
    print('Используется для ловли связи и т.д.')
elif word == 'стекло':
    print('Рассыпчатое вещество, превращающаяся в прозрачный предмет')
elif word == 'стол':
    print('Мебель')
elif word == 'клавиатура':
    print('На ней есть много символов')

print(solve)
print('')
print(alphabet)

while attempts != 3 and '_' in solve:
    user_word = input('Введите букву:')
    if user_word in solve:
        print('Вы уже вводили эту букву')
    elif user_word in word:
        print('Вы выбрали правильную бувку!')
        if user_word in alphabet:
            alphabet.remove(user_word)
            print(alphabet)
        for i in range(len(word)):
            if user_word == word[i]:
                solve[i] = user_word
                print(' ')
                print(solve)
    else:
        print('Такой буквы нет в слове')
        attempts += 1
if attempts >= 3:
    print('Ты проиграл!')
else:
    print('Ты выиграл!')