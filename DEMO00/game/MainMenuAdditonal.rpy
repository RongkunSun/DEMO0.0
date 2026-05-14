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