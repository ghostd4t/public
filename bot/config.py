from itertools import cycle
TOKEN = 'TOKEN_HERE' #BOT TOKEN

REACTION = 'Слышб, че высрал'
kamenshik = 'Я бот работаю 3 дня без апдейтов и не отдам вам await message.channel.send'

responses =  ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
              'Мне кажется — «да»',
              'Вероятнее всего',
              'Хорошие перспективы',
              'Знаки говорят — «да»',
              'Да',
              'Пока не ясно, попробуй снова',
              'Спроси позже', 'Лучше не рассказывать',
              'Сейчас нельзя предсказать',
              'Сконцентрируйся и спроси опять',
              'Даже не думай',
              'Мой ответ — «нет»',
              'По моим данным — «нет»',
              'Перспективы не очень хорошие',
              'Весьма сомнительно']
winx = ['Блум','Стелла','Флора',"Текна","Муза","Лейла"]

status = cycle(['on Blizzard World', 'on Busan', 'on Dorado', 'on Eichenwalde', 'on Hanamura', 'on Havana', 'on Hollywood', 'on Ilios', 'on Junkertown', 'on King\'s Row',
                'on Lijiang Tower', 'on Necropolis', 'on Nepal', 'on Numbani', 'on Oasis', 'on Rialto', 'on Route 66', 'on Temple of Anubis', 'on Volskaya Industries',
                'on Watchpoint: Gibraltar'])
###
#@client.event   #bot return if working
#async def on_ready():
    #print('We have logged in as {0.user}'.format(client))
#async def on_message(self,message):
    #print('{0.author}: {0.content}'.format(message))