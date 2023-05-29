#### Экран Экстра

init python:
    mg= MusicRoom()
    mg.add("track1.ogg", always_unlocked=True)
    mg.add("track2.ogg")
    mg.add("track3.ogg")

    g = Gallery()
    g.button("cg_gallery01")
    g.image("image1")
    g.unlock("image1")

    g.button("cg_gallery02")
    g.image("image2")
    g.unlock("image2")

    g.button("cg_gallery03")
    g.image("image3")
    g.unlock("image3")

    g.button("cg_gallery04")
    g.image("image4")
    g.unlock("image4")

    g.button("cg_gallery05")
    g.image("image5")
    g.unlock("image5")

    g.button("cg_gallery06")
    g.image("image6")
    g.unlock("image6")

    g.button("cg_gallery07")
    g.image("image7")
    g.unlock("image7")

    g.button("cg_gallery08")
    g.image("image8")
    g.unlock("image8")

    g.button("cg_gallery09")
    g.image("image9")
    g.unlock("image9")

    g.button("cg_gallery10")
    g.image("image10")
    g.unlock("image10")

    g.button("cg_gallery11")
    g.image("image11")
    g.unlock("image11")

    g.button("cg_gallery12")
    g.image("image12")
    g.unlock("image12")

    g.button("cg_gallery13")
    g.image("image13")
    g.unlock("image13")

    g.button("cg_gallery14")
    g.image("image14")
    g.unlock("image14")

    g.button("cg_gallery15")
    g.image("image15")
    g.unlock("image15")

    g.button("cg_gallery16")
    g.image("image16")
    g.unlock("image16")

    g.button("cg_gallery17")
    g.image("image17")
    g.unlock("image17")

    g.button("cg_gallery18")
    g.image("image18")
    g.unlock("image18")

    g.locked_button=("images/gallery/thumbnail_locked.png")

default awards=[
    ["Первая концовка","Достигнуть своей первой концовки","persistent.ending1==True"],
    ["Еще что-то","Автор гений","persistent.ending2==True"],
    ["Что-то новое","Автог гений х2","persistent.ending3==True"]]


## Экран навигации экстра ###########################################################
screen exnavi():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        textbutton _("Изображения") action ShowMenu("image_gallery")
        textbutton _("Сцены") action ShowMenu("scene_gallery")
        textbutton _("Награды") action ShowMenu("awards_gallery")

## Музыкальный плеер в верхнем правом углу ########################################
screen mp3():
    frame:
        xalign 1.0
        hbox:
            spacing 5
            textbutton "ПРЕД" action mg.Previous()
            textbutton "ПУСК" action mg.Play()
            textbutton "СТОП" action mg.Stop()
            textbutton "СЛЕД" action mg.Next()
            frame:
                background None
                xsize 150
                $ titletrack=renpy.music.get_playing()
                if titletrack:
                    $ titletrack=titletrack[:len(titletrack)-4]
                    $ titletrack=titletrack.replace("_"," ")
                    $ titletrack=titletrack.title()
                    text "[titletrack]" xalign 0.5
                else:
                    null
## Экстра экран меню ############################################################
screen exgame_menu(scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        transclude
                else:
                    transclude

    use exnavi
    label "Extra"
    textbutton _("Return"):
        style "return_button"
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    use mp3

### Галерея изображений ##########################################
screen image_gallery():
    tag menu
    use exgame_menu(scroll="viewport"):
        grid 3 6:
            style_prefix "gslot"
            xalign 0.5
            yalign 0.5
            spacing gui.slot_spacing
            add g.make_button("cg_gallery01","images/gallery/thumbnail01.png")
            add g.make_button("cg_gallery02","images/gallery/thumbnail02.png")
            add g.make_button("cg_gallery03","images/gallery/thumbnail03.png")
            add g.make_button("cg_gallery04","images/gallery/thumbnail04.png")
            add g.make_button("cg_gallery05","images/gallery/thumbnail05.png")
            add g.make_button("cg_gallery06","images/gallery/thumbnail06.png")
            add g.make_button("cg_gallery07","images/gallery/thumbnail07.png")
            add g.make_button("cg_gallery08","images/gallery/thumbnail08.png")
            add g.make_button("cg_gallery09","images/gallery/thumbnail09.png")
            add g.make_button("cg_gallery10","images/gallery/thumbnail10.png")
            add g.make_button("cg_gallery11","images/gallery/thumbnail11.png")
            add g.make_button("cg_gallery12","images/gallery/thumbnail12.png")
            add g.make_button("cg_gallery13","images/gallery/thumbnail13.png")
            add g.make_button("cg_gallery14","images/gallery/thumbnail14.png")
            add g.make_button("cg_gallery15","images/gallery/thumbnail15.png")
            add g.make_button("cg_gallery16","images/gallery/thumbnail16.png")
            add g.make_button("cg_gallery17","images/gallery/thumbnail17.png")
            add g.make_button("cg_gallery18","images/gallery/thumbnail18.png")
style gslot:
    xsize 256
    ysize 144
### Галерея сцен ##########################################
screen scene_gallery():
    tag menu
    use exgame_menu(scroll="viewport"):
        grid 3 3:
            style_prefix "gslot"
            xalign 0.5
            yalign 0.5
            spacing gui.slot_spacing
            ## scene 1
            if renpy.seen_label("scene1"):
                imagebutton idle "images/gallery/scene1.png" action Replay("scene1")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 2
            if renpy.seen_label("scene2"):
                imagebutton idle "images/gallery/scene2.png" action Replay("scene2")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 3
            if renpy.seen_label("scene3"):
                imagebutton idle "images/gallery/scene3.png" action Replay("scene3")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 4
            if renpy.seen_label("scene4"):
                imagebutton idle "images/gallery/scene4.png" action Replay("scene4")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 5
            if renpy.seen_label("scene5"):
                imagebutton idle "images/gallery/scene5.png" action Replay("scene5")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 6
            if renpy.seen_label("scene6"):
                imagebutton idle "images/gallery/scene6.png" action Replay("scene6")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 7
            if renpy.seen_label("scene7"):
                imagebutton idle "images/gallery/scene7.png" action Replay("scene7")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 7
            if renpy.seen_label("scene8"):
                imagebutton idle "images/gallery/scene8.png" action Replay("scene8")
            else:
                add "images/gallery/thumbnail_locked.png"

            ## scene 9
            # Так как 9 нет, то null чтоб не сломалась таблица
            null
### Галерея наград ###########################################
screen awards_gallery():
    tag menu
    use exgame_menu(scroll="viewport"):
        vbox:
            spacing gui.slot_spacing
            for i in range(len(awards)):
                $ verify=awards[i][2]
                $ eltitle=awards[i][0]
                $ eldesc=awards[i][1]
                frame:
                    yfill False
                    xfill True
                    padding (10,10,10,10)
                    has hbox
                    spacing gui.slot_spacing
                    if eval(verify)==True:
                        frame:
                            background None
                            xsize 100
                            text "!!!"
                        frame:
                            background None
                            xsize 200
                            text "[eltitle]" color gui.accent_color
                        text "[eldesc]" color gui.text_color yalign 0.5 size 22
                    else:
                        frame:
                            background None
                            xsize 100
                            null
                        frame:
                            background None
                            xsize 200
                            text "[eltitle]" color "#666"
                        text "[eldesc]" color "#999" yalign 0.5 size 22
