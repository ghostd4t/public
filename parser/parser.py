import requests
import time#время в методах измеряется в секундах(то есть 1 час = 60*60 = 3600
from datetime import datetime
from bs4 import BeautifulSoup as BS


work = 1 #отвечает за работу второго(основного цикла - парсера)

prevd = 0 #в этой переменной будет содержаться предыдущая дата, для сравнения с актуальной датой, что бы программа -
          #смогла распознать когда происходит смена дней и запускала парсер(выставил как 0 т.к. нулевой даты в календаре нет и этот
          #ноль нам нужен только для запуска программы (в дальнейших итерациях эта переменная будет переписываться автоматически)


prevdata = ''#в этой переменной будет содержаться предыдущая строка данных, для сравнения с актуальной версией строки расписания, что бы программа -
             #смогла распознать когда происходит смена (заменяется автоматически)

while True: #первичный цикл парсера
    d = datetime.now()
    d = d.day # получаем дату на сегодняшний день
    if d != prevd:#сравниваем дату с предыдущим днем(т.к. изначально я взял 0 запустится вторичный цикл всегда)
        while work != 0:#вторичный цикл(основной)
            r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSIVERYGBU3-BQoWOdBt1luNnxQLKmjvGReoehhi7gqJ-xqmuNzOrXp3RGptEqZ2On_uVxHW3OqkIhm/pubhtml')
            print(r)#получаем запрос от сайта и обрабатываем ответ
            html = BS(r.content, 'html.parser')
            element = html.select('tbody')
            element = str(element[0].text)#парсим контент таблицы(все расписание в одну строку и переводим в текст
            #element = element[97:] - (это не трогай, я оставил для теста)
            if element == prevdata:#сравниваем данные с предыдущей сохраненной информацией
                time.sleep(3600)#если данные совпадают(то есть день сменился, но расписание пока что не изменилось), ждем 1 час, потом снова идем запращивать данные
            else:
                #если данные не совпали и мы получили новое расписание:
                prevdata = element#откладываем в prevdata новое расписание, что бы уже с ним шло сравнение в дальнейших итерациях
                print('u have new')
                print(element)
                """
                тут  нужно отдать комманду боту с отправкой уведомления о новом расписании
                """
                time.sleep(72000)#если бот отработал расписание ждем 20 часов что бы не грузить систему
                work = 0#выходим из цикла парсинга (основного, попадаем в первичный цикл ожидания смены дня)
        prevd = d #заменяем после отправки расписания актуальную дату на устаревшую для дальнейших итераций

    else:
        time.sleep(14400)#если день не поменялся то делаем новый запрос через 4 часа


