screen test_button:
    
    imagebutton:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 0.05
        focus_mask True
        idle "gui/button/PlainCombatButton.png"
        hover "gui/button/PlainCombatButton.png"
        action Show("test_menu")
        at test_extension

transform test_extension:
    ypos 0.05
    on hover:
        linear 0.5 ypos 0.1
    on idle:
        linear 0.5 ypos 0.05
    

screen test_menu:
    modal True

    image "images/Interactables/pausemenu lines.png"

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 1.png"
        hover "images/Interactables/pausemenu button 1 hover.png"
        action Hide("test_menu")

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 2.png"
        hover "images/Interactables/pausemenu button 2 hover.png"
        action Hide("test_menu")

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 3.png"
        hover "images/Interactables/pausemenu button 3 hover.png"
        action Hide("test_menu")

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 4.png"
        hover "images/Interactables/pausemenu button 4 hover.png"
        action Hide("test_menu")

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 5.png"
        hover "images/Interactables/pausemenu button 5 hover.png"
        action Hide("test_menu")
    
    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 6.png"
        hover "images/Interactables/pausemenu button 6 hover.png"
        action Hide("test_menu")

    imagebutton:
        focus_mask True
        idle "images/Interactables/pausemenu button 7.png"
        hover "images/Interactables/pausemenu button 7 hover.png"
        action Hide("test_menu")