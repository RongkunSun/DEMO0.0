# 游戏的脚本可置于此文件中。
#define config.main_menu_music = "audio/littlestar.mp3"


#开场演出
label splashscreen:
    scene black
    #if not renpy.music.is_playing():
        #play music "audio/littlestar.mp3" fadein 1.0
    # 第一行
    show text "制作" as line1:
        xalign 0.2
        yalign 0.2
        alpha 0.0
        zoom 0.0
        linear 2.0 alpha 1.0 zoom 2
        pause 1.5
        linear 0.5 alpha 0.0

    # 第二行
    show text "饼干车间" as line2:
        xalign 0.2
        yalign 0.4
        alpha 0.0
        zoom 0.0
        pause 2.5
        linear 2.5 alpha 1.0 zoom 2.5
        pause 1.0
        linear 0.5 alpha 0.0

    # 播放视频（10秒）
    #scene black  # 清屏
    #play movie "video.mp4" loop False
    #pause 10
    #stop movie

    pause 7

   
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
   
    pause 3
    
    
    return

#剧情分支控制变量
default outfit = ""
default visited_park1 = False
# 全局台词属性溶解效果
#define config.say_attribute_transition = Dissolve(0.5)

# 开场ppt
#剧情测试模块

label start:
    #scene bg_parallax
    stop music fadeout 0.7
    call work from _call_work
    $pname = renpy.input("在这里签上你的名字：", length=10)# ,default="玩家")
    $pname = pname.strip()  # 去除输入的前后空格
    if pname == "":
        $pname = "Player"

    call layoff from _call_layoff
    call train from _call_train
    #call b_board from _call_b_board
    call zubizubi_intro from _call_zubizubi_intro
    
    

    #call work
    #call layoff
    #call train
    #call test_qianye_full
    #call train_station

    return

label zubizubi_intro:
    
    scene ts

    #$ textbox_mode = "textbox_tense1"
    qy_unknown "这家伙看起来和之前......好像也没什么变化嘛？"
    qy_unknown "不是都说上过班的人，{w=0.5}会看起来不一样吗？"

    p "！！"
    p "千叶！！！"

    show qy posl1

    qy "还以为你戴着耳机，得过一会儿才注意到我呢。"
    p "你很显眼好嘛。"
    show qy emml2
    qy "可能只是在你眼中如此吧。"
    p "谢谢你，千叶，有你来接我真好。"
    show qy posl2
    qy "乐意之至，正好今天餐厅也没什么事，我顺便出来放松放松。"
    p "说到餐厅......生意应该一如既往的好吧。"
    show qy posl1
    qy "没错呢。"
    show qy wowl1
    qy "哦？这个随身听你居然还用着呢。"
    p "可能因为习惯了，所以就一直用到现在了。"

    qy "也不知道现在这东西算复古还是时髦了。"
    show qy wowl1
    p "嗯......确实不太好说。"
    show qy posl1
    qy "走吧，先帮你把这些行李送回家。"
    p "嗯！"

    hide qy posl4

    scene street_home2 with fade
    pause 0.3
    scene street_home1 with fade
    pause 0.3
    scene phome_livingroom with fade

    show qy posl4
    qy "啊！终于摆脱了这些沉甸甸的家伙。"
    hide qy
    qy "(伸了个懒腰)"
    show qy posl3
    qy "真是难得的闲暇啊！"
    show qy posl2
    qy "接下来打算做点什么吗？"

    menu:
        "就加入你的餐厅事业吧!":
            jump choice1

        "其实我有点饿了。":
            jump choice2

        "......完全没想好。":
            jump choice3

label choice1:

    show qy posl3
    qy "哈哈你想哪儿去了，我说的是今天的安排啦。"
    show qy emml2
    qy "既然你还没什么头绪，那我们今天就去做点“复古又时髦”的事情吧。"
    p "诶, 要去干什么啊？"
    hide qy

    jump cont13
label choice2:

    show qy emml2
    qy "看来即使今天休息，我也得在餐厅多待一会儿了。"
    hide qy
    
    scene street_home2 with fade
    pause 0.3
    scene coala_out with fade

    "千叶家的考拉OK餐厅......好像自从初中毕业后，我就没再来过了。"

    scene coala_in with fade

    #【进店的开门音效专场，开始播放夏日餐厅bgm】
    
    show qy emml2
    qy "久等了。这些都是还没进入菜单的新品哦，下个月才会正式上架。"
    show qy wowl1
    qy "大部分还在研发阶段，最近几天应该还会做一些口味上的调整。"
    show qy posl1
    qy "大概只有我请客，才有机会让“客人”提前吃到了。"

    p "看起来都很有秋天的风味呢。"
    show qy norl2
    qy "忙活了好几周才敲定的，希望吃起来也是如此吧。"
    show qy emml1
    qy "唉——餐厅里倒是还放着夏天的音乐呢"
    show qy posl2
    qy "对了，给我讲讲你之前的上班生活吧......讲给我这个没上过班的听听。"
    p "虽然没上过班，但每天都作为“餐厅继承人”工作得很努力呢。"
    show qy emml2
    qy "低调、低调。毕竟按奶奶的说法，我现在还在“见习”阶段。"

    p "上班的话......嗯......该怎么形容呢?"
    p "回想起来，其实有点像每天都在过同一天。"
    show qy wowl1
    qy "听起来怎么有点惨。"
    show qy posl1
    qy "不过，总该有点收获吧？"
    hide qy
    p "......"
    p "......钱倒是有攒下一些。"
    show qy posl1
    qy "那这次回来，你打算停留多久啊？"

    p "如果按存款倒推的话，一年应该都没有关系。毕竟回来住，就不用考虑房租了。"
    p "总之，暂时还不至于流落街头。"
    show qy posl3
    qy "听起来不错呢。既然钱和时间都有了，肚子现在应该也填饱。我们就出发去下一个地方吧！"
    p "诶, 要去哪里啊？"
    hide qy
    scene coala_out with fade
    jump outside_shop
label choice3:

    show qy posl3
    qy "既然这样，那就交给我了。"
    show qy posl2
    qy "今天就去做点“复古又时髦”的事情吧！"
    p "诶, 要做什么啊？"
    hide qy

    jump cont13

label cont13:

    scene street_home2 with fade
    pause 0.3
    scene coala_out with fade
    "千叶和我是初中同班同学，她家在临春经营着“考拉OK”的音乐餐厅。"
    "说起来，这家餐厅好像从我记事起就已经存在了。\n而去过的人，大概都会对它印象深刻。\n毕竟从各个方面来说，它都算得上“极具特色”。"#(考拉逐渐侵略整个画面）
    "......不过我和千叶现在好像不在去往餐厅的方向。真不知道千叶要把我们带到哪里去......"

label outside_shop:

    show qy wowl1
    qy "啊，已经能看到招牌了，前面就是了！"
    hide qy
    "我顺着千叶手指着的方向看去。"
    scene zubi_out with fade
    p "Zu......bi......Zubizubi？！"
    p "它不是初三的时候就倒闭了吗？"
    show qy emml2
    qy "是啊，没想到它后来复活了。而且一晃眼又开了这么久了。"
    show qy wowl1
    qy "在你搬走后，确实还发生了不少事情呢......"
    hide qy
    "Zubizubi......嗯......该怎么形容它呢？"
    "印象里它好像什么关于音乐的“东西”都会卖......"
    "以前放学后，我也经常会和朋友一起来。"

    p "Zubizubi音乐杂货铺，好怀念啊。不过从外观看，它现在已经是新的样子了。"
    show qy emml2
    qy "你继续回想吧，我要先走一步了。待在店里可比“呆”在外面有趣多了。"
    p "等等我！"

    scene zubi_mid with fade

    "进店，熟悉又陌生的感觉扑面而来。依旧是琳琅满目的cd、唱片和器材配件。"
    "角落里堆放的不是一捆一捆的音乐杂志，就是猜不出从哪儿来，也猜不出怎么用的乐器。"

    p "货品......怎么感觉比以前多了好几倍?!"
    show qy posl1
    qy "没错，更像“洞穴”了。"
    hide black
    p "但意外打理的......很干净。"
    show qy wowl1
    qy "这里的店员应该工作得很辛苦吧，毕竟要维护这么多商品。"
    
    scene zubi_in with fade
    show qy wowl1

    qy "诶，你看！这里竟然有这个，感觉上次好像看舅舅摆弄过类似的东西。"
    hide qy
    "说着，千叶拿起那个摆在货架旁的细长圆筒，左右倾斜了一下。{p}里面发出“哗啦哗啦”豆子滚过般的声音。"
    play sound "audio/soundeffect/rainstick1.wav"

    menu:
        "竟然会发出这种声音啊。":
            show qy posl3
            qy "很有意思吧。"
            show qy posl1
            qy "看外观绝对猜不到呢。"

        "原来是这么用的啊。":
            show qy norl2
            qy "嗯，上次舅舅怎么说得来着？"
            show qy wowl1
            qy "好像是“......当地人用来祈雨的乐器”。"
            show qy emml2
            qy "不过家里那个现在应该已经在仓库吃灰了。"

    show qy wowl1
    p "啊切！"
    show qy emml2
    qy "没事吧，难道说搬家太累，有点感冒了？"
    p "应该不是，但是周围好像有什么奇异的味道。"
    show qy wowl1
    qy "可能是店里焚的香吧，昨天刚下过雨。"
    p "我怎么不记得店里以前有这种“特色”。"
    show qy emml2
    qy "可能是老板的新爱好吧。不过我也好一阵子没见到她了。"
    hide qy
    scene zubi_counter with fade
    "接着，我注意到一位很酷的小姐杵在收银台后。{p}台面上散落着一些泡泡糖纸。"


    "这家伙为了吹出更大的泡泡......到底一次嚼了多少块？"
    "【解锁成就：泡泡糖纸】"

    "她手里拿着一本漫画书，正聚精会神地翻阅着，似乎忽略了我们的光顾。"

    "千叶走上前去，用手指叩了叩玻璃台面。"
    "哒哒——"
    show qy posl2 at right
    qy "马奇，你在看什么呢？"
    "“啪”的一声，那位小姐正吹着的泡泡瞬间瘪了，{w=0.5}视线随即从漫画移向了我们，露出了狡黠的笑容。"
    show mq wowl1 at left
    mq_unknown "诶，千叶！{w=0.3}我说怎么声音有些耳熟，原来是你啊！"
    show mq posl2
    mq_unknown "好久不见，我正打算餐厅出新菜品的时候去找你玩呢！"
    show mq thinkl1
    qy_unknown "嗯？不过，乐队的聚餐也临近了......"
    show mq posl4
    qy_unknown "到时候很多人，很多很多菜，嘻嘻嘻嘻......"
    
    show qy emml2
    qy "欢迎你随时光临。"
    hide qy
    hide mq
    
    show mq wowl1
    mq_unknown "哦，你旁边怎么还多了一个新朋友？这位是......"

    menu:
        "你好，我叫[pname]，今天刚搬回临春。":
            jump intro1
            hide mq

        "你好，我叫[pname]，是千叶以前的同学。":
            jump intro2
            hide black

label intro1:
    show mq posl1 at left
    mq_unknown "诶？这么巧。{w=0.3}今天折腾回来辛苦了吧？{w=0.5}我叫马奇，今后我们也许会经常见面了。"
    
    p "好在有千叶的帮忙，最辛苦的部分很快就搞定了。"
    show mq posl4
    mq "——是啊，有千叶这样一位朋友真好啊。"
    show qy emml2 at right
    qy "马奇，你都夸得我不好意思了。"
    p "所以......"
    menu:
        "马奇是这里的店员吗？":
            hide qy
            hide mq
            show mq posl4h
            mq "你猜？"
            show mq posl3
            mq "哈哈哈，不卖关子了。其实我也是来逛店的啦。"
            p "原来是这样啊。"

        "马奇是这里的老板吗？":
            hide qy
            hide mq
            show mq posl4h
            mq "你猜？"
            show mq posl3
            mq "哈哈哈，不卖关子了。其实我也是来逛店的啦。"
            p "原来是这样啊。"

    jump after_intro
label intro2:
    show mq posl1 at left
    mq "真羡慕啊！{w=0.3}像你们这种从小就认识的友谊。我叫马奇，算是这里的......常客吧？{p}当然也是千叶家餐厅的忠实粉丝。"
    mq "不过千叶的朋友就是我的朋友，今天我们就算认识了。"
    p "嗯，马奇......可真是"

    menu:
        "很有热情、活力呢。":
            show qy emml2 at right
            qy "她是个“自来熟”。"

        "有点“自来熟”呢。":
            show qy emml2 at right
            qy "她一贯如此。"

    show mq naul1
    mq "嘿嘿，其实是“人来疯”啦。"
    hide qy
    hide mq

    jump after_intro

label after_intro:

    show mq wowl1
    mq "对了，刚才我光顾着自报家门了。你们今天来店里，是想找点什么吗？"
    p "嗯......好像确实没想过。"

    menu:
        "马奇有什么推荐的吗？":
            show mq posl4b
            mq "哼哼，这你可就问对人啦！平时我可是在这里淘到过不少便宜好货。"
            show qy emml2 at right
            show mq posl4h
            qy "马奇似乎在这方面“嗅觉”意外灵敏呢。"
            hide qy
            show mq posl2b
            mq "是“听”！人家是靠听的啦。"
            show mq sadl0b
            mq "再说有什么其它技巧的话......那就是“心”吧。没错！一颗“寻宝”的心。"
            show mq posl1
            mq "毕竟我平时好像也就靠这两样，不管是打鼓还是干别的什么。"
            hide mq at char_out
            "说着马奇低头看向收银台，用两根食指随意地在玻璃台边轻轻敲出了一小段节拍。{p}看不出她此时是在思考还是放空。"
            show qy posl1 at right
            qy "哈哈，怎么感觉话题“嗖”的一下就跳到了打鼓呢。"
            hide qy at char_out
            show mq wowl1w
            mq "诶呀，一不小心就把话题扯远了。"
            p "所以......马奇小姐是因为打鼓，才会这样思考吗？"
            show mq thinkl1
            mq "嗯......这我倒没怎么想过呢？"
            show mq sadl0b
            mq "或许是这样吧。毕竟我也算是个不入流的职业鼓手。"

        "马奇对这里很熟悉吗？":
            show mq thinkl1
            mq "嘛，算是吧。"
            show mq posl2w
            mq "毕竟我平时是打鼓的，经常会来这里淘点稀奇古怪的玩意儿。拿回去学习学习。"

            p "原来马奇小姐是鼓手吗？"
            show mq posl4h
            mq "嗯，姑且算是不入流的职业鼓手吧。"

    menu:
        "听起来是很酷的职业":
            show mq wowl1w
            mq "不过，不是什么很稳定的工作。"
            show mq posl3
            mq "好处是可以经常去现场看演出。自己演，也听别人演。{w=0.3}总之，在live house表演，{w=0.5}最棒了！"
            hide mq
            show qy posl1
            qy "对马奇来说，打鼓好像不只是一份工作呢。"

        "听起来，是一份有点辛苦又掺杂着不稳定的工作呢":
            show mq posl4
            mq "哈哈，的确如此。"
            show mq posl1
            mq "不过在舞台上表演开始的那一刻——{w=0.3}一切就都感觉不一样了。{w=0.5}live表演最有意思了!"
            hide mq
            show qy posl1
            qy "马奇在舞台上的样子可是和平时很不一样呢。"

    menu:
        "马奇在舞台上......是什么样子呢？":
            hide qy
            show mq posl4h
            mq "这个嘛，你看到就知道啦。现在暂时保密！"
            show mq wowl1
            mq "哦，对啦！正好我手里还剩两张，你和千叶一人一张吧。"
            "马奇不知从哪里翻出两张彩色纸条“啪”的一下拍在了玻璃台面上。"
            show mq pail1
            mq "诶呦，刚才为了装酷没控制好力度，失误、失误。"
            show mq posl1h
            mq "不过留在台面上的才是重点。"
            hide mq
            p "......这是？"

        "live表演、live house是什么？":
            hide qy
            show mq wowl1w
            mq "诶，你没有去过live house吗？"
            p "确实对我来说是有些陌生的概念。平时听音乐基本上都是通过耳机。"
            hide mq
            "马奇开始低头在口袋里摸索起来。"
            "下一秒，她掏出两张彩色纸条，“啪”地拍在了玻璃台面上。{p}......听声音就知道拍得不轻。"

            show mq posl5
            mq "唔，那这个你一定要收下！！！千叶也有份。"
            hide mq
            p "......这是？"

    show qy posl3 at right
    qy "哈哈，是马奇他们下次表演的门票，那我就不客气的收下了！"
    show mq emol1 at left
    mq "呜呜，千叶，谢谢你的支持。"
    show mq posl2w
    mq "呐，把这个首尾相粘一下，变成手坏，就可以带着它自由进出live house了。{p}不过只可以在指定场次使用哦，比如说我所在的乐队登台表演的那一晚。"

    menu:
        "乐队？马奇的乐队吗？":
            hide mq
            hide qy
            show mq posl4h
            mq "既然那么好奇，不如直接来现场看看呗？"
            p "好吧，看来只有去到现场才能知道了。"
            hide mq

        "我会和千叶一起的！":
            hide mq
            hide qy
            show mq posl4
            mq "一言为定哦！{w=0.3}到时候在台下看不到可爱的你们我会伤心的。"
            hide mq
    scene zubi_in with fade
    with vpunch
    yz_unknown "刚才是什么动静？！我在库房都听到了，我以为你只是来安静地看会儿漫画的，马小姐——"
    scene zubi_counter with fade
    show mq wowl1
    mq "哦，对喽，今天我们乐队的另一个家伙碰巧也在。"
    scene zubi_in with fade
    with vpunch
    yz_unknown "什么？来客人了你也不跟我讲一声？！还是我在这边伸着脖子才看到的......"
    "声音听着有些耳熟。"
    yz_unknown "稍等一下，我马上就来——"
    "总觉得在哪里听过这个声音。{w=0.5}可一时半会儿又想不起来。"
    scene zubi_counter with fade
    show qy emml2
    "千叶朝货架后方瞟了一眼，微微往前探了探脑袋，{w=0.5}然后一脸坏笑地看向了我。"
    show qy posl2
    qy "哦？{w=0.3}原来今天不止马奇在，连盐之也在啊。"
    hide qy
    "——“盐之”？"
    p "......盐之......"

    "难怪总觉得耳熟！"
    "脚步声越来越近。"

    menu:
        "看去":
            pause 0.5
            show yz wowl1 at char_in,center
            yz "嗯？你怎么会出现在这里。"
            show yz thinkl1
            yz "马奇和千叶看起来没问题啊，都和平时一个样，原来——"
            show yz posl1
            yz "你真的回来啦。"

        "眼神回避":
            yz "哦，是千叶啊，还有——"
            yz "一个完全没想到会出现在这里的家伙。"
            show yz posl1 at char_in,center
            pause 0.3
            yz "我以为你不会回来了呢？"
            
        
        
    menu:
        "......":
            p "......"
            "一时间不知道该说些什么。"
            "......就随便说点什么吧。"


        "确实好久没见了呢，盐之。":
            show yz thinkl1
            yz "嗯......嘛......也没有很久啦。也就六、七年？"
            hide yz at char_out
            show mq huhl1 at char_in,center
            mq "啊？六七年难道不是很久了吗？已经够我......呃，让我想一想——"
            hide mq at char_out
            show qy emml2 at char_in,center
            qy "够考拉OK换不知道多少轮季节菜单了。"
            hide qy at char_out
    menu:
        "你头发变长了。":
            show yz wowl1
            yz "嗯，反正现在也不会有什么中学的老古板揪着这点不放了。"
            show yz posl2
            yz "你也变了很多。"
            hide yz at char_out

        "长头发很适合你。":
            show yz awkl2h
            yz "怎么上来就说这种话。"
            hide yz at char_out

    show mq wowl2 at char_in,left
    mq "等等，等等？？？怎么感觉我好像错过了一些剧情？！"
    show mq wowl1hw
    mq "盐之和[pname]之间难道有什么我不知道的“过去”吗？"
    show qy posl4 at char_in,right
    qy "是关于两人青梅竹马的部分啦。"
    with vpunch
    p "......等等。千叶，你刚刚脱口而出了什么啊？！"
    with vpunch
    show mq huhl1
    mq "哦？！"
    hide mq at char_out
    hide qy at char_out
    show yz norl1c at char_in,center
    yz "那都多久以前的事了。"
    show yz norl1cb
    "......{w=0.5}嗯？"
    #with hpunch
    "盐之他怎么好像脸红了......{w=0.5}{cps=30}那家伙在搞什么啊？"
    hide yz at char_out
    show mq norl1h at char_in,center
    mq "啊？？？"
    show mq thinkl2
    mq "所以......你跟千叶认识......千叶跟[pname]认识，而你和[pname]居然也早就认识了！"
    show mq wowl2
    mq "搞了半天，{w=0.5}原来只有我是“新角色”？！"
    hide mq at char_out
    show yz posl1h at char_in,left
    yz "时候不早了......马奇你不是还要去乐器行教课吗？"
    show qy posl3 at char_in,right
    qy "好啦好啦，马奇，以后你总会知道的。"
    show qy emml2
    qy "现在，赶紧去上课吧。{w=0.3}你也不想来让来上课的小朋友在教室苦苦等待吧。"
    hide yz
    hide qy
    show mq wowl2 at char_in,center
    with vpunch
    mq "可是我八卦还没听够啊喂！！下次、下次，{w=0.3} [pname]一定要讲给我听啊！！"
    hide mq
    #【“哐当”一声，
    "门被带上了。{p}店内音箱里的音乐不知不觉换了一首。"
    show yz thinkl1 at char_in,left
    yz "库房那边还剩点货要清点......"
    show qy posl1 at char_in,right
    qy "没事，我们自己逛就行了，你先去忙吧。"
    
    # 表情切换、眨眼，停顿一下
    show yz wowl0
    yz "......"
    show yz posl1
    yz "那就拜托了，我先回后面了。"
    show yz posl3w
    yz "有问题就喊我！"
    hide yz at char_out
    p "嗯。"
    hide yz at char_out
    hide qy at char_out
    scene zubi_mid with fade
    "盐之回到库房去了。{p}我和千叶又在店里停留了一小会儿。"
    scene zubi_out with fade
    "再出来时，外面的太阳亮得有些刺眼。"
    #【切入店外隐约的午后蝉鸣与微风声】#
    "回到临春的第一天，似乎比想象中还要热闹得多。"

label after_date:

    #【场景背景切换：街道、店面之类的】

    scene coala_out_x with fade
    pause 0.4
    scene street_home1_x with fade
    pause 0.4
    scene street_home2_x with fade
    "和千叶逛着逛着，天已经快黑了。"
    show qy posl1 at char_in,center
    qy "那就下周live见了。"
    p "不过，在那之前，我们应该还会见面吧。"
    show qy posl2
    qy "说得也是。有空再约！"
    p "嗯。"
    show qy posl4
    qy "不用担心打扰到我哦，{w=0.5}有事我会直说的。"
    
    "(千叶的头顶似乎长出了天使光环。)"
    
    p "呜呜......{p}天使......"
    show qy wowl1
    qy "？"
    
    p "没什么。"
    show qy posl1
    qy "那就拜拜喽，到时候手机联系。"

    scene street_home1_x with fade
    pause 0.3
    scene phome_livingroom_n with fade
    pause 0.3
    scene phome_bedroom_n with fade
    #场景背景切换：家门口，玄关，房间】

    p "走了一天，终于可以躺下了。"

    "不过身体虽然累了，{w=0.5}但感觉大脑好像还没有困意。{p}毕竟白天发生了那么多事情。"
    "接下来要怎么度过这个夜晚呢？"
    menu:
        "就开始准备睡觉吧。":
            jump sleep_route

        "要不......再去公园走走？":
            jump park_route


label sleep_route:

    "简单收拾了一下，就钻入了被窝。"
    scene bedroom_n with fade
    pause 1.0
    jump day_sick

label park_route:
    $ visited_park1 = True
    scene street_home1_n with fade
    pause 0.3
    scene street_home2_n with fade
    pause 0.3
    scene park_mid_n with fade
    #【转场：街道、店面之类的；街道、路灯、飞虫、一点点泛白的天空，这时候看你们的了！】
    p "啊——{w=0.5}公园，{w=0.3}好久没来这里了。" #【可以放过去公园的样子】
    "现在这个时候，还能隐约听到一点蝉鸣。{w=0.3}露在外面的皮肤还能感受到丝丝凉风，{w=0.3}光是坐在长椅上就很放松了。"
    p "这种时候，如果还能带上耳机，听着自己喜欢的歌曲，{w=0.3}那就更爽了。"
    scene park_n with fade
    "掏出耳机，选好音乐，正准备戴上时——"

    "“窸窸窣窣”——"
    "声音是从旁边的树丛传来的。"
    "“咔嚓”——像是什么树枝被踩断了。"
    "——大概是什么小动物弄出的声响吧。"
    "“唰唰唰”"
    "——像是有什么东西靠近了。"
    with vpunch
    show mm 
    "下一秒，一个少女从树丛里钻了出来。"
    "她低头拍了拍身上的叶子和灰尘，像是什么都没发生过一样。"

    msu_unknown "......可恶，又跟丢了。"

    "很快，她注意到了我的目光。"

    msu_unknown "哈，被你看到了。"

    menu:

        "把目光移开":

            msu_unknown "要不......就把你定为下一个目标吧？"

            p "”......！“"

            msu_unknown "放心，不会一上来就把你灭口的。"

            p "”......！！“"

            "然后是漫长的几声蝉鸣，树叶被风吹得沙沙作响。{p}还有她越来越近的脚步声。"

            msu_unknown "这个耳机应该已经是很多年前的东西了吧。"

            "诶？——"

            "她抬了抬下巴，指向我手里的耳机。"

            p "......我不太了解呢。只知道是很久以前买的了。"

            msu_unknown "虽然2年前再版过一次，不过果然原版的质感还是无法替代啊。"

            hide mm

            "现在周围的光线已经逐渐暗了下来，她居然还能......看得这么清楚？"

            show mg at char_in,right

            ms_unknown "该回去了。"

            show mm at char_in,left

            msu_unknown "知道了，毛莎。本来我也要往家走了"

            msu_unknown "那就下次再见了。"

            hide mm
            hide mg

            "少女冲我摆了摆手，转身和神秘男子向公园出口走去。"

            show mm at char_in,center

            msu_unknown "哦，对了。"

            "突然, 她又退回几步，转头对我说。"

            msu_unknown "刚才只是没忍住，{w=0.5}捉弄了一下你。"

            hide mm at char_out

            "少女的脚步声远去了。"

            "{w=0.5}啊——{w=0.5}松了一口气。"

            "总觉得刚刚那两个人像同一种生物。"

            "之后，又独自坐了一会儿。"

            "回到家，简单收拾了一下，就进入了梦乡。"
            scene black with fade
            jump day_sick




        "继续看着她":

            "我们对视了几秒。昏暗的光线下，她的皮肤却依然白得像会反光一样。"

            "接着，她的视线落到了我身上。"

            "难道我身上有什么奇怪的东西吗？"

            "她眯了眯眼睛，向我靠近了几步。"

            msu_unknown "这个耳机应该已经是很多年前的东西了吧。"

            "她抬了抬下巴，指向我手里的耳机。"

            p "......我不太了解呢。只知道是很久以前买的了。"

            msu_unknown "虽然2年前再版过一次，不过果然原版的质感还是无法替代啊。"

            hide mm

            "现在周围的光线已经逐渐暗了下来。她居然还能......看得这么清楚？"

            show ms at char_in,right

            ms_unknown "该回去了。"

            show mm at char_in,left

            msu_unknown "知道了，毛莎。本来我也要往家走了"

            msu_unknown "那就下次再见了。"

            hide mm
            hide ms

            "少女冲我摆了摆手，转身和神秘男子向公园出口走去。"

            "......{p}......总觉得那两个人像同一种生物。"

            "之后，又独自坐了一会儿。"

            "回到家，简单收拾了一下，就进入了梦乡。"

            scene black with fade

            jump day_sick

label day_sick:

    scene phome_bedroom with fade

    p "啊切、啊切！"

    "一醒来脑袋昏昏沉沉。"

    p "体温计放在哪里了来着......？"

    #play sound "audio/rummage.ogg"
    "（翻箱倒柜声）"

    #play sound "audio/thermometer_beep.ogg"
    "（体温计滴滴声）"

    p "怎么温度这么高？！"

    scene black with fade

    "接下来的一周里，大部分时间都在家静养。"


    "（滴滴）"

    "手机上浮现出千叶的信息："
    "（考拉创口贴emoji？）{p}千叶：祝你早日康复，{p}期待下周一起去看live哦。"

    scene phome_bedroom with fade

    "感觉好点的时候——{w=0.3}基本上都在看书、打游戏。"

    "（体温计滴滴声）"

    "好在，在去看live的日期前，{w=0.3}痊愈了！"
    #【转场、转场表示时间的流逝】



label before_livehouse:

    # 去livehouse前
    #【新一天开始的音乐】
    "今天就是去看演出的日子了。{p}昨天已经和千叶约好集合的时间地点。"

    "......不过，穿什么好呢？"

    menu:

        "酷酷的考拉OK文化衫":
            $ outfit = "koala"
            "好像是哪年在考拉OK吃饭获得的赠品。"
            "额，上面怎么还破了几个洞啊？！完全不记得是怎么搞的了。好在不影响穿着。"
            

        "中性风的鸭舌帽和乐队t恤":

            $ outfit = "band"
            "t恤还是以前在Zubizubi买的。"
            "买的时候好像有点大了，所以没怎么穿过。现在穿......意外的很合身！"

        "崭新的短款机车夹克":

            $ outfit = "jacket"
            "连吊牌都还没拆。"
            "当初脑子一热买了下来，结果一次都没穿出去过。......穿这个去看live，应该正合适吧。"

        "和平时穿的一样":
            $ outfit = "normal"
            "最后还是选了最习惯的那套搭配。"
            "虽然没什么特别的，但身体和心情都很轻松。"
    
    "随声听、手机、钥匙......都已经在口袋里了。"
    "都穿戴好了，感觉可以出发了！"
    "对了，还有这个“手环”。门票一定得带上。"

    "“滴滴”"
    "手机上浮现出千叶的信息：我快到了，一会儿门口见。"
label outside_livehouse:
    #【转场：街道、店面之类的；live house门口】
    scene street_home2_n with fade
    qy "这边！"
    qy "你还蛮有精神的嘛，看来已经完全恢复了。"#（眯眼笑）
    "......可能是感冒药、漫画书、游戏机、小说们的功劳吧。"
    if outfit == "koala":
        qy "哦？竟然穿着考拉OK文化衫。"
        qy "真有点怀念呢。"
        p "嗯，原来一直好好躺在衣柜里。"
    if outfit == "band":
        qy "哈哈，没想到你今天竟然穿得这么”内行“。"
        p "怎么说？"
        qy "就跟那些低调的乐迷一样。"
        p "原来是这样。"
    if outfit == "jacket":
        qy "哦？很少见你穿这么拉风的行头。"
        qy "不过，很适合你哦！"
        p "谢谢夸奖！"
    if outfit == "normal":
        qy "和平时一样的穿着。"
        qy "......有句话怎么说来着——{p}“日常”就是最朋克的。"
        p "第一次听说。"

    qy"对了，我从餐厅给你带了慰问品。"#（爽朗的笑容）
    "“拆开包装声”"
    p "是考拉形状的饼干。"
    menu:

        "那我就不客气的收下了！":

            qy "好吃的话，我下次再给你带。"

        "谢谢你，千叶！":
            qy "不用客气，小意思啦。"

    qy "时间差不多了，我们进去吧。"
    "说着千叶指了指我们背后live house的入口。"

#【环境音为主】
label enter_livehouse:
    "踏过一级一级狭窄的台阶，日常世界的感觉被一点一点稀释。"
    "两侧墙壁上爬满了让人不得不停下脚步、思考几秒才能读懂的涂鸦和海报。{p}路过它们时，目光总会不自觉地被勾住。{p}灯光在冷暖之间不断切换，连感官都变得有些失真。"
    "终于，我们又开始走在平地上。"

    "而这间 live house 真正的内部，也终于向我们敞开——"
    #【 声音串场，开始有背景音乐。】
    "走马观花地扫过去——"
    "啊，是小狗；"
    "还有游戏海报！"
    qy "真的有这个游戏吗？"
    "诶，实验性电子乐？还是现场演奏的？！{p}等等，小吃摊和水吧怎么也在这里？{p}他们到底是怎么全都挤进来的——"  


label jiancheng_intro:

    show jc posl1 at char_in,center

    jc_unknown "哈喽，千叶。好久不见。" #（眯眼笑

    qy "好久不见。"

    jc_unknown "之前听马奇说，你今天会和朋友一起来。"

    "他的目光落到了我身上。"

    jc_unknown "这位就是马奇提到的那位“朋友”吧？"
    jc_unknown "请问怎么称呼你？"

    p "我叫[pname]，你好。"

    jc_unknown "幸会，叫我简诚就好。"

    menu:

        "你也是今天演出的乐手吗？":

            jc "哦，忘了自我介绍了，我是和马奇同乐队的键盘手。"

            jc "呐，手环上这里，就是我们乐队的名字。"

            "说着他指了指自己手腕上的手环。"

            "这才发现，自己手上的那条和他戴的，印有相同的文字"

            p "原来叫Kidsplay啊。"

            jc "嗯。" #面带笑意的点了点头

            hide jc at char_out
            jump maosha_intro



        "你和千叶很熟？":

            jc "哈哈，算是吧。"
            jc "大概是因为我们整个乐队都是她们家餐厅的忠实顾客。"

            jc "{cps=150}都是因为某些家伙每次演出完都吵着闹着要吃，吃不到就不消停。{/cps}{nw}"
            $ renpy.pause(0.8)

            p "刚刚感觉有什么奇怪的话快速溜过了。"

            qy "考拉OK，算是Kidsplay的传统聚餐地吧。" #(大笑)

            jc "有的时期，餐厅生意异常火爆。我也会提前联系千叶，麻烦她预留位置。"

            jc "一来二去，好像就熟络起来了。"

            p "Kidsplay......"

            jc "嗯，我们乐队的名称是{w=0.２}K-I{w=0.２}-D{w=0.２}-S{w=0.２}-P{w=0.２}-L{w=0.２}-A{w=0.２}-Y，{w=0.5}Kidsplay。"

            jc "你带的手环上也应该也有写。"

            "说着他抬了抬手腕, 轻轻晃了晃手环。"

            hide jc at char_out

            "仔细一看，和我的印字完全一样，只是颜色不同。"
            jump maosha_intro



label maosha_intro:

    #"毛莎登场"
    show ms norl1 at char_in,center

    "这时，有人从后面拍了拍简诚的肩膀。"

    ms_unknown "那两人迟到了，我们先去调试吧。"

    "语气平静得几乎没有起伏。"

    if visited_park1:
        "——是昨天公园里那个人。"
        #“原来他不是吸血鬼、外星人什么的。”
    
    ms_unknown  "你好，千叶。"
    qy "好久不见。"

    hide ms at char_out
    "对方说完就要转身离去。"
    show jc at char_in,left
    jc "毛莎，稍等一下。"

    jc "这是[pname]，今天和千叶一起来的。"
    show ms at char_in,right
    p "你好。"

    ms_unknown "你好。"

    jc "他是毛莎，我们乐队的贝斯手。"

    "毛莎微微点了点头。{w=0.3}视线从我的手环上扫过，什么也没说。"

    ms_unknown "我们得走了。"
    jc "[pname]和千叶，那就一会儿演出见了。"
    hide jc at char_out
    hide ms at char_out
    p "嗯。"
    show qy posl1 at char_in,center
    qy "回见。"
    hide qy at char_out

label before_show:
    "快开场了，我和千叶也移步到了演出区域。"
    qy "太好了，前排还空着！"
    qy "走，我们去找个离表演最近的位置。"
    "千叶兴奋地指了指舞台下方。"
    "那里被一排金属护栏隔了出来。"
    p "这些护栏......看起来真像丧尸片里用来阻挡僵尸的装置。"

    qy "哈哈哈，说不定一会儿真的会变成那样呢。"

    p "总觉得一会儿耳朵会被震麻......两边的音箱离得也太近了。"
    qy "没错，有时候可能还得用上耳塞。"
    p "耳塞？......没有准备。"
    p "不过......"
    "在兜里摸索了一会儿......"
    "！{p}找到了！"
    p "这个是不是也行？"
    "掏出随身听——上面还缠着那副常用的耳机。"
    qy "嗯，有这个应该就够了！"

    fana "Kidsplay?听说这支乐队的前主唱好像和他们是不欢而散啊。"
    fanb "啊？我听说不是因为那个吉他手吗？"
    fana "真的假的......"

    truefan "你们这些家伙怎么会相信、传播这种不靠谱的小道消息？！就不能把注意力放在音乐上吗？"

    "灯光暗了下来—— "

    fanab"......"
    truefan "来了来了！"
    #（口哨声）（电吉他扫音/总之就是失真但真实的诡异电音）
    "——Kidsplay登场了。"




label snowball_fight:
    scene black with fade
    play music "snowbgm.mp3"
    show snow
    "走出排练室，空气格外清新，大脑也从刚才的燥热中渐渐冷静下来。"

    "雪正淅淅沥沥地落到周围的一切事物上。我觉得自己的脸热得发烫，雪花大概也没法在上面停留。"
    play sound "snowball_hit.mp3"
    with hpunch
    "啪！"

    "被什么东西从背后狠狠拍打了一下。"
    $ timeout = 10
    $ timeout_label = "snow_timeout"

    show screen countdown
    menu:

        "刚刚那个雪球多半是："

        "盐之扔的":
            hide screen countdown
            jump snow_yanzhi

        "马奇丢的":
            hide screen countdown           
            jump snow_maqi

        "简诚投的":
            hide screen countdown
            jump snow_jiancheng

        "毛莎？......真的会是他吗？":
            hide screen countdown
            jump snow_maosha



label snow_timeout:
    hide screen countdown
    "我愣了一下，把手从兜里掏了出来。"

    yz "完了......好像投得有点准。"

    "趁手指还没感觉到冷，就回敬了盐之一个更扎实的雪球。"
    play sound "snowball_hit.mp3"
    with hpunch
    mq "打雪仗竟然不带我！看招儿！"

    jump snow_merge


label snow_yanzhi:

    "我立马把手从兜里掏了出来。趁手指还没感觉到冷就回敬了一个更扎实的雪球。"
    play sound "snowball_hit.mp3"
    with hpunch
    yz "诶？！你怎么猜到的？"

    mq "打雪仗竟然不带我！看招儿！"

    jump snow_merge


label snow_maqi:

    "我立马把手从兜里掏了出来。趁手指还没感觉到冷就回敬了一个更扎实的雪球。"
    play sound "snowball_hit.mp3"
    with hpunch
    mq "喂喂喂，我哪有盐之那么坏！"

    yz "完了......好像投得有点准。"

    mq "不过......打雪仗？这个我擅长！！看招儿！"

    jump snow_merge


label snow_jiancheng:

    "我立马把手从兜里掏了出来。趁手指还没感觉到冷就回敬了一个更扎实的雪球。"
    play sound "snowball_hit.mp3"
    with hpunch
    jc "这种事，一般都不会是我主动挑起的。"

    yz "完了......好像投得有点准。"

    mq "打雪仗竟然不带我！看招儿！"

    jump snow_merge


label snow_maosha:

    "虽然不太确定，我还是立马把手从兜里掏了出来。趁手指还没感觉到冷就回敬了一个更扎实的雪球。"
    play sound "snowball_hit.mp3"
    with hpunch
    ms "......我只负责团雪球。"

    yz "完了......好像投得有点准。"

    mq "打雪仗竟然不带我！看招儿！"

    jump snow_merge


label snow_merge:
    play sound "snowball_hit.mp3"
    with hpunch
    play sound "snowball_hit.mp3"
    with hpunch
    yz "嗷！你俩下手轻点儿！"

    ms "我暂时当盐之的盟友。"

    yz "你又不会真出手，还不是看我被打。"

    "盐之顺手接过毛莎递来的新雪球。"

    jc "有人帮你团雪球就不错了。"

    p "既然“战争”已经被挑起了……"

    jc "我选择中立……"
    play sound "snowball_hit.mp3"
    with hpunch
    jc "为什么中立派也有人打！"

    mq "战争来临时谁都不能置身事外！"

    play sound "snowball_hit.mp3"
    with hpunch
    "哈哈哈"
    play sound "snowball_hit.mp3"
    with hpunch
    play sound "snowball_hit.mp3"
    with hpunch
    with hpunch
    

    yz "不如我们停战、建交，来堆个超大的雪人吧！"

play sound "snowball_hit.mp3"
with hpunch

mq "就堆那种身子要两、三个人推才能推得动的！"

play sound "snowball_hit.mp3"
with hpunch

jc "听起来脑袋至少也得两个人抬。"

ms "……胡萝卜的话，我可以帮忙。"

play sound "snowball_hit.mp3"
with hpunch
with hpunch

"我看了看手里正攥着的雪球。"

menu:
    "要停战吗？"

    "嗯，那就停吧。":

        "我蹲下身，松开了手，让雪球自然滚落到覆盖着积雪的地面上，然后把它往雪里按了按，又向前轻轻推了一下。"

        "太好了。雪是粘的。"

        p "这下真的可以堆雪人了！"

        "推雪球是让人不知疲倦的事。因为只要一直推，雪球就会一直变大，直到重得几个人都推不动为止。"

        jc "照这个大小继续滚下去……不会因为妨碍交通被带走吧？"

        mq "诶？！"

        yz "诶？！"

        p "诶？！"

        ms "……离人行道还差三米。"

    "不要。":

        p "再玩一会儿吧！"

        mq "乐意奉陪！"

        yz "可恶，竟然没有中计。"

        yz "毛莎，再给我团三个。"

        "毛莎手上的动作还是和刚才一样，并没有加快。"

        jc "我帮你团两个吧，毛莎。"

        mq "啊？简诚，你怎么跑去帮他们了！说好的中立呢！！"

        mq "[pname]快！趁现在！打乱他们的计划！"

        p "收到！"
        play sound "snowball_hit.mp3"
        with hpunch

        jc"好险——差点就被打中了。"

        "此时马奇的行动也发生了变化。原本只是重复着团雪球、扔雪球、躲雪球的循环，现在开始在这些动作之余往旁边一块儿较高的积雪上再添几把雪，然后拍拍；再加几把雪，然后按一按。我立刻读懂了她的意图——"
        ms "对面的防御系统升级了。"
        yz"不过我们已经都不是小孩子了，那种以前平趴在自己筑起的雪墙后面就能挡住飞来的雪球的伎俩，现在还好不好用还真不好说。"
        jc"不过是建造本身就是乐趣的一部分。"
        "看着马奇干得起劲的样子，只会让人想加入她的行动。"
        p"诶呀！"
        "就在我分神的片刻，耳朵就被一个雪球砸中了。"
        "一些雪飞溅到我嘴里，尝起来只有凉凉的感觉。"
        mq"[pname]被击中了，看我的！"
        play sound "snowball_hit.mp3"
        
        window hide
        $ timeout = 3
        $ timeout_label = "snow_down"
        show screen countdown
        # "是啊——"
        menu:
            "“明天要不要一起堆雪人？”":
                hide screen countdown
                window show
                p"明天要不要一起堆雪人！"
                mq "好啊，明天我也没课。"
                yz"我没意见。"
                ms"……我带胡萝卜。"
                jc"只要明天没有暴风雪。"
                play sound "snowball_hit.mp3"
                with hpunch
                jc"好险，{w=0.5}幸好躲开了。"

label snow_down:
    "鼓起勇气，往身后一片还无人踏足的雪地上倒了下去。整个人作为一个“大”字陷了进去。"
    "或许是刚才说了太多话，扔了太多雪球，也可能是因为了被砸了太多次，此时已经累得完全不想动弹。"
    "我勉强挪了挪脑袋，让自己躺得更舒服些。"
    "盯着空中缓缓飘落的雪花——{p}下雪......{p}如果一直下雪就好了。"
    "“我们明天去堆雪人吧？”声音透过积雪和帽子模模糊糊地传入耳中。"
    jc "你还真是执着啊。"
    mq"明天，我们去堆雪人！"

    window hide
    $ timeout = 3
    $ timeout_label = "snow_mute"
    show screen countdown
    menu:
        "“嗯！”":
            hide screen countdown
            window show
            "我“腾”的一下坐了起来，开始把粘在身上的雪片一一拍落。"
            "不小心溅了一点点到嘴里，没有尝出什么特别的味道。"

label snow_mute:
    "我没有回应。又在雪地里躺了一会儿，然后直起了身。"
    "掸落身上粘着的雪时，不小心弄了一点到嘴巴里。{p}尝起来没有味道。"

    jump afte_musicfestival

   


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

label afte_musicfestival:
    "粉色的头发......{w=0.5}是伊娜！"
    menu:
        "追上去！":
            jump chasing_ina
        "留在原地。":
            jump stay_there
#追逐战小样
label chasing_ina:

    scene crowd
    play music "chasingher.mp3"
    play audio "steps.mp3"
    "现在舞台上刚刚结束一段精彩的表演，台下一部分激动的观众正在阵阵高呼“安可！安可！安可！”，想把喜欢的乐队招唤回来，让他们再多演一会儿。还有一部分观众已经开始结伴往出口前进，大概是想去休息区稍作调整，好精力充沛的迎接下一场令人心潮澎湃的演出。"

    "这时我才意识到，想要在这样的人流中追上伊娜——可真不是什么容易的事情。"

    show team1
    "左前方的人群松散一些，两个学生模样的女生正在亲密地交头接耳。\n右前方人头攒动，密密麻麻，前方那位酷酷的游客手里，还拿着一杯随时可能撒出来的饮料。"

    menu:
        "走左前方":

            hide team1
            show ill

            "女生a：“贝斯手她好帅啊......”"
            "女生b：”我感觉脑袋晕晕的，会不会是中——”"
            "眼看少女就要晕倒，刚好经过她身旁的我——"

            menu:

                "扶！":

                    "我勉强扶住了少女，避免了她的摔倒，把她交给她同伴后，我和伊娜的距离——又拉开了点。"

                "不扶！":

                    "虽然没有出手，但少女还是勉强稳住了自己的身体，她的同伴也及时扶住了她，我和伊娜的距离——没有什么变化。"


        "走右前方":

            hide team1
            show beer

            "在我与那名游客擦肩而过的同时，她巧妙的转了个身，避免了我和她手中的饮料有任何接触。"

            "她大声喊道：“夏日冰饮，真是太爽啦！我可不想浪费任何一滴。”"

            hide beer

            "我和伊娜的距离似乎近了一些。"


        "走正前方":
            hide team1
            hide ill
            hide beer
            "走中间确实和看起来的一样可行。我和伊娜的距离缩短了不少。"

            "但是她随即加快了脚步。"

            p "......可恶啊。{p}她的速度比我想象中还要快。"

    hide team1
    hide ill
    hide beer
    "伊娜的帽檐时不时瞥向我这边，却始终没有停下自己的脚步。"


    show dancer
    show couple
    play audio "steps.mp3"
    menu:

        "我继续追逐着伊娜的步伐,前路出现了像弹簧一样蹦蹦跳跳的跳舞小子和正在热聊的两个路人。"
        

        "走跳舞小子那边":

            hide couple
            hide dancer

            "那小子似乎感应到了我的开始匆匆，立刻为我让开了道路。"

            hide dancer

            p "谢啦！"

            "但我与伊娜的距离，似乎只增不减。"


        "走两个路人那边":

            hide dancer
            hide couple

            show puke
            play sound "puke_effect.mp3"

            "其中一个路人竟然开始疯狂呕吐了起来。"
            "她的同伴小声嘟囔着：“.......你没事吧？要不要去休息一下？”"

            hide puke

            "把我吓得往旁边一跳。和伊娜的距离又拉开了一些。"

            p "可恶，这下肯定追不上了。"

    
    "虽然心里已经觉得多半是追不上了，但我的步伐一刻也没敢停歇。" 
    stop music
    stop audio   #jump stay_there
    "好在，她终于停了下来。{p}随即竟转过身，主动走到了我的面前。"
    ina"看来也是个执着的家伙呢。"
    "趁着我大口喘气的功夫，伊娜自顾自地说起话来。"
    ina"在我离开后，大家果然重振旗鼓，走向了更大的舞台。{p}还招募到了像你这样的新成员。"
    "被伊娜盯着的感觉像是"
    show bear2
    ina"你应该知道我是谁吧？不然也不会追我这么一段路了。"
    show bear1
    ina"player，很高兴见到你。我是伊娜，Kidsplay的前主唱。"
    ina"时间有限，让我先问你一个问题吧。"
    ina"如果有一天，你在舞台上的光芒逐渐掩盖了Kidsplay其他成员，而你又比任何人都清楚，他们也拥有理应被世界所看见的才华。这时，一个能让你单飞的机会摆在你的面前。你会怎么选？"
    "我勉勉强强地顺了口气。"
    menu:
        "我绝对不会离开Kidsplay的。":
            ina"有意思。没想到你这么勇敢。有你在的话......应该会不一样吧。"
            ina"那就祝你好运喽。"
        "我大概也会做出和你一样的选择吧。":
            
            p "也会......{w=0.5}作出那个离开的决定。"
            ina"那个平时沉默寡言的男孩，当时应该已经猜到我的意图了吧？"
            ina"虽说不管怎么选都没有错。但我的离开，大概让盐之那家伙，偷偷难过了很久吧。"
            #ina"为了伙伴的离开而难过，为了梦想又要晚一点实现而难过......为了自己想要伙伴留下的那一点点私心而难过。"
            p"原来伊娜也不是完全不了解盐之的心情。"
    "几声消息提示音从伊娜的手机里传来，但统统被她无视了。"
    ina"好了，现在轮到我回答你一个问题了。"
    menu:
        "你当初为什么会离开kids play？":
            ina"因为我知道自己想要什么也知道别人想要什么。我不想让观众只记住“伊娜的乐队”，这对乐队里其他人的才华来说实在是种浪费。他们可不是现在那些，围绕在我身边，单单为了在舞台上衬托我而存在的家伙。当明星更适合我，我可没什么创作天赋。"
        "伊娜你会为什么而难过吗？":
            ina"意想不到的问题。如果认真回答的话，大概——"
            ina"如果有一天，无法遵循内心的声音而行动，应该会让我很难过吧。"
        
        "你和盐之......之前是情侣吗？":  
            ina "哈哈哈，真是把我逗笑了。我们可没有交往过。我知道他有一个喜欢了很久的人。而我喜欢的人嘛——" 
            show bear3
            play sound "rose.mp3"
            "伊娜真诚的目光能让被她注视的人内心产生强烈的震颤，我深有所感。{p}这就是动物遇到比自己强大的存在时会有的本能反应吗？{p}说到底，人类也是动物的一种​。" 
            hide bear3
            stop sound
        "下次再来看我们的表演吧！":
            "伊娜愣了一下，好像刚刚发现了什么小小的惊喜。"
            ina"行啊，到时候记得给我留赠票。"
    show bear1
    "此刻，伊娜的手机开始吱吱作响。铃声是一首我和kidsplay的大家一起排练过的歌。"
    "伊娜按灭了手机铃声，说道——"
    ina"我的团队在等我了，他们应该也在等你吧。我们两个该回去了。"
    "她向我道了别，又在手机上输入了什么，便匆匆转身离去。眼前的粉色一点一点融入面前鲜活躁动的人群，直到彻底消失不见。"




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
