import random
import re
import time
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
          'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
          'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', '	Сейчас нельзя предсказать',
          'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
          'Перспективы не очень хорошие', 'Весьма сомнительно']


print('Привет, Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Ответом на вопрос должно быть да или нет')

def has_cyrillic(text):
    for i in text:
        if not bool(re.search('[а-яА-Я]', i)):
            return False
        else:
            text = text.rstrip()
            return text

def meeting():
    while True:
        a = input('Как тебя зовут? \n')
        for i in a:
            if i == ' ':
                a = a.strip()
            else:
                a = a.rstrip()
        if a.isdigit():
            print('А давно цифры стали именами?')
        elif a.isalpha() and has_cyrillic(a):
            print('Здравствуй,', a)
            break
        else:
            print('Какое то неправильное имя, давай без приколов')


def asking():
    while True:
        c = input('Спрашивай, что хочешь, а я отвечу \n')
        for i in c:
            if i == ' ':
                c = c.strip()
            else:
                c = c.rstrip()
        if c[len(c) - 1:] == '?' and all(x.isspace() or x.isalnum() for x in c) and has_cyrillic(c):
            print(random.choice(answers))
            break
        else:
            print('Это вовсе не вопрос')


def repeat():
    while True:
        b = input('Если хочешь задать еще вопрос, нажми "д", если нет - "н" \n')
        for i in b:
            if i == ' ':
                b = b.strip()
            else:
                b = b.rstrip()
        if b == 'н':
            print('Возвращайся, если возникнут вопросы!')
            time.sleep(2)
            break
        elif b == 'д':
            asking()
        else:
            print('Некорректный символ')


meeting()
asking()
repeat()
