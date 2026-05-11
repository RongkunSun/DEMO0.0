# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define p = Character("Player")
define mq = Character("马奇", color="#e3b008")
define yz = Character("盐之", color="#f42727")
define jc = Character("简诚", color="#c9f0f7")
define ms = Character("毛莎", color="#3354c1")
define msu = Character("毛笋", color="#e82b73")
define qy = Character("千叶", color="#fd8426")

# =====character image定义 =====
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

image yan_body_redcoat = "images/yanzhi/yan_body_redcoat.png"

image yan_face_normal = "images/yanzhi/yan_face_normal.png"
image yan_face_smile = "images/yanzhi/yan_face_smile.png"
image yan_face_speak = "images/yanzhi/yan_face_speak.png"
image yan_face_awkward = "images/yanzhi/yan_face_awkward.png"
image yan_anime_blink = "images/yanzhi/yan_anime_blink.png"

# ===== layeredimage定义 =====
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
layeredimage yan:
    #zoom 0.25

    group body:
        attribute redcoat default
        #attribute koalcoatred
     
    group face:

        attribute normal default:
            "yan_face_normal"

        attribute awkward:
            "yan_face_awkward"

        attribute smile:
            "yan_face_smile"

        attribute speak:
            "yan_face_speak"
        
#===== bgimage定义 =====
image park = "images/park.jpg"
image office ="images/openning/temp_office.png"
image subway ="images/openning/temp_subway.png"
image toilet ="images/openning/temp_toilet.png"
image layoff = "images/openning/temp_layoff.png"
image map = "images/openning/temp_map.png"
image trainstation = im.Scale("images/openning/temp_trainstation.jpg", 1920, 1080)


#blinking animation for qianye's neutral face
image qianye_face_normal_anim:

    "qianye_face_normal"
    pause renpy.random.uniform(3.0, 6.0)  # 更自然一点

    "qianye_face_closed"
    pause 0.1

    repeat


#开场演出
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
        #jump bulletin_boardtest
    call train_station_intro
    call zubizubi_route
    

    #call work
    #call layoff
    #call train
    #call test_qianye_full
    #call train_station

    return

label train_station_intro:

    scene bg_train_station

    "？？？：这家伙看起来和之前......好像也没什么变化嘛？"
    "？？？：不是都说上过班的人，会看起来不一样吗？"

    p "！！"

    show qianye koalcoat happy at center

    p "千叶！！！"

    show qianye koalcoat speaking

    qy "还以为你戴着耳机，得过一会儿才注意到我呢。"

    p "你很显眼好嘛。"

    show qianye koalcoat quitenice

    qy "可能只是在你眼中如此吧。"

    p "谢谢你，千叶，有你来接我真好。"

    show qianye koalcoat happy

    qy "乐意之至，正好今天餐厅也没什么事，我顺便出来放松放松。"

    p "说到餐厅......生意应该一如既往的好吧。"

    show qianye koalcoat confident

    qy "没错呢。"

    show qianye koalcoat speaking

    qy "哦？这个随身听你居然还用着呢。"

    p "可能因为习惯了，所以就一直用到现在了。"

    show qianye koalcoat quitenice

    qy "也不知道现在这东西算复古还是时髦了。"

    p "嗯……确实不太好说。"

    show qianye koalcoat happy

    qy "走吧，先帮你把这些行李送回家。"

    p "嗯！"

    scene bg_player_home

    show qianye koalcoat speaking at center

    qy "啊！终于摆脱了这些沉甸甸的家伙。"

    show qianye koalcoat happy

    "（千叶伸了个懒腰）"

    qy "真是难得的闲暇啊！"

    show qianye koalcoat quitenice

    qy "接下来打算做点什么吗？"

    menu:

        "就加入你的餐厅事业吧!":

            show qianye koalcoat happy

            qy "哈哈你想哪儿去了，我说的是今天的安排啦。"

            show qianye koalcoat confident

            qy "既然你还没什么头绪，那我们今天就去做点“复古又时髦”的事情吧。"

            p "诶，要去干什么啊？"

            jump zubizubi_route

        "其实我有点饿了。":

            show qianye koalcoat happy

            qy "看来即使今天休息，我也得在餐厅多待一会儿了。"

            scene bg_koalaok_restaurant

            "考拉OK餐厅，也就是千叶家的餐厅......好像初中毕业后就没来过了。"

            show qianye koalcoat happy at center

            qy "久等了。这些都是还没正式进入菜单的新品哦。"

            show qianye koalcoat confident

            qy "恐怕也只有我请客，才有机会让“客人”提前吃到了。"

            p "看起来都很有秋天的风味呢。"

            show qianye koalcoat happy

            qy "嘿嘿，不过餐厅里的音乐还是夏天的感觉。"

            show qianye koalcoat quitenice

            qy "对了，给我讲讲你之前的上班生活吧.....讲给我这个没上过班的听听。"

            p "虽然没上过班，但每天都作为“餐厅继承人”工作得很努力呢。"

            show qianye koalcoat speaking

            qy "低调、低调。毕竟按奶奶的说法，我现在还在“见习”阶段。"

            p "上班的话......嗯......该怎么形容呢?"
            p "回想起来，其实有点像每天都在过同一天。"

            show qianye koalcoat unhappy

            qy "听起来怎么有点惨。"

            show qianye koalcoat quitenice

            qy "不过，总该有点收获吧？"

            p "……"
            p "……钱倒是有攒下一些。"

            qy "那这次回来，你打算停留多久？"

            p "如果按存款倒推的话，一年应该都没有关系。毕竟回来住，就不用考虑房租了。"

            show qianye koalcoat happy

            qy "听起来不错呢。既然钱和时间都有了，肚子现在应该也填饱。我们就出发去下一个地方吧！"

            p "诶，要去哪里啊？"

            jump zubizubi_route

        "…….完全没想好。":

            show qianye koalcoat confident

            qy "既然这样，那就交给我了。"

            qy "今天就去做点“复古又时髦”的事情吧。"

            p "诶，要去做什么啊？"

            jump zubizubi_route


label zubizubi_route:

    scene bg_street

    "千叶家在临春开了一家叫“考拉OK”的音乐餐厅。"
    "去过的人，基本都会对它印象深刻。"

    "毕竟从各个方面来说，它都算得上“极具特色”。"

    "（卡拉逐渐侵略整个画面）"

    "不过......我和千叶现在好像不在去往餐厅的方向。真不知道千叶要把我们带到哪里去......"

    scene bg_zubizubi_outside

    "【背景图之后切换】"

    show qianye koalcoat happy at center

    qy "啊，已经能看到招牌了，前面就是了！"

    "我顺着千叶手指着的方向看去。"

    p "Zu……bi……Zubizubi？！"
    p "它不是初三的时候就倒闭了吗？"

    show qianye koalcoat quitenice

    qy "对啊，没想到已经复活后又开了这么久了。在你搬走之后。"

    "Zubizubi……嗯……该怎么形容它呢？"
    "它好像什么关于音乐的都会卖......以前放学后，经常会和朋友一起来。"

    p "Zubizubi音乐杂货铺。"

    scene bg_zubizubi_logo

    "通常来这里是为了打发时间，顺带听听音乐，和店员聊聊天；有时情况也会反过来。"

    scene bg_zubizubi_outside

    show qianye koalcoat confident at center

    qy "你继续回想吧，我要先走一步了。待在店里可比“呆”在外面有趣多了。"

    p "等等我！"

    scene bg_cdshop

    "进店，熟悉又陌生的感觉扑面而来。"

    p "店里的货品怎么感觉比以前多了好几倍。"

    show qianye koalcoat happy at left

    qy "没错，更像“洞穴”了。"

    "接着，我注意到一位很酷的小姐杵在收银台后。"
    "台面上散落着一些泡泡糖纸。"

    "这家伙为了吹出更大的泡泡……到底一次嚼了多少块？"

    "【解锁成就：泡泡糖纸】"

    "她手里拿着一本漫画书，正聚精会神地翻阅着，似乎忽略了我们的光顾。"

    show qianye koalcoat speaking

    qy "马奇，你在看什么啊——"

    "那位小姐的视线一下子从漫画上移了上来，露出了狡黠的笑容。"

    show mq_normal at right

    mq "千叶！我说怎么声音有些耳熟，原来是你来啦！"

    "原来千叶和这位似乎是叫马奇的小姐认识啊。"

    mq "好久没有见到你了。我还打算餐厅出新菜单的时候去找你玩呢！"

    mq "不过乐队的聚餐也临近了，很快我就又能吃上考拉ok了。很多人、很多很多菜，嘻嘻嘻嘻......"

    show qianye koalcoat happy

    qy "欢迎你随时光临。"

    mq "哦，你还带了新朋友来？"

    mq "我叫马奇，这个店我可熟悉啦，你等等，我去帮你把店员叫过来！"

    mq "喂——来客人啦！！！"

    "原来她不是这里的店员啊......"

    "???：欢迎光临，请稍等一下。我正在理货，马上就过来——"

    p "你好，我叫player。是千叶以前的同学，今天刚搬回临春。"

    mq "那真是太巧了，竟然还是千叶的老朋友啊！"

    mq "......你“搬回来”了的话......意味着......说不定，以后我们会经常见面啦！"

    mq "我平时是敲鼓的，没准儿下次你还能看到我在舞台上演出呢？"

    mq "不过，你平时会去看live吗？"

    p "live house演出嘛......其实还一次都没去过。"

    mq "噢？那要不......"

    show yan redcoat normal at center

    "???：马小姐——一会儿没盯着你就吃了这么多？"
    "???：都说了，这是给来店的客人准备的。"
    "???：快把收银台让出来，你这位游手好闲的“常驻顾客”。"

    show qianye koalcoat happy

    qy "今天有你的排班啊，盐之。"

    p "——“盐之”？"
    p "......盐......"

    "糟糕，反应过来时我已经和盐之的目光对上了。"

    "【久别重逢】"

    show yan redcoat awkward

    yz "......"
    yz "......好久不见。"

    show yan redcoat speak

    yz "原来你......还会回来啊。"

    p "......"

    menu:

        "好久不见。":

            show yan redcoat normal

            p "好久不见。"

            "（盐之的表情没有喜悦的一瞬间，反而趋于平静了）"

            "盐之的头发......留得这么长了。"

        "你头发变长了。":

            p "你头发变长了。"

            show yan redcoat awkward

            "（盐之从一瞬间惊讶/喜悦快速变为傲娇/掩饰）"

            show yan redcoat speak

            yz "你也变了很多。"

        "长头发很适合你。":

            p "长头发很适合你。"

            show yan redcoat awkward

            yz "怎么上来就说这种话。"

            "（盐之：气急败坏！“你怎么突然讲这种。”）"

    mq "等等？？？怎么感觉我好像错过了很多？"

    show yan redcoat normal

    yz "毕竟算是从小一起长大的......甚至比千叶认识的更早。"

    mq "啊？？？"

    mq "所以......你跟千叶认识......千叶跟player认识，而player你和也早就认识了！"

    mq "搞了半天，原来只有我是新角色？！"

    mq "不行，那我就要和大家创造新的共同回忆！"

    show qianye koalcoat happy

    qy "一如既往的很有干劲呢。"

    mq "虽然刚才被盐之那家伙打断了，但是——铛铛！"

    mq "我手里可掌握着这两张硬通货哦。"

    p "手里拿着两张.....门票一样的东西？"

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
