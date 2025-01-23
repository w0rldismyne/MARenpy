screen settings:
    modal True

    imagemap:
        alpha False

        ground "New Assets/Title/title_image.png"
        idle "New Assets/Title/title_idle.png"
        hover "New Assets/Title/title_hover.png"

        hotspot (596, 234, 83, 82) action Return()
        hotspot (697, 235, 81, 81) action Return()
        hotspot (583, 883, 223, 66) action Return()
        hotspot (583, 968, 150, 69) action Return()

screen settings_2:
    modal True

    imagemap:
        alpha False

        ground "New Assets/Confirm - Pause/pause_frame.png"
        idle "New Assets/Confirm - Pause/pause_idle.png"
        hover "New Assets/Confirm - Pause/pause_hover.png"

        hotspot (600, 12, 382, 313) action Return()
        hotspot (1006, 12, 404, 311) action Return()
        hotspot (601, 347, 295, 209) action Return()
        hotspot (922, 347, 488, 211) action Return()
        hotspot (602, 579, 529, 265) action Return()
        hotspot (1149, 575, 263, 270) action Return()
        hotspot (601, 862, 381, 206) action Return()
        hotspot (1003, 860, 405, 203) action Show("confirmation")

screen confirmation:
    modal True

    imagemap:
        alpha False

        ground "New Assets/Confirm - Pause/confirm_frame.png"
        idle "New Assets/Confirm - Pause/confirm_idle.png"
        hover "New Assets/Confirm - Pause/confirm_hover.png"

        hotspot (951, 632, 136, 52) action Hide("confirmation"), Return()
        hotspot (1106, 631, 137, 55) action Hide("confirmation")