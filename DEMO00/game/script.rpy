# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define p = Character("Player")
define mq = Character("马奇", color="#fbd145")
define yz = Character("盐之", color="#f42727")
define jc = Character("简诚", color="#c9f0f7")
define ms = Character("毛莎", color="#3354c1")
define msu = Character("毛笋", color="#e82b73")
define qy = Character("千叶", color="#0ecce1")

# ===== image定义 =====
image qianye_body_koalcoat = "images/qianye/qianye_body_koalacoat.png"
image qianye_body_koalcoatred = "images/qianye/qianye_body_koalacoatred.png"

image qianye_face_normal = "images/qianye/qianye_face_default.png"
image qianye_face_displeasure = "images/qianye/cat.png"
image qianye_face_happy = "images/qianye/qianye_face_happy.png"
image qianye_face_confident = "images/qianye/qianye_face_confident.png"
image qianye_face_sad = "images/qianye/qianye_face_sad.png"
image qianye_face_speaking = "images/qianye/qianye_face_speaking.png"
image qianye_face_unhappy = "images/qianye/qianye_face_unhappy.png"
image qianye_face_quitenice = "images/qianye/qianye_face_quitenice.png"

# ❗你缺这个


layeredimage qianye:
    zoom 0.25

    group body:
        attribute koalcoat default
        attribute koalcoatred
     
    group face:

        attribute normal default:
            "qianye_face_normal"

        attribute displeasure:
            "qianye_face_displeasure"

        attribute happy:
            "qianye_face_happy"

        attribute confident:
            "qianye_face_confident"
        attribute sad:
            "qianye_face_sad"   
        attribute speaking:
            "qianye_face_speaking"
        attribute unhappy:
            "qianye_face_unhappy"
        attribute quitenice:
            "qianye_face_quitenice"

#blinking animation for qianye's neutral face
image qianye_face_normal_anim:

    "qianye_face_normal"
    pause renpy.random.uniform(3.0, 6.0)  # 更自然一点

    "qianye_face_closed"
    pause 0.1

    repeat

label test_qianye_full:

    scene black

    # ===== 初始 =====
    show qianye koalcoat
    qy "默认状态9（koalcoat + normal + 眨眼）。"

    # ===== 表情测试（默认衣服）=====
    show qianye koalcoat normal
    qy "normal。"

    show qianye koalcoat happy
    qy "happy。"

    show qianye koalcoat sad
    qy "sad。"

    show qianye koalcoat confident
    qy "confident。"

    show qianye koalcoat displeasure
    qy "displeasure。"

    show qianye koalcoat unhappy
    qy  "unhappy。"

    show qianye koalcoat quitenice
    qy "quitenice。"

    show qianye koalcoat speaking
    qy "speaking（测试嘴型）。"
    qy "连续说几句看看自然不自然。"

    # ===== 换衣服测试 =====
    show qianye koalcoatred normal
    qy "红外套 + normal。"

    show qianye koalcoatred happy
    qy "红外套 + happy。"

    show qianye koalcoatred sad
    qy "红外套 + sad。"

    show qianye koalcoatred confident
    qy "红外套 + confident。"

    # ===== 快速切换测试（看有没有闪烁）=====
    show qianye koalcoat normal
    qy "切回默认衣服。"

    show qianye happy
    show qianye sad
    show qianye displeasure
    show qianye confident
    show qianye unhappy
    show qianye quitenice

    qy "快速切换结束。"

    # ===== 眨眼观察 =====
    show qianye normal
    qy "现在停一会，观察眨眼。"
    pause 5.0

    # ===== speaking连续测试 =====
    show qianye speaking
    qy "说话测试1。"
    qy "说话测试2。"
    qy "说话测试3。"

    show qianye normal
    qy "恢复 normal。"

    return            

image park = "images/park.jpg"
image office ="images/openning/temp_office.png"
image subway ="images/openning/temp_subway.png"
image toilet ="images/openning/temp_toilet.png"
image layoff = "images/openning/temp_layoff.png"
image map = "images/openning/temp_map.png"



#image qianye = "images/temp_qianye.png"

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
    #scene bg_parallax

    scene bg_back
    show bg_mid
    show bg_front
    "测试空间感"
    scene bulletin_board
    "测试公告栏"
    label bulletin_boardtest:
        call screen bulletin_boardtest
    label white:
        "一张招募贝斯手的告示。"
        "看来这支乐队缺人很久了。"
        jump bulletin_boardtest
    label yellow:
        "Open Mic Night 报名名单。"
        "很多名字都被划掉了。"
        "似乎竞争很激烈。"
        jump bulletin_boardtest
    label brown:
        "The Cosmic Drifters。"
        "已经解散的地下乐队。"
        "但似乎有人还在怀念他们。"
        jump bulletin_boardtest
    #call work
    #call layoff
    #call train
    #call test_qianye_full
    #call train_station

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


init python:

    class ParallaxDisplayable(renpy.Displayable):

        def __init__(self, child, depth=20.0, speed=0.1, **kwargs):
            super(ParallaxDisplayable, self).__init__(**kwargs)

            self.child = renpy.displayable(child)

            # 当前偏移
            self.x = 0.0
            self.y = 0.0

            # 目标偏移
            self.tx = 0.0
            self.ty = 0.0

            self.depth = depth
            self.speed = speed


        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            # === 获取鼠标位置（关键修复点）===
            mx, my = renpy.get_mouse_pos()

            # 屏幕中心
            cx = width / 2
            cy = height / 2

            # 转换为偏移
            dx = (mx - cx) / self.depth
            dy = (my - cy) / self.depth

            # 目标位置（反向）
            self.tx = -dx
            self.ty = -dy

            # === 缓动 ===
            self.x += (self.tx - self.x) * self.speed
            self.y += (self.ty - self.y) * self.speed

            # === 渲染子图 ===
            cr = renpy.render(self.child, width, height, st, at)
            rv.blit(cr, (self.x, self.y))

            # 持续刷新
            renpy.redraw(self, 0)

            return rv
#image bg_parallax = ParallaxDisplayable("bg.png", depth=30)
    #scene bg_back
    #show bg_mid
    #show bg_front
image bg_back  = ParallaxDisplayable("back.png", depth=60)
image bg_mid   = ParallaxDisplayable("mid.png", depth=35)
image bg_front = ParallaxDisplayable("face.png", depth=20)

#可交互公告栏代码
screen bulletin_boardtest:
    add "bulletin_board.png"
    modal True

    imagebutton auto "yellowp_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "yellowTemperature control")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("yellow")

    imagebutton auto "whitep_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "white Temperature control")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("white")
    
    imagebutton auto "brownp_%s.png":
        focus_mask True
        hovered SetVariable("screen_tooltip", "brownTemperature control")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("brown")




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
