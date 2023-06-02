init:
##Музыка##

    $ renpy.music.register_channel("sound_menu1","sfx",False)
    $ renpy.music.register_channel("ch1","sfx")
    $ renpy.music.register_channel("ch2","sfx")

##Персонажи##

        #--Основные--#
    define question = Character('???', color="#9b9569")
    define narrator = Character(what_italic=True)
    define maks = Character('Макс', color="#EB6969")
    define ira = Character('Ира', color="#EBE469")
    define kolya = Character('Коля', color="#3DAE69", image = "kolya")
        #--Переменные--#
    define help.ira = False #День3-День4
    define scam.boris= False #День6
    define walk.ira = False #День8
    define bolk.ira = False #День10-День11
    define cabluk.ira = False #День9-День10
    define ratirl.ira = False #День10
    define scam.redhead = False #День11
    define balls.ira = 0 #Да в принцпипе все ебанные блок схемы
    define balls.tanya = 0 #Да в принцпипе все ебанные блок схемы
    define connect.bench = False #День12
    define nora.ira = False #День11-День12
##Спрайты##
        #--Пример спрайт с эмоцией--#
    #image pan happy = "images/sprites/pan/p_happy.png"
    #image pan sad = "images/sprites/pan/p_sad.png"
##Фоны##
    #image map = "images/bg/map.png"

##Анимация перехода##

    #--Двое--#
    transform jump1_2:
        xcenter 0.30 ycenter 0.71
        linear 0.15 ycenter 0.69
        linear 0.1 ycenter 0.71

    transform jump2_2:
        xcenter 0.70 ycenter 0.71
        linear 0.15 ycenter 0.69
        linear 0.1 ycenter 0.71

    #--Трое--#
    transform jump1_3:
        xcenter 0.20 ycenter 0.71
        linear 0.15 ycenter 0.69
        linear 0.1 ycenter 0.71

    transform jump2_3:
        xcenter 0.5 ycenter 0.71
        linear 0.15 ycenter 0.69
        linear 0.1 ycenter 0.71

    transform jump3_3:
        xcenter 0.80 ycenter 0.71
        linear 0.15 ycenter 0.69
        linear 0.1 ycenter 0.71

#Переменные
    #$ persistent.start = False

###################################################################################
init python:
    def percent():
            global result
            global dialogue
            seen = renpy.count_seen_dialogue_blocks()
            result = seen * 100 / dialogue
