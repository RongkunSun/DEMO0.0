# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define p = Character("Player")
define mq = Character("马奇", color="#fbd145")
define yz = Character("盐之", color="#f42727")
define jc = Character("简诚", color="#c9f0f7")
define ms = Character("毛莎", color="#3354c1")
define msu = Character("毛笋", color="#e82b73")
define qy = Character("千叶", color="#0ecce1")



image park = "images/park.jpg"
image office ="images/openning/temp_office.png"
image subway ="images/openning/temp_subway.png"
image toilet ="images/openning/temp_toilet.png"
image layoff = "images/openning/temp_layoff.png"
image map = "images/openning/temp_map.png"

image qianye = "images/temp_qianye.png"

image trainstation = im.Scale("images/openning/temp_trainstation.jpg", 1920, 1080)



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
    g.button("test1")
    g.image("temp_bg_park1.png") 
    g.button("test2")
    g.image("temp_bg_park2.png") 
   
screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "wip_bg.png"

    # A grid of buttons.
    grid 3 3:

        xfill True
        yfill True
        add g.make_button("test1", "temp_bg_park01.png", xalign=0.5, yalign=0.5)
        add g.make_button("test2", "temp_bg_park02.png", xalign=0.5, yalign=0.5)

    textbutton "Return" action Return()

# 全局台词属性溶解效果
#define config.say_attribute_transition = Dissolve(0.5)

# 开场ppt

label start:
    call work
    call layoff
    call train
    call train_station

    return

label work:
    scene office
    pause 2.0
    scene subway
    pause 2.0
    scene toilet
    pause 2.0
    scene office
    pause 1.0
    scene subway
    pause 1.0
    scene toilet
    pause 1.0
    scene office
    pause 0.5
    scene subway
    pause 0.5
    scene toilet
    pause 0.5
    return
label layoff:
    scene black
    pause 0.5

    show layoff:
        alpha 0.0
        pause 1.5
        alpha 1.0

    "“明天不用来了！”"

    return

label train:
    scene  map
        #play sound "audio/train.ogg"
    "之后就是连夜收拾行李，坐上了回老家的火车。"
    "详细的经过来不及解释了，先下车吧。"
    #stop sound fadeout 1.0

    return
label train_station:
    scene trainstation

    scene station

    show qianye

    "？？？" "上班生活过得怎么样啊？"
    p "千叶！！！有你来接我真好！"


    qy "那当然啦。正好今天餐厅没什么事，我也出来放松放松。"

    p "上班的话……每天都像在过同一天。"

    qy "听起来怎么有点惨。"
    qy "不过，总该有点收获吧？"

    p "……"
    p "……钱倒是有攒下一些。"

    qy "真是难得的闲暇啊！既然钱和时间都有了，接下来打算做点什么吗？"

    menu:
        "你打算做什么？"

        "就加入你的餐厅事业吧":
            qy "哈哈你想哪儿去了，我说的是今天的安排啦。"
            jump after_choice

        "有点饿了":
            qy "看来即使今天休息，我有段餐厅也得在餐厅里度过啦。"
            jump after_choice

        "完全没想好":
            qy "我知道我们今天可以去干什么啦。"
            jump after_choice
    return

label after_choice:

    # 后续剧情继续写这里


    return



  

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
