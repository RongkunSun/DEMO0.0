# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
#define p = Character("Player")
define p = Character("[pname]", color="#ffffff")
define mq = Character("马奇", color="#e3b008")
define yz = Character("盐之", color="#f42727")
define jc = Character("简诚", color="#90b6bd")
define ms = Character("毛莎", color="#3354c1")
define msu = Character("毛笋", color="#e82b73")
define qy = Character("千叶", color="#fd8426")

# =====character image定义 =====
#千叶
image qy_body_koalcoat = "images/qianye/qianye_body_koalacoat.png"
image qy_body_koalcoatred = "images/qianye/qianye_body_koalacoatred.png"

image qy_face_normal = "images/qianye/qianye_face_default.png"
image qy_face_displeasure = "images/qianye/cat.png"
image qy_face_happy = "images/qianye/qianye_face_happy.png"
image qy_face_confident = "images/qianye/qianye_face_confident.png"
image qy_face_sad = "images/qianye/qianye_face_sad.png"
image qy_face_speaking = "images/qianye/qianye_face_speaking.png"
image qy_face_unhappy = "images/qianye/qianye_face_unhappy.png"
image qy_face_quitenice = "images/qianye/qianye_face_quitenice.png"
#529新增
image qy_face_norl1 = "images/qianye/qy_face_nor11.png"
image qy_face_norl2 = "images/qianye/qy_face_nor12.png"
image qy_face_posl1 = "images/qianye/qy_face_pos11.png"
image qy_face_posl2 = "images/qianye/qy_face_pos12.png"
image qy_face_posl3 = "images/qianye/qy_face_pos13.png"
image qy_face_posl4 = "images/qianye/qy_face_pos14.png"
image qy_face_wowl1 = "images/qianye/qy_face_wow11.png"
image qy_face_emml1 = "images/qianye/qy_face_emm12.png"
image qy_face_emml2 = "images/qianye/qy_face_emm12.png"
#盐之
image yz_body_redcoat = "images/yanzhi/yan_body_redcoat.png"
image yz_face_normal = "images/yanzhi/yan_face_normal.png"
image yz_face_smile = "images/yanzhi/yan_face_smile.png"
image yz_face_speak = "images/yanzhi/yan_face_speak.png"
image yz_face_awkward = "images/yanzhi/yan_face_awkward.png"
image yz_anime_blink = "images/yanzhi/yan_anime_blink.png"
#马奇
image mq= "images/mq.png"

# ===== layeredimage定义 =====
layeredimage qy:
    #zoom 0.25

    group body:
        attribute koalcoat default
        attribute koalcoatred
     
    group face:

        attribute normal default:
            "qy_face_normal"

        attribute displeasure:
            "qy_face_displeasure"

        attribute happy:
            "qy_face_happy"

        attribute confident:
            "qy_face_confident"
        attribute sad:
            "qy_face_sad"   
        attribute speaking:
            "qy_face_speaking"
        attribute unhappy:
            "qy_face_unhappy"
        attribute quitenice:
            "qy_face_quitenice"
        #529新增
        attribute norl1:
            "qy_face_norl1"
        attribute norl2:
            "qy_face_norl2"

        attribute posl1:
            "qy_face_posl1"
        attribute posl2:
            "qy_face_posl2"
        attribute posl3:
            "qy_face_posl3"
        attribute posl4:
            "qy_face_posl4"
            
        attribute wowl1:
            "qy_face_wowl1"

        attribute emml1:
            "qy_face_emml1"
        attribute emml2:
            "qy_face_emml2"
        
            
layeredimage yz:
    #zoom 0.25

    group body:
        attribute redcoat default
        #attribute koalcoatred
     
    group face:

        attribute normal default:
            "yz_face_normal"

        attribute awkward:
            "yz_face_awkward"

        attribute smile:
            "yz_face_smile"

        attribute speak:
            "yz_face_speak"
        
#===== bgimage定义 =====
image park = "images/park.jpg"
image office ="images/openning/temp_office.png"
image subway ="images/openning/temp_subway.png"
image toilet ="images/openning/temp_toilet.png"
image layoff = "images/openning/temp_layoff.png"
image map = "images/openning/temp_map.png"
image trainstation = im.Scale("images/openning/temp_trainstation.jpg", 1920, 1080)


#blinking animation for qianye's neutral face
image qy_face_normal_anim:

    "qy_face_normal"
    pause renpy.random.uniform(3.0, 6.0)  # 更自然一点

    "qy_face_closed"
    pause 0.1

    repeat

#立绘翻转参数
transform flip:
    xzoom -1

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
#剧情测试模块

label start:
    #scene bg_parallax
    
    call work from _call_work
    $pname = renpy.input("在这里签上你的名字：", length=10, default="玩家")
    $pname = pname.strip()  # 去除输入的前后空格
    if pname == "":
        $pname = "Player"

    call layoff from _call_layoff
    call train from _call_train
    call b_board from _call_b_board
    call zubizubi_intro from _call_zubizubi_intro
    
    

    #call work
    #call layoff
    #call train
    #call test_qianye_full
    #call train_station

    return

label zubizubi_intro:
    show qy posl1
    "？？？：这家伙看起来和之前......好像也没什么变化嘛？"
    "？？？：不是都说上过班的人，会看起来不一样吗？"

    p "！！"
    p "千叶！！！"

    show qy posl3

    qy "还以为你戴着耳机，得过一会儿才注意到我呢。"
    p "你很显眼好嘛。"
    qy "可能只是在你眼中如此吧。"
    show qy posl2
    p "谢谢你，千叶，有你来接我真好。"
    qy "乐意之至，正好今天餐厅也没什么事，我顺便出来放松放松。"
    show qy wowl1
    p "说到餐厅......生意应该一如既往的好吧。"
    qy "没错呢。"

    qy "哦？这个随身听你居然还用着呢。"
    p "可能因为习惯了，所以就一直用到现在了。"

    qy "也不知道现在这东西算复古还是时髦了。"
    p "嗯……确实不太好说。"

    qy "走吧，先帮你把这些行李送回家。"
    p "嗯！"

    hide qy posl4

    scene trainstation

    show qy confident

    qy "啊！终于摆脱了这些沉甸甸的家伙。"
    qy "(伸了个懒腰)"
    qy "真是难得的闲暇啊！"
    qy "接下来打算做点什么吗？"

    menu:
        "就加入你的餐厅事业吧!":
            jump choice1

        "其实我有点饿了。":
            jump choice2

        "……完全没想好。":
            jump choice3


label choice1:

    qy "哈哈你想哪儿去了，我说的是今天的安排啦。"
    qy "既然你还没什么头绪，那我们今天就去做点“复古又时髦”的事情吧。"
    p "诶, 要去干什么啊？"

    jump cont13


label choice2:

    qy "看来即使今天休息，我也得在餐厅多待一会儿了。"

    scene black with fade

    "千叶家的考拉OK餐厅......好像自从初中毕业后，我就没再来过了。"

    scene black with fade

    "【进店的开门音效专场，开始播放夏日餐厅bgm】"

    qy "久等了。这些都是还没进入菜单的新品哦，下个月才会正式上架。"
    qy "大部分还在研发阶段，最近几天应该还会做一些口味上的调整。"
    qy "大概只有我请客，才有机会让“客人”提前吃到了。"

    p "看起来都很有秋天的风味呢。"
    qy "忙活了好几周才敲定的，希望吃起来也是如此吧。"
    qy "唉——餐厅里倒是还放着夏天的音乐呢"

    qy "对了，给我讲讲你之前的上班生活吧.....讲给我这个没上过班的听听。"
    p "虽然没上过班，但每天都作为“餐厅继承人”工作得很努力呢。"

    qy "低调、低调。毕竟按奶奶的说法，我现在还在“见习”阶段。"

    p "上班的话......嗯......该怎么形容呢?"
    p "回想起来，其实有点像每天都在过同一天。"

    qy "听起来怎么有点惨。"
    qy "不过，总该有点收获吧？"

    p "……"
    p "……钱倒是有攒下一些。"

    qy "那这次回来，你打算停留多久啊？"

    p "如果按存款倒推的话，一年应该都没有关系。毕竟回来住，就不用考虑房租了。"
    p "总之，暂时还不至于流落街头。"

    qy "听起来不错呢。既然钱和时间都有了，肚子现在应该也填饱。我们就出发去下一个地方吧！"
    p "诶, 要去哪里啊？"

    jump cont13


label choice3:

    qy "既然这样，那就交给我了。"
    qy "今天就去做点“复古又时髦”的事情吧！"
    p "诶, 要做什么啊？"

    jump cont13


label cont13:

    "千叶和我是初中同班同学，她家在临春经营着“考拉OK”的音乐餐厅。"
    "说起来，这家餐厅好像从我记事起就已经存在了。"
    "而去过的人，大概都会对它印象深刻。"
    "毕竟从各个方面来说，它都算得上“极具特色”。"
    "......不过我和千叶现在好像不在去往餐厅的方向。真不知道千叶要把我们带到哪里去......"

    scene black with fade

    "After 1、2、3"
    "【进店前】"

    qy "啊，已经能看到招牌了，前面就是了！"

    "我顺着千叶手指着的方向看去。"

    p "Zu……bi……Zubizubi？！"
    p "它不是初三的时候就倒闭了吗？"

    qy "是啊，没想到它后来复活了。而且一晃眼又开了这么久了。"
    qy "在你搬走后，确实还发生了不少事情呢......"

    "Zubizubi……嗯……该怎么形容它呢？"
    "印象里它好像什么关于音乐的“东西”都会卖......"
    "以前放学后，我也经常会和朋友一起来。"

    p "Zubizubi音乐杂货铺，好怀念啊。不过从外观看，它现在已经是新的样子了。"

    qy "你继续回想吧，我要先走一步了。待在店里可比“呆”在外面有趣多了。"
    p "等等我！"

    scene shop

    "进店，熟悉又陌生的感觉扑面而来。依旧是琳琅满目的cd、唱片和器材配件。"
    "角落里堆放的不是一捆一捆的音乐杂志，就是什么猜不出从哪儿来也猜不出怎么用的乐器。"

    p "货品......怎么感觉比以前多了好几倍?!"
    qy "没错，更像“洞穴”了。"
    "尽管店内的过道因为大小不一的货品很维持笔直流畅的线条，{p}
    但目之所及的物品比起盖着一层毛绒绒的灰尘，{p}
    反而干净的出奇，是有些表面还带着点反光的那种。"
    p "但意外打理的......很干净。"
    qy "这里的店员应该工作得很辛苦吧，毕竟要维护这么多商品。"
    

    qy "诶，你看！这里竟然有这个，感觉上次好像看舅舅摆弄过类似的东西。"

    "说着，千叶拿起那个摆在货架旁的细长圆筒，左右倾斜了一下。"
    "里面发出“哗啦哗啦”豆子滚过般的声音。"

    menu:
        "竟然会发出这种声音啊。":
            qy "很有意思吧。"
            qy "看外观绝对猜不到呢。"

        "原来是这么用的啊。":
            qy "嗯，上次舅舅怎么说得来着？"
            qy "好像是“......当地人用来祈雨的乐器”。"
            qy "不过家里那个现在应该已经在仓库吃灰了。"

    p "啊切！"
    qy "没事吧，难道说搬家太累，有点感冒了？"
    p "应该不是，但是周围好像有什么奇异的味道。"
    qy "可能是店里焚的香吧，昨天刚下过雨。"
    p "我怎么不记得店里以前有这种“特色”。"
    qy "可能是老板的新爱好吧。不过我也好一阵子没见到她了。"

    "接着，我注意到一位很酷的小姐杵在收银台后。"

    "这家伙为了吹出更大的泡泡……到底一次嚼了多少块？"
    "【解锁成就：泡泡糖纸】"

    "她手里拿着一本漫画书，正聚精会神地翻阅着，似乎忽略了我们的光顾。"

    qy "马奇，你在看什么呢？"

    "？？？：诶，千叶！我说怎么声音有些耳熟，原来是你啊！"

    "？？？：好久不见，我正打算餐厅出新菜品的时候去找你玩呢！"

    "？？？：嗯？不过，乐队的聚餐也临近了....."
    "？？？：到时候很多人，很多很多菜，嘻嘻嘻嘻......很快我就又能吃上考拉ok了。"

    qy "欢迎你随时光临。"

    "？？？：哦，你旁边怎么还多了一个新朋友？这位是......"

    menu:
        "你好，我叫[pname]，今天刚搬回临春。":
            jump intro1

        "你好，我叫[pname]，是千叶以前的同学。":
            jump intro2


label intro1:

    mq "诶？这么巧。今天折腾回来辛苦了吧？我叫马奇，今后我们也许会经常见面了。"

    p "好在有千叶的帮忙，最辛苦的部分很快就搞定了。"
    mq "——是啊，有千叶这样一位朋友真好啊。"

    qy "马奇，你都夸得我不好意思了。"

    menu:
        "所以，马奇是这里的店员？":
            mq "你猜？"
            mq "哈哈哈，不卖关子了。其实我也是来逛店的啦。"
            p "原来是这样啊。"

        "所以，马奇是这里的老板？":
            mq "你猜？"
            mq "哈哈哈，不卖关子了。其实我也是来逛店的啦。"
            p "原来是这样啊。"

    jump after_intro


label intro2:

    mq "真羡慕你们这种从小就认识的友谊。我叫马奇，算是这里的......常客吧？当然也是千叶家餐厅的忠实粉丝。不过千叶的朋友就是我的朋友，今天我们就算认识了。"

    p "嗯，马奇......可真是"

    menu:
        "很有热情、活力呢。":
            qy "她是个“自来熟”。"

        "有点自来熟呢。":
            qy "她一贯如此。"

    mq "嘿嘿，其实是“人来疯”啦。"

    jump after_intro


label after_intro:

    mq "对了，刚才我光顾着自报家门了。你们今天来店里，是想找点什么吗？"
    p "好像想不出什么具体的目标。"

    menu:
        "马奇有什么推荐的吗？":
            mq "哼哼，这你可就问对人啦！平时我可是在这里淘到过不少便宜好货。"
            qy "马奇似乎在这方面“嗅觉”意外灵敏呢。"
            mq "是“听”！人家是靠听的啦，再说有什么其它技巧的话......那就是“心”吧。没错！一颗“寻宝”的心。"

            mq "毕竟我平时好像也就靠这两样，不管是打鼓还是干别的什么。"
            "说着马奇低头看向收银台，用两根食指随意地在玻璃台边轻轻敲出了一小段节拍。"
            qy "哈哈，怎么感觉话题“嗖”的一下就跳到了打鼓呢。"
            mq "诶呀，一不小心就把话题扯远了。"
            p "所以......马奇小姐是因为打鼓，所以才会这样思考吗？"
            mq "嗯......这我倒没怎么想过呢？"
            mq "或许是这样吧。毕竟我也算是个不入流的职业鼓手。"

        "马奇对这里很熟悉吗？":
            mq "嘛，算是吧。"
            mq "毕竟我平时是打鼓的，经常会来这里掏点“经典片段”、“沧海遗珠”什么的。拿回去学习学习。"

            p "原来马奇小姐是鼓手吗？"
            mq "嗯，姑且算是不入流的职业鼓手吧。"

    menu:
        "听起来是很酷的职业":
            mq "不过，不是什么很稳定的工作。好处是可以经常去现场看演出。自己演，也听别人演。总之，在live house表演，最棒了！"
            qy "对马奇来说，打鼓好像不只是一份工作呢。"

        "听起来，是一份有点辛苦又掺杂着不稳定的工作呢":
            mq "哈哈，的确如此，不过在舞台上表演开始的那一刻——一切就都感觉不一样了。live表演最有意思了!"
            qy "马奇在舞台上的样子可是和平时很不一样呢。"

    menu:
        "马奇在舞台上......是什么样子呢？":
            mq "这个嘛，你看到就知道啦。现在暂时保密！"
            mq "哦，对啦！正好我手里还剩两张，你和千叶一人一张吧。"
            "马奇不知从哪里翻出两张彩色纸条“啪”的一下拍在了玻璃台面上。"
            mq "诶呦，刚才为了装酷没控制好力度，失误、失误。"
            mq "不过留在台面上的才是重点。"
            p "......这是？"

        "live表演、live house是什么？":
            mq "诶，你没有去过live house吗"
            p "确实对我来说是有些陌生的概念。平时听音乐基本上都是通过耳机。"

            "马奇开始低头在口袋里摸索起来，顺势掏出两张彩色纸条，“啪”的一下拍在了玻璃台面上——"
            mq "唔，那这个你一定要收下！！！千叶也有份。"
            p "......这是？"

    qy "哈哈，是马奇他们下次表演的门票，那我就不客气的收下了！"
    mq "呜呜，千叶，谢谢你的支持。"
    mq "呐，把这个首尾相粘一下，变成手坏，就可以带着它自由进出live house了。不过只可以在指定场次使用哦，比如说我所在的乐队登台表演的那一晚。"

    menu:
        "乐队？马奇的乐队吗？":
            mq "既然那么好奇，不如直接来现场看看呗？"
            p "好吧，看来只有去到现场才能知道了。"

        "我也要和千叶一起去！":
            mq "一言为定哦！到时候在台下看不到可爱的你们我会伤心的。"

    "？？？：刚才是什么动静？！我在库房都听到了，我以为你只是来安静的看会儿漫画的，马小姐——"
    "？？？：稍等一下，我马上就来——"

    mq "哦，对喽，今天我们乐队的另一个家伙碰巧也在。"

    "？？？：什么？来客人了你也不跟我讲一声？！还是我在这边伸着脖子才看到的......"

    mq "喉喔，原来今天不止马奇在，连盐之也在啊。"

    "——盐之？"
    p "......"

    menu:
        "看去":
            yz "嗯？你怎么会出现在这里。"
            yz "马奇和千叶看起来没问题啊，都和平时一个样，原来——"
            yz "你真的回来啦。"

        "眼神回避":
            yz "哦，是千叶啊，还有——"
            yz "一个完全没想到会出现在这里的家伙。"
            yz "我以为你不会回来了呢？"

    menu:
        "......":
            pass

        "确实好久没见了呢，盐之。":
            yz "嗯......嘛......也没有很久啦。也就六、七年？"
            mq "啊？六七年难道不是很久了吗？已经够我......呃，让我想一想——"
            qy "够考拉OK推出200多个新菜品了。"
            mq "哇，千叶你算得真快！"

    menu:
        "你头发变长了。":
            yz "嗯，反正现在也不会有什么中学的老古板揪着这点不放了。"
            yz "你也变了很多。"

        "长头发很适合你。":
            yz "怎么上来就说这种话。"
            yz "你怎么突然讲这种。"

    mq "等等，等等？？？怎么感觉我好像错过了一些剧情？！"
    mq "盐之和[pname]之间难道有什么我不知道的“过去”吗？"
    qy "是关于两人青梅竹马的部分啦。"
    p "......等等。千叶,你刚刚脱口而出了什么啊？！"
    mq "哦？！"
    yz "那都是过去的事了。"

    "......"
    "盐之那家伙怎么好像脸红了......."

    mq "啊？？？"
    mq "所以......你跟千叶认识......千叶跟[pname]认识，而你和[pname]居然也早就认识了！"
    mq "搞了半天，原来只有我是“新角色”？！"

    yz "时候不早了......马奇你不是还要去乐器行教课吗？"

    qy "好啦好啦，马奇，以后你总会知道的。现在，赶紧去上课吧。你也不想来让来上课的小朋友在教室苦苦等待吧。"

    mq "可是我八卦还没听够啊喂！！下次、下次, [pname]一定要讲给我听啊！！"

    "【切入店外隐约的午后蝉鸣与微风声】"
    "回到临春的第一天，似乎比想象中还要热闹得多。"

label after_date:

    "暂时到家"

    scene street_evening
    with fade

    "【场景背景切换：街道、店面之类的】"

    "和千叶逛着逛着，就已经接近傍晚了。"

    qy "那就下周live见了。"
    p "不过，在那之前，我们应该还会见面吧。"
    qy "说得也是，我有空的话，随时可以约！"
    p "嗯。"
    qy "那就拜拜喽，到时候手机联系。"

    "（立绘迷迷思）"

    scene home
    with fade

    "【场景背景切换：家门口，玄关，房间】"

    p "走了一天，终于可以躺下了。"

    "不过身体虽然累了，但感觉大脑好像还没有困意。毕竟白天发生了那么多事情。"

    menu:
        "就开始准备睡觉吧。":
            jump sleep_route

        "要不......再去公园走走？":
            jump park_route


label sleep_route:

    "简单收拾了一下，就钻到了被窝里。"

    return


label park_route:

    scene park

    p "这种时候，如果还能带上耳机，听着自己喜欢的歌曲，那就更爽了。"

    "掏出耳机，选好音乐，正准备戴上时——"

    "【“窸窸窣窣”的声音】"
    "“窸窸窣窣”——"
    "声音是从旁边的树丛传来的。"
    "“咔嚓”——像是什么树枝被踩断了。"
    "——大概是什么小动物弄出的声响吧。"
    "“唰唰唰”"
    "——像是有什么东西靠近了。"

    "下一秒，一个少女从树丛里钻了出来。"
    "她低头拍了拍身上的叶子和灰尘，像是什么都没发生过一样。"

    "？？？：……可恶，又跟丢了。"

    "很快，她注意到了我的目光。"

    "？？？：哈，被你看到了。"

    menu:

        "把目光移开":

            "？？？：”要不......就把你定为下一个目标吧？“"

            p "”......！“"

            "？？？：”放心，不会一上来就把你灭口的。“"

            p "”......！！“"

            "然后是漫长的几声蝉鸣，树叶被风吹得沙沙作响。"

            "还有她越来越近的脚步声。"

            "？？？：这个耳机应该已经是很多年前的东西了吧。"

            "诶？——"

            "她抬了抬下巴，指向我手里的耳机。"

            p "......我不太了解呢。只知道是很久以前买的了。"

            "？？？：虽然3年前再版过一次，不过果然原版的质感还是无法替代啊。"

            "现在周围的光线已经逐渐暗了下来，她居然还能......看得这么清楚？"

            "？？？：该回去了。"

            "？？？：知道了，毛莎。本来我也要往家走了"

            "？？？：那就下次再见了。"

            "少女冲我摆了摆手，转身和神秘男子向公园出口走去。"

            "？？？：哦，对了。"

            "突然, 她又退回几步，转头对我说。"

            "？？？：刚才只是没忍住捉弄了一下你。"

            "少女的脚步声远去了。"

            "啊——松了一口气。"

            "总觉得刚刚那两个人像同一种生物。"

            "之后，又独自坐了一会儿。"

            "回到家，简单收拾了一下，就进入了梦乡。"

            "回来后好好休息了一周，不知不觉就花了很多时间在读书、打游戏上。"


        "继续看着她":

            "我们对视了几秒。昏暗的光线下，她的皮肤却依然白得像会反光一样。"

            "接着，她的视线落到了我身上。"

            "难道我身上有什么奇怪的东西吗？"

            "她眯了眯眼睛，向我靠近了几步。"

            "？？？：这个耳机应该已经是很多年前的东西了吧。"

            "她抬了抬下巴，指向我手里的耳机。"

            p "......我不太了解呢。只知道是很久以前买的了。"

            "？？？：虽然3年前再版过一次，不过果然原版的质感还是无法替代啊。"

            "现在周围的光线已经逐渐暗了下来。她居然还能......看得这么清楚？"

            "？？？：该回去了。"

            "？？？：知道了，毛莎。本来我也要往家走了"

            "？？？：那就下次再见了。"

            "少女冲我摆了摆手，转身和神秘男子向公园出口走去。"

            "……"
            "……总觉得那两个人像同一种生物。"

            "之后，又独自坐了一会儿。"

            "回到家，简单收拾了一下，就进入了梦乡。"

            "”啊切，啊切！”"

            p "回来后好好休息了一周，不知不觉就花了很多时间在读书、打游戏上。"


label before_livehouse:

    "去livehouse前"

    "……不过，穿什么好呢？"

    menu:

        "酷酷的考拉OK文化衫":

            "好像是哪年在考拉OK吃饭获得的赠品。"
            "额，上面怎么还破了几个洞啊？！完全不记得是怎么搞的了。好在不影响穿着。"

        "中性风的鸭舌帽和乐队t恤":

            "t恤还是以前在Zubizubi买的。"
            "买的时候好像有点大了，所以没怎么穿过。现在穿......意外的很合身！"

        "崭新的短款机车夹克":

            "连吊牌都还没拆。"
            "当初脑子一热买了下来，结果一次都没穿出去过。……穿这个去看live，应该正合适吧。"

        "和平时穿的一样":

            "最后还是选了最习惯的那套搭配。"
            "虽然没什么特别的，但身体和心情都很轻松。"

    "都穿戴好了，感觉可以出发了！"
    "对了，还有这个“手环”。门票一定得带上。"

    "“滴滴”"
    "手机上浮现出千叶的信息：我快到了，一会儿门口见。"


label jiancheng_intro:

    "简诚登场"

    "？？？：”哈喽，千叶。好久不见（眯眼笑）"

    qy "好久不见。"

    "？？？：之前听马奇说，你今天会和朋友一起来。"

    "他的目光落到了我身上。"

    "？？？：这位就是马奇提到的那位“朋友”吧？"
    "？？？：请问怎么称呼你？"

    p "我叫[pname]，你好。"

    "？？？：幸会，叫我简诚就好。"

    menu:

        "你是怎么认识马奇的？":

            jc "哦，忘了自我介绍了，我是和马奇同乐队的键盘手。"

            jc "呐，手环上这里，就是我们乐队的名字。"

            "说着他指了指自己手腕上的手环。"

            "我这才发现，自己手上的那条和他戴的是同一款。"

            p "原来叫Kidsplay啊。"

            jc "点了点头（面带笑意）"
            jump maosha_intro



        "你是怎么认识千叶的？":

            jc "哈哈，千叶吗？大概是因为我们整个乐队都是她们家餐厅的忠实顾客。"

            "（简诚：都是因为某些家伙每次演出完都吵着闹着要吃，吃不到就不消停。【很快的自动播放】）"

            p "刚刚感觉有什么奇怪的话快速溜过了。"

            qy "考拉OK，算是Kidsplay的传统聚餐地吧。（大笑）"

            jc "有的时期餐厅生意异常火爆，我也会提前联系千叶，麻烦她提前预留位置。"

            jc "一来二去，好像就熟络起来了。"

            p "Kidsplay……"

            jc "嗯，我们乐队的名称是K-I-D-S-P-L-A-Y，Kidsplay。"

            jc "你带的手环上也应该也有写。"

            "说着他抬了抬手腕, 轻轻晃了晃手环。"

            "仔细一看，原来连颜色和印字都一样。"
            jump maosha_intro



label maosha_intro:

    "毛莎登场"

    "这时，有人从后面拍了拍简诚的肩膀，"

    "？？？：那两人迟到了，我们先去调试吧。"

    "语气平静得几乎没有起伏。"

    
    "——是昨天公园里那个人。"
   
    "他看向了我和千叶。"

    ms "你好，千叶。"

    qy "好久不见。"

    jc "等等，毛莎。"

    jc "这是[pname]，今天和千叶一起来的。"

    p "你好。"

    ms "你好。"

    jc "他叫毛莎，是我们乐队的贝斯手。"

    "毛莎微微点了点头，便没再开口。"

    "……有种不能随便搭话的气场。"
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



label b_board:
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
