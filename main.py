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


def meeting():
    while True:
        a = input('Как тебя зовут? \n')
        a = " ".join(a.split())
        if any(letter.isdigit() for letter in a):
            print('А давно цифры стали именами?')
        elif any(letter for letter in a if not re.search('[а-яА-Я]', letter)):
            print('Какое то неправильное имя, давай без приколов')
        else:
            print('Здравствуй,', a)
            return


def asking():
    while True:
        c = input('Спрашивай, что хочешь, а я отвечу \n')
        " ".join(c.split())
        if any(letter for letter in c if re.search('[а-яА-Я|\\s?$]', letter)):
            print(random.choice(answers))
            return
        else:
            print('Это вовсе не вопрос')


def repeat():
    while True:
        b = input('Если хочешь задать еще вопрос, нажми "д", если нет - "н" \n')
        " ".join(b.split())
        if b == 'н':
            print('Возвращайся, если возникнут вопросы!')
            time.sleep(2)
            return
        elif b == 'д':
            asking()
        else:
            print('Некорректный символ')


meeting()
asking()
repeat()
