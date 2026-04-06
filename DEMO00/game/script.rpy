# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("Player")

label splashscreen:
    scene black

    # 第一行
    show text "制作" as line1:
        xalign 0.2
        yalign 0.2
        alpha 0.0
        zoom 0.0
        linear 2.0 alpha 1.0 zoom 3
        pause 1.5
        linear 0.5 alpha 0.0

    # 第二行
    show text "饼干车间" as line2:
        xalign 0.2
        yalign 0.4
        alpha 0.0
        zoom 0.0
        pause 2.5
        linear 2.5 alpha 1.0 zoom 3.5
        pause 1.0
        linear 0.5 alpha 0.0

    # 播放视频（10秒）
    #scene black  # 清屏
    #play movie "video.mp4" loop False
    #pause 10
    #stop movie

    pause 7

    play music "audio/main_menu1.mp3" fadein 1.0 noloop
    #中文游戏标题
    show text "迷恋下一拍" as line3:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        zoom 0.0
        linear 2.5 alpha 1.0 zoom 6
        pause 1.0
        linear 0.5 alpha 0.0
    
    
    # 英文游戏标题
    #show text "love next note" as line3_en:
        #xalign 0.5
        #yalign 0.55   # 稍微偏下
        #alpha 0.0
        #zoom 0.0
        #pause 7
        #linear 2.5 alpha 1.0 zoom 4   # 可以略小于中文
        #pause 1.0
        #linear 0.5 alpha 0.0
        
    pause 2
    stop music fadeout 2.0
    pause 3
    
    
    return

# 游戏在此开始。
init python:

    # Step 1. Create the gallery object.
    g = Gallery( )

#label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    #scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    #show eileen happy

    # 此处显示各行对话。

    #e "您已创建一个新的 Ren'Py 游戏。"

    #e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    #return
