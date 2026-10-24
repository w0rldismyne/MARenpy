# Boss Sprites
default boss_active = "images/Sprites/Mariko/Boss1.png"
default boss_idle = "images/Sprites/Mariko/Boss1.png"
default boss_attack = "images/Sprites/Mariko/4.png"
default boss_hurt = "images/Sprites/Mariko/3.png"

# UI Panels
default info_overlay = "New Assets/Fight/fight_frame.png"

screen boss_overlay():

    image "[info_overlay]"

screen nagen_hp_bars():

    image "New Assets/Fight/name_nagen.png":
        xanchor 0.0
        yanchor 0.5
        pos 124, 1032

    text "Nagen":
        color "#000000"
        xanchor 0.0
        yanchor 0.5
        pos 134, 1036

    # Nagen's Health
    bar:
        xanchor 0.0
        yanchor 0.5
        pos 60, 945
        xysize 814, 89
        value nagen_current_hp
        range nagen_hp
        left_bar "New Assets/Fight/mc_hp_full.png"
        right_bar "New Assets/Fight/mc_hp_empty.png"
        left_gutter 156
        right_gutter 15

    text "[nagen_current_hp]/[nagen_hp]":
        xanchor 1.0
        yanchor 0.5
        pos 829, 949
        size 40

default nagen_current_hp = -1
default nagen_hp = -1

default nagen_attack = -1
default nagen_defense = -1

default turn_order = 0
define nagen_turn = 0
define boss_turn = 1
define round_end = 2

# Fight Resolution
default fight_end_state = -1
define lose = 0
define win = 1