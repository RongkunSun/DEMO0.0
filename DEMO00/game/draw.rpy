init python:

    import os
    import math
    import time
    import pygame

    # 预设色块(5 列 x 2 行)
    CATDRAW_COLORS = [
        "#000000", "#ffffff", "#e53935", "#fb8c00", "#fdd835",
        "#43a047", "#29b6f6", "#1e88e5", "#8e24aa", "#f48fb1",
    ]

    # 预设笔刷大小(半径,像素)
    CATDRAW_SIZES = [6, 14, 26]

    class CatDrawCanvas(renpy.Displayable):
        """画布:背景层(纯色/底图) + 画笔层(透明 surface) + 印章层(列表)。"""

        def __init__(self, width, height, bg_color="#ffffff", bg_image=None, **kwargs):
            super(CatDrawCanvas, self).__init__(**kwargs)

            self.cw = width
            self.ch = height

            # 画笔层:透明 surface,笔画直接画进来;橡皮画 alpha=0 打透明洞
            self.paint = pygame.Surface((width, height), pygame.SRCALPHA)

            self.tool = "brush"              # "brush" | "eraser" | "stamp"
            self.color = CATDRAW_COLORS[2]
            self.radius = CATDRAW_SIZES[1]
            self.stamp = None                # 当前选中的印章路径
            self.pick_bg = False             # 开启后,下一次点色块改的是背景色

            self.bg_color = bg_color
            self.bg_image = bg_image
            self.stamps = []                 # 已放置的印章 [{path, x, y, w, h}]

            self.drawing = False
            self.last = None

            self._bg_d = None                # 缓存的背景 displayable
            self._bgimg_d = None
            self._stamp_d = {}               # path -> displayable
            self._stamp_size = {}            # path -> (w, h)

        # ── 渲染:背景 → 画笔层 → 印章 ──

        def render(self, width, height, st, at):
            w, h = self.cw, self.ch
            rv = renpy.Render(w, h)

            if self._bg_d is None:
                self._bg_d = Solid(self.bg_color)
            rv.blit(renpy.render(self._bg_d, w, h, st, at), (0, 0))

            if self.bg_image:
                if self._bgimg_d is None:
                    self._bgimg_d = Transform(self.bg_image, xysize=(w, h))
                rv.blit(renpy.render(self._bgimg_d, w, h, st, at), (0, 0))

            rv.canvas().get_surface().blit(self.paint, (0, 0))

            for s in self.stamps:
                d = self._stamp_d.get(s["path"])
                if d is None:
                    d = self._stamp_d[s["path"]] = Image(s["path"])
                rv.blit(renpy.render(d, w, h, st, at), (s["x"], s["y"]))

            return rv

        # ── 事件 ──

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if 0 <= x < self.cw and 0 <= y < self.ch:
                    if self.tool == "stamp":
                        if self.stamp:
                            self._place_stamp(x, y)
                    else:
                        self.drawing = True
                        self.last = (x, y)
                        self._dab(x, y)
                        renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEMOTION and self.drawing:
                self._segment(self.last, (x, y))
                self.last = (x, y)
                renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.drawing = False
                self.last = None

            return None

        # ── 画笔/橡皮 ──

        def _dab(self, x, y):
            x, y = int(x), int(y)
            if self.tool == "eraser":
                self._erase_stamps_at(x, y)
                pygame.draw.circle(self.paint, (0, 0, 0, 0), (x, y), self.radius)
            else:
                pygame.draw.circle(self.paint, Color(self.color), (x, y), self.radius)

        def _segment(self, p0, p1):
            # 沿线段插值画圆点,快速拖动也不会断
            (x0, y0), (x1, y1) = p0, p1
            dist = math.hypot(x1 - x0, y1 - y0)
            n = max(1, int(dist / max(1, self.radius // 2)))
            for i in range(1, n + 1):
                t = i / n
                self._dab(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)

        def _erase_stamps_at(self, x, y):
            r = self.radius
            hit = [s for s in self.stamps
                if pygame.Rect(s["x"], s["y"], s["w"], s["h"]).inflate(2 * r, 2 * r).collidepoint(x, y)]
            for s in hit:
                self.stamps.remove(s)

        # ── 印章 ──

        def _place_stamp(self, x, y):
            size = self._stamp_size.get(self.stamp)
            if size is None:
                size = self._stamp_size[self.stamp] = renpy.load_surface(self.stamp).get_size()
            w, h = size
            self.stamps.append({"path": self.stamp,
                                "x": int(x - w / 2), "y": int(y - h / 2),
                                "w": w, "h": h})
            renpy.redraw(self, 0)

        # ── 工具栏调用的方法 ──

        def set_tool(self, tool):
            self.tool = tool
            if tool != "stamp":
                self.stamp = None
            renpy.restart_interaction()

        def set_color(self, color):
            if self.pick_bg:
                self.bg_color = color
                self._bg_d = None
                self.pick_bg = False
                renpy.redraw(self, 0)
            else:
                self.color = color
                self.tool = "brush"
                self.stamp = None
            renpy.restart_interaction()

        def set_size(self, radius):
            self.radius = radius
            renpy.restart_interaction()

        def set_stamp(self, path):
            self.stamp = path
            self.tool = "stamp"
            renpy.restart_interaction()

        def toggle_pick_bg(self):
            self.pick_bg = not self.pick_bg
            renpy.restart_interaction()

        def clear(self):
            self.paint.fill((0, 0, 0, 0))
            del self.stamps[:]
            renpy.redraw(self, 0)

        # ── 保存 ──

        def save_png(self):
            surf = pygame.Surface((self.cw, self.ch))
            surf.fill(Color(self.bg_color))

            if self.bg_image:
                bg = renpy.load_surface(self.bg_image)
                try:
                    bg = pygame.transform.smoothscale(bg, (self.cw, self.ch))
                except Exception:
                    bg = pygame.transform.scale(bg, (self.cw, self.ch))
                surf.blit(bg, (0, 0))

            surf.blit(self.paint, (0, 0))

            for s in self.stamps:
                surf.blit(renpy.load_surface(s["path"]), (s["x"], s["y"]))

            path = os.path.join(_catdraw_save_dir(),
                                time.strftime("painting_%Y%m%d_%H%M%S") + ".png")
            pygame.image.save(surf, path)
            renpy.notify("画保存好啦！")

    def _catdraw_save_dir():
        d = os.path.join(config.savedir, "paintings")
        os.makedirs(d, exist_ok=True)
        return d

    def catdraw_saved_paintings():
        """返回已保存画作的 PNG 绝对路径列表,按保存时间从旧到新排序。"""
        d = os.path.join(config.savedir, "paintings")
        if not os.path.isdir(d):
            return []
        return sorted(os.path.join(d, f) for f in os.listdir(d)
                    if f.lower().endswith(".png"))


# 游戏用这个变量控制可用印章(用 default 声明,随存档保存解锁状态)
default catdraw_stamps = []


screen catdraw(background=None, bg_color="#ffffff", stamps=None):

    modal True

    # 防止小朋友滚轮误触回滚,把画丢掉
    key "rollback" action NullAction()
    key "rollforward" action NullAction()

    default panel = CatDrawCanvas(1480, 1040, bg_color=bg_color, bg_image=background)

    $ catdraw_stamp_list = stamps if stamps is not None else catdraw_stamps

    add Solid("#f7edda")

    # 画布(外框 + viewport 裁掉超出边缘的印章)
    frame:
        xpos 14
        ypos 14
        background "#8d6e63"
        padding (6, 6)
        viewport:
            xysize (1480, 1040)
            add panel

    # 工具栏
    frame:
        xpos 1512
        ypos 14
        xysize (394, 1052)
        background "#fff3e0"
        padding (16, 16)

        vbox:
            spacing 14

            hbox:
                spacing 12
                textbutton "画笔":
                    style "catdraw_button"
                    xsize 175
                    action Function(panel.set_tool, "brush")
                    selected panel.tool == "brush"
                textbutton "橡皮":
                    style "catdraw_button"
                    xsize 175
                    action Function(panel.set_tool, "eraser")
                    selected panel.tool == "eraser"

            hbox:
                spacing 12
                for i, r in enumerate(CATDRAW_SIZES):
                    textbutton "●":
                        style "catdraw_button"
                        xsize 112
                        ysize 76
                        text_size (22 + i * 18)
                        action Function(panel.set_size, r)
                        selected panel.radius == r

            grid 5 2:
                spacing 8
                for c in CATDRAW_COLORS:
                    button:
                        xysize (62, 62)
                        padding (3, 3)
                        background "#b8a894"
                        hover_background "#7a6a55"
                        selected_background "#e65100"
                        action Function(panel.set_color, c)
                        selected (panel.color == c and not panel.pick_bg)
                        add Solid(c)

            textbutton ("↑ 点上面的色块换背景" if panel.pick_bg else "换背景颜色"):
                style "catdraw_button"
                xsize 362
                action Function(panel.toggle_pick_bg)
                selected panel.pick_bg

            text "印章:" style "catdraw_label"

            viewport:
                xysize (362, 300)
                mousewheel True
                scrollbars "vertical"
                vbox:
                    spacing 8
                    if catdraw_stamp_list:
                        for row_start in range(0, len(catdraw_stamp_list), 3):
                            hbox:
                                spacing 8
                                for p in catdraw_stamp_list[row_start : row_start + 3]:
                                    button:
                                        xysize (108, 108)
                                        padding (6, 6)
                                        background "#ffffff"
                                        hover_background "#ffe0b2"
                                        selected_background "#ffb74d"
                                        action Function(panel.set_stamp, p)
                                        selected (panel.tool == "stamp" and panel.stamp == p)
                                        add Transform(p, xysize=(96, 96), fit="contain")
                    else:
                        text "还没有可用的印章" style "catdraw_label"

            hbox:
                spacing 12
                textbutton "清空":
                    style "catdraw_button"
                    xsize 175
                    action Confirm("要把画全部擦掉吗？", yes=Function(panel.clear))
                textbutton "保存":
                    style "catdraw_button"
                    xsize 175
                    action Function(panel.save_png)

            textbutton "关闭画板":
                style "catdraw_button"
                xsize 362
                action Return()


style catdraw_button is button:
    background "#ffffff"
    hover_background "#ffe0b2"
    selected_background "#ffb74d"
    insensitive_background "#eeeeee"
    padding (10, 14)

style catdraw_button_text is button_text:
    size 32
    color "#6d4c41"
    hover_color "#4e342e"
    selected_color "#bf360c"
    xalign 0.5
    yalign 0.5

style catdraw_label is text:
    size 26
    color "#8d6e63"