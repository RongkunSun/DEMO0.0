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