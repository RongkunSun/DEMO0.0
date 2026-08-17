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