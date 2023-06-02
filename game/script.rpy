﻿label start:

    $ save_name = "Начало"
    #jump day11
    show kolya normal at jump2_3
        
    kolya "Серый день сменяется тусклой ночью. Многоэтажные дома словно стены средневековых замков, окружают жилую территорию этого гетто."
    kolya "Я не знаю, почему некогда цветущая окраина города, которую я видел с билбордов на автостраде, превратилась в загнивающий клоповник, где каждый пытается выжить, цепляясь за любую возможность, на сколько бы не была тонка эта нить."
    kolya "И вот я, сидящий на этом каменном подоконнике. Сделав из него ложу, я получил вполне хорошее пригретое местечко в холодном мире."

#ДЕНЬ1
label day1:
    label event1_1: #Монолог
        "Рассказ и показ мира от лица ГГ-шки"
    label event1_2: #Событие
        "Показ Базы и персонажей в банде"
#ДЕНЬ2
label day2:
    label event2_1: #Событие
        "Женя узнает о Синдикате переговаривается с ним об операции"   
    label event2_2: #Событие
        "ГГ-шка по пути домой встречает Иру"
#ДЕНЬ3
label day3:
    label event3_1: #Событие
        "ГГ-шка встречает Иру утром"    
    label event3_2: #Выбор
        menu:
            "Помочь ли Ире завтра с волонтерством"
            "Хорошо, почему бы и нет?":
                $ help.ira= True
            "Прости, у меня завтра дела":
                pass                
    label event3_3: #Событие
        "Сбор на базе и подготовка первых ступеней плана операции"
        if help.ira:
            jump day4_1
        else:
            jump day4_2
#ДЕНЬ4 ПО ПУТИ ИРЫ              
label day4:
    label event4_1: #Событие +1Ире
        "ГГ-шка все утро помогает ей с бездомными готовя им и разнося еду"
    label event4_2: #Событие 
        "ГГ-шка опаздывает на встречу, из-за чего встречается только с рассерженной Женей, получает план от нее"
    label event4_3: #Монолог
        "ГГ-шка один отправляется домой"
#ДЕНЬ4 ПО ПУТИ ТАНИ
label day4_1:
    label event4_1_1: #Событие +1Тане
        "ГГ-шка проходит на базу утром и застает Таню до прихода все остальных"
    label event4_1_2: #Событие 
        "Банда собирается с обсуждением плана"
    label event4_1_3: #Событие
        "ГГ-шка прогуливается до дома с Таней" #не влияет ни на что    
#ДЕНЬ5 
label day5:
    label event5_1: #Событие
        "ГГ-шка встречается с Колей на крыше здания на против дорогого дома"
    label event5_2:
        "ГГ-шка делает обход с правой стороны встречаясь с Ирой"
        if help.ira: #Событие
            pass #Если он ей помогал, то будет доп фраза от Иры
    label event5_3: #Событие
        "ГГ-шка встречается с Колей и обсуждают осмотры"
    label event5_4: #Монолог
        "ГГ-шка идем домой"
#ДЕНЬ6
label day6: 
    label event6_1: #Событие
        "Встреча с Пьяной Тетей и уход из дома"
    label event6_2: #Выбор
        "На базе банды Борис с Колей"
        menu:
            "Сказать Коле о том, что Борис жульничает"
            "Коль посмотри туда":
                "Коля прекращает игру с Борисом переходя на борьбу"
            "Сам догадается":
                    pass

    label event6_3: #Событие
        "Встреча с Женей на крыше заброшки"
#ДЕНЬ7
label day7:
    label event7_1: #Монолог
        "Кошмары"
    label event7_2: #Событие
        "Таня будет ГГ-шку"
    label event7_3: #Событие
        "Поход с Женей для встречи с Синдикатом во дворах"
#ДЕНЬ8
label day8:
    label event8_1: #Событие
        "Встреча с Ирой у Магазина"
    label event8_2: #Выбор
        menu:
            "Прогуляться по парку с ней?"
            "Просто, но я сегодня не в духе":
                pass
            "Давай, хороший денек":
                $ walk.ira =True
        if walk.ira == True:
            jump event8_3  
        else:
            jump event8_3_1
    label event8_3: #Событие по пути Тани +1Тане
        "Возвращение на базу с продуктами"
    label event8_4: #Событие
        "разговор на подоконнике"
        jump day9
    label event8_3_1: #Событие по пути Иры +1Ире
        "Прогулка по парку с девушкой"
    label event8_4_1: #Событие
        "Возвращение на базу и разговоры по телефоны с Ирой"
#ДЕНЬ9
label day9:
    label event9_1: #Событие
        "Подготовка, изучением"
    label event9_2: #Событие
        "Таня приготовила хотдоги"
    label event9_3: #Выбор
        "Игра в баскетбол против других парней"
        menu:
            "Пойти играть с ними?"
            "Давай сюда мяч":
                "Мы играем"
            "Нет, я пойду лучше полежу":
                pass
    label event9_4: #Событие
        "Увищел с окна Иру таскающую тяжелые ящики"
    label event9_5: #Выбор
        menu:
            "Помочь девушке?"
            "Я что, не мужик?":

                jump event9_6
            "Я и так устал":
                $ cabluk.ira = True
                jump event9_6_1
    label event9_6: # Событие по пути Иры +1
        "Помогаешь разгрузить машину"
        
    label event9_6_1: #Событие по пути Тани +1
        "Игра в приставку"
#ДЕНЬ10
label day10:
    label event10_1: #Событие
        "Прогулка до магазинаю, в"
    label event10_2: #Событие
        "Помогаешь девушке донести пакеты до дома"
        if cabluk.ira:
            "Доп фраза, узнает, что Ира живет в дорогом доме"
    label event10_3: #Выбор
        menu: 
            "Прогуляться с Ирой по парку?"
            "Давай":
                pass
            "У меня сегодня есть":
                    jump event10_4_1
    label event10_4: #Событие по пути Иры +1
        "Прогулка по парку с девушкой"
        if walk.ira:
            "Если он уже с ней гулял, то доп фразы"
    label event10_5: #Выбор
        menu:
            "Ира уснула, но не выключила телефон"
            "Нет, я не могу":
                jump event10_6
            "Хм, что ей написали":
                jump event10_6_1
    label event10_4_1: #Событие по пути Тани +1
        "Проработка планов на базе"
    label event10_5_1: #Событие тут автор умрет от кринжа R.I.P.
        "Сегодня очень лунная ночь"   
        jump day11_1 
    label event10_6: #Событие
        "Возвращение на базу, оказывается Коля много увидел"
    label event10_7: #Выбор
        menu:
            "Все знают, что ты общаешься с девушкой из того дома"
            "Да, и я скажу, что это хорошие новости":
                if ratirl.ira:
                    "Если он читал переписки, то будет дополнительные  фразы"
                jump day11 
            "Это случайность, я просто помог ей":
                jump day11_1
    label event10_6_1: #Событие
        "Изучение переписок"
    label event10_7_1: #Событие
        "Возвращение на базу, оказывается Коля много увидел"
        jump event10_7
#ДЕНЬ11 Открывает Циничную концовка 
label day11: 
        label event11_1: #Событие
            "Женя будет ГГ-шку, его задача сегодня будет сбор информации"
        label event11_2: #Событие
            "Встреча с Ирой у волонтерской конторы"
        label event11_3: #Выбор
            menu:
                "Спросить ее о прогулке?"
                "Ир, не хочешь прогуляться сегодня?":
                    jump event11_4
                "Да, денек хороший":
                    jump event11_4_1
        label event11_4: #Событие
            "Прогулка по парку с девушкой"
        label event11_5: #Событие по пути Тани +1
            "Что ты тут делаешь Тань?"
        label event11_6: #Событие
            "Прогулка по дорогому дому"
            jump event11_7
        label event11_4_1: #Событие
            "Помощь волонтерам"
        label event11_5_1: #Событие по пути Иры +1
            "Встреча с отцом Иры"
        label event11_6_1: #Событие
            "Прогулка по дорогому дому"
        label event11_7: #Выбор
            menu:
                "Расказать Ире о прошлом?"
                "Нет, ничего":
                    jump event11_8
                "Ир, тут такое":
                    jump event11_8_1
        label event11_8: #Событие по пути Тани +1
            "ГГ-шка увидел сообщение от Тани"
            "ГГ-шка встретит Таню"
            jump event11_folpancookielol
        label event11_8_1: #Событие по пути Иры +1
            "Хорошо провели время, но ГГ-шка замечает пропущенный вызов от Тани"
            "ГГ-шка придет позже"
            jump event11_folpancookielol
        label event11_folpancookielol: #Самый кукилоловский выбор
            menu:
                "Рассказать про то, что увидел в дорогом доме?"
                "И так с чего начать...":
                    pass
                "Нет, я ничего не узнал особого":
                    jump event11_1_5
        label event11_9: #Событие
            "ГГ-шка дополняет план, открывается выбор позже"
            $ nora.ira = True
        jump day12
#ДЕНЬ11 хуй его знает, что тут писать
label day11_1:
    label event11_1_1: #Выбор
        menu:
            "Кто прав?"
            "Борис, Пламя не зря ночью пост сторожила":
                jump event11_1_2
            "В его словах есть доля правды":
                $ scam.redhead = True
    label event11_1_2: #Событие
        "Коля попадает в драку"
    label event11_1_3: #Событие
        "Разбработка плана"
        if bolk.ira:
            "Если он гулял с Ирой, то будут дополнительные фразы"
    label event11_1_4: #Событие
        "Поход в магазин с Борисом за расходниками для операции"
        if scam.redhead:
            "Если выбор был на стороне Бориса, то будут дополнительные фразы"
    label event11_1_5: #Событие
        "Доработка плана"
#ДЕНЬ12
label day12:
    label event12_1: #Монолог
        "Кошмар"
    label event12_2: #Событие
        "Женя с Колей и Борисом уходят на заключительную разведку, оставив ГГ-ку и Таню для подготовки снаряжения"
    label event12_3: #Выбор
        menu:
            "Таня предлагает прогуляться до магазина за энергертиками"
            "Прости, мне не очень хочется сейчас гулять":
                jump event12_4
            "Давай, а то я свихнусь с этими веревками":
                jump event12_4_1
    label event12_4: #Монолог по пути Иры +1
        "ГГ-шка во время перебирания веревок обдумывает операцию"
    label event12_5: #Событие
        "Возвращение остальных"
    label event12_4_1: #Событие по пути Тани +1
        "Прогулка по магазина и до остановка на скамейке"
    label event12_5_1: #Событие
        "Встреча остальных у базы"
        $ connect.bench=True
    label event12_6: #Событие
        "заключительная подготовка"
        if connect.bench:
            "Если они сидели на скамейке, то будут дополнительные фразы"
        if balls.ira >= 4:
            menu:
                "Позвонить Ире?"
                "Ира не заслужила этого":
                    jump event12_7
                "Нет, если взялись нужно идти до конца":
                    jump event12_7_1
    label event12_7: #Событие
        "До начала операции ГГ-шка сбегает на встречу с Ирой"
    label event12_8: #Событие 
        "ГГ-шка рассказывает все Ире и они доходят до того, что нужно отговорить остальных"
    label event12_9: #Событие 
        "Вернувшись на базу ГГ-шка не находит остальных, но находит записку от Тани"
        if connect.bench:
            "В записке как раз будет описыватсья ее симпатия, если он с ней до этого сидел на скамейке, то будет дополнительные фразы"
    label event12_10: #Событие 
        "ГГ-шка с Ирой готовятся дома встретить банду"
    label event12_11: #Событие 
        "Встреча с бандой. попытка договориться"
    label event12_12: #Событие 
        "Борис достает пистолет, что бы престрелить ГГ-шку за предательство"
    label event12_13: #Событие 
        "Таня успевает спасти ГГ-шку, но выстрел попадает ей в живот"
    label event12_14: #Событие 
        "Таня умирает на руках, родители Иры спускаются узнать, что за шум"
    label event12_7_1: #Событие
        if nora.ira:
            menu:
                "Пролезть ли через потойной путь Иры?" 
                "Да":
                    jump event12_8_3
                "Нет":
                    jump event12_8_2
        else:
            jump event12_8_2
    label event12_8_2: #Событие
        "Проникновение"
    label event12_9_2: #Событие
        "Установка взрывчатки и тихий выход из дома"
    label event12_10_2: #Событие
        "Конец истории"
    label event12_9_3: #Событие
        "Встреча Иры"
    label event12_10_3: #Событие
        "Ира успевает позвонить в полицию и позвать родителей"
    label event12_11_3: #
        "Борис достает пистолет"
    label event12_12_3: #
        "Бомба установлена, но дом оцепили копы"
    label event12_13_3: #
        "Перестрелка, один из копов пытается застрелить ГГ-шку, но Таня спасает его собой"
    label event12_14_3: #
        "Таня умирает на руках, а заряд детонирует"
    label event12_15_3: #
        "ГГ-шка выживает и видит последствие взрыва"
    
    

    






