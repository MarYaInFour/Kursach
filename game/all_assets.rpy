init:
##Музыка##

    $ renpy.music.register_channel("sound_menu1","sfx",False)
    $ renpy.music.register_channel("ch1","sfx")
    $ renpy.music.register_channel("ch2","sfx")

##Персонажи##

        #--Основные--#
    define question = Character('???', color="#FFFFFF")
    define narrator = Character(what_italic=True)
    define maks = Character('Макс', color="#FFFFFF")
    define ira = Character('Ира', color="#FFFFFF")
        #--Переменные--#
    define help.ira = False #День3-День4
    define scam.boris= False #День6
    define walk.ira = False #День8
##Спрайты##

        #--Пример сайд имедж--#
    #image side shiken neutral = "images/side_images/shiken_neutral.png"

        #--Пример спрайт с эмоцией--#
    #image pan happy = "images/sprites/pan/p_happy.png"
    #image pan sad = "images/sprites/pan/p_sad.png"

##Фоны##
    #image map = "images/bg/map.png"

##Анимация перехода##

    #--Двое--#
    transform jump_1_2:
        xcenter 0.30 ycenter 0.60
        linear 0.15 ycenter 0.58
        linear 0.1 ycenter 0.60

    transform jump_2_2:
        xcenter 0.70 ycenter 0.60
        linear 0.15 ycenter 0.58
        linear 0.1 ycenter 0.60

    #--Трое--#
    transform jump_1_3:
        xcenter 0.20 ycenter 0.60
        linear 0.15 ycenter 0.58
        linear 0.1 ycenter 0.60

    transform jump_2_3:
        xcenter 0.5 ycenter 0.60
        linear 0.15 ycenter 0.58
        linear 0.1 ycenter 0.60

    transform jump_3_3:
        xcenter 0.80 ycenter 0.60
        linear 0.15 ycenter 0.58
        linear 0.1 ycenter 0.60

#Переменные
    #$ persistent.start = False

###################################################################################
init python:
    def percent():
            global result
            global dialogue
            seen = renpy.count_seen_dialogue_blocks()
            result = seen * 100 / dialogue
