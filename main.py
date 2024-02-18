import random
print('привет давай поиграем в виселицу!?')
input("нежми enter что бы продолжить ")
print('начинаем!!!')
win = True
words = ['собака', 'кошка', 'учебник' ,'двоечка' , 'ножницы']
word = random.choice (words)
letters = []
hp = 10
while hp > 0:
    win = True
    letter = input('ведите букву ')
    letters.append(letter)
    for symb in word:
        if symb in letters:
            print(symb, end=" ")
        else:
            print('*',end = ' ')
            win = False
    print()
    if win:
        print('Ты победил!!!')
        break
    if letter not in word:
        hp -= 1
        print(f'осталось жизней {hp}')
if hp == 0:
    print('ты проиграл')