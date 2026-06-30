#gallery accessed from main menu
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

#Main menu parallax background
init python:

    class ParallaxDisplayable(renpy.Displayable):

        def __init__(self, child, depth=20.0, speed=0.1, **kwargs):
            super(ParallaxDisplayable, self).__init__(**kwargs)

            self.child = renpy.displayable(child)

            self.x = 0.0
            self.y = 0.0

            self.tx = 0.0
            self.ty = 0.0

            self.depth = depth
            self.speed = speed

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            # 鼠标安全处理（关键）
            mx, my = renpy.get_mouse_pos()

            if mx is None or my is None:
                mx = width * 0.5
                my = height * 0.5

            # 标准化坐标（屏幕无关）
            dx = (mx / float(width)) - 0.5
            dy = (my / float(height)) - 0.5

            # 视差目标（depth = 最大像素偏移）
            self.tx = -dx * self.depth
            self.ty = -dy * self.depth

            # easing（稳定版）
            self.x += (self.tx - self.x) * self.speed
            self.y += (self.ty - self.y) * self.speed

            # 渲染子图
            cr = renpy.render(self.child, width, height, st, at)

            # 避免浮点 jitter
            rv.blit(cr, (int(self.x), int(self.y)))

            # 稳定刷新（避免 0ms 死循环）
            renpy.redraw(self, 0.016)

            return rv

        def visit(self):
            return [self.child]
#image bg_parallax = ParallaxDisplayable("bg.png", depth=30)
    #scene bg_back
    #show bg_mid
    #show bg_front
#image bg_back  = ParallaxDisplayable("back.png", depth=60)
#image bg_mid   = ParallaxDisplayable("mid.png", depth=35)
#image bg_front = ParallaxDisplayable("face.png", depth=20)

#speacial screen effect
default timeout = 3.0
default timeout_label = None

screen countdown():

    if timeout_label:

        timer timeout action [
            Hide("countdown"),
            Jump(timeout_label)
        ]