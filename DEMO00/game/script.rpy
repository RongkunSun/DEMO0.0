# 游戏的脚本可置于此文件中。
#define config.main_menu_music = "audio/littlestar.mp3"



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
    #call scene1_onthetrain from _call_scene1_onthetrain
    call zubizubi_intro from _call_zubizubi_intro
    
    

    #call work
    #call layoff
    #call train
    #call test_qianye_full
    #call train_station

    return






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
            play sound "awww.mp3"

            "她大声喊道：“夏日冰饮，真是太爽啦！我可不想浪费任何一口。”"

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

        "我继续追逐着伊娜的步伐，前方出现了像弹簧一样蹦蹦跳跳的跳舞小子和正在热聊的两个路人。"
        

        "走跳舞小子那边":

            hide couple
            hide dancer

            "那小子似乎感应到了我的来势匆匆，立刻为我让开了道路。"

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
    ina"如果有一天，你在舞台上的光芒逐渐掩盖了Kidsplay其他成员，而你又比任何人都清楚，他们拥有着值得被世界所看见的才华。这时，一个能让你单飞的机会摆在你的面前。你会怎么选？"
    "我勉勉强强地顺了口气。"
    default stay_kidsplay = False

    menu:
        "我绝对不会离开Kidsplay的。":
            $ stay_kidsplay = True
            ina"有意思。没想到你这么勇敢。有你在的话......应该会不一样吧。"
            ina"那就祝你好运喽。"
        "我大概也会做出和你一样的选择吧。":
            $ stay_kidsplay = False    
            p "也会......{w=0.5}做出那个离开的决定。"
            ina"那个平时沉默寡言的男孩，{p}当时应该猜到我的意图了吧？"
            ina"虽说不管怎么选都没有错。但我的离开，大概让盐之那家伙，偷偷难过了很久吧。"
            #ina"为了伙伴的离开而难过，为了梦想又要晚一点实现而难过......为了自己想要伙伴留下的那一点点私心而难过。"
            p"原来伊娜也不是完全不了解盐之的心情。"
    "几声消息提示音从伊娜的手机里传来，但统统被她无视了。"
    ina"好了，现在轮到我回答你一个问题了。"
    menu:
        "你当初为什么会离开Didsplay K？":
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
        "下次再来看我们的表演吧！" if stay_kidsplay:
            "伊娜愣了一下——这似乎是个出乎意料的邀请。"
            ina"行啊，到时候记得给我留赠票。"
    show bear1
    "此刻，伊娜的手机开始吱吱作响。铃声是一首我和kidsplay的大家一起排练过的歌。"
    "伊娜按灭了手机铃声，说道——"
    ina"我的团队在等我了，他们应该也在等你吧。我们两个该回去了。"
    "她向我道了别，又在手机上输入了什么，便匆匆转身离去。眼前的粉色一点一点融入面前鲜活躁动的人群，直到彻底消失不见。"


#考拉餐厅奶奶给我们祖传戒指小样：
label koalaok_final:
    show grandmasay
    play music "grandmachat.mp3"
    koala_grandma "......[pname]，等一下......来帮我试试餐厅新研发的方便茶包......看看味道......和在店里喝到的相比......怎么样......"
    play sound "hotwater.mp3"
    "真的只是眨了几下眼睛的功夫，两杯热腾腾的红茶就已经被泡好端上了桌——"
    play sound "clearingspoon.mp3"
    "茶包的确泡起来方便又快捷，闻起来也和店里能喝到的那种一模一样。"
    play sound "rollingrollingspoon.mp3"
    "等着红茶放凉的功夫，考拉奶奶悠悠地说道——"
    show grandmalook
    koala_grandma "时间过得可真快啊......一转眼，我们千叶就已经能在餐厅独当一面了。"
    "我点点头，小口啜饮着还冒着热气的红茶，鼻尖和眼睛都能感受到温暖的氤氲。"
    play sound "rollingrollingspoon.mp3"
    koala_grandma "我有的时候会问问她，有没有觉得继承餐厅......让她少了很多和同龄人一起打打闹闹、轻松自在的时光......或者说，少了很多和朋友一起出去冒险的机会。"
    show grandmafade
    "即使很忙，千叶也经常抽出时间和我们玩......{p}忙着平衡工作和日常生活的同时，也不忘时不时给朋友制造些“小惊喜”。"
    hide grandmafade
    koala_grandma "每次她都说......自己拥有的......是非常宝贵的机会，一想到客人因为吃到餐厅里美味的食物而留下美好的回忆，她就觉得——“经营餐厅，是一件很值得投入的事情。”"

    show powerfulqianye
    "可以想像千叶笑着说出这种话的情景。"
    hide powerfulqianye
    show grandmafade
    koala_grandma "经营这样一家餐厅不仅心中要充满对生活的热爱，同时也意味着对重复、繁琐的事务日复一日的坚持。"
    "一直陪伴在我身边的千叶对于我是什么样的存在呢？"
    hide grandmafade

    play sound "putring.mp3"
    koala_grandma "对了......这枚戒指就交给你了[pname]......就由你帮我拿给千叶吧。"
    hide grandmalook
    show grandmasay
    "此时一枚戒指正静静地躺在刚刚还摆过茶杯的桌面上。"
    
    "考拉奶奶拿着我俩喝完的茶杯慢慢悠悠地走向了后厨。"

    koala_grandma "好像今天还约了姐妹们唱露天KTV......差点儿忘了......现在走应该还来得及......"

    menu:
        "奶奶我送你去露天KTV场所吧。":
            koala_grandma "好......好......那真是谢谢你啦！"

        "奶奶那我先走了。":
            koala_grandma "行......咱俩各自去忙各自的吧。"

    koala_grandma "......看来下个产品就让他们......去研发......用冷水就能泡好的......冷泡红茶吧......"

    koala_grandma "一定会很受现在都市年轻人喜欢的。"

    "当我拿起那枚戒指时，发现它也带上了一点两杯热茶留下的温度。"

    "要在什么时候把这枚戒指交给千叶呢？{p}在这之前我会好好保管它的。"


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
