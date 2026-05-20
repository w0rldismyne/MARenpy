init python:
    def panel_transforms(panel_state):
        if panel_state is c_i_hidden:
            return pitchblack
        elif panel_state is c_i_to_be_revealed:
            return reveal_panel
        else:
            return None

    def set_profile_availability(name, value):
        i_profile_list[name]["available"] = value
        return

    def fake_reveal_panel(page, panel_name):
        if i_chapter_layouts[current_chapter][page][panel_name]["state"] is c_i_hidden:
            i_chapter_layouts[current_chapter][page][panel_name]["state"] = c_i_to_be_revealed
        return

    def real_reveal_panel(page, panel_name):
        i_chapter_layouts[current_chapter][page][panel_name]["state"] = c_i_revealed
        return

# Chapter Constant
define c_chapter_prologue = 0
define c_chapter_one = 1
define c_chapter_two = 2

# Investigation States Constants
define c_i_hidden = -1
define c_i_to_be_revealed = 0
define c_i_revealed = 1

# Profile States
define c_i_profile_available = 1
define c_i_profile_unavailable = 0
define c_i_profile_hidden = -1

# UI States
define investigation_first_enter = True
define profile_animation_lock = False
default clipboard_opened_state = False
define profile_page = 1


define temp_culprit_list = False

# region UI Elements - Investigation
image clipboard_idle:
    "images/Interactables/clipboard_interactable.png"

image clipboard_hover:
    "images/Interactables/clipboard_interactable.png"
    matrixcolor BrightnessMatrix(0.1)

image tab_pi_idle:
    "images/Interactables/TabPinkFalse.png"

image tab_pi_highlighted:
    "images/Interactables/TabPinkFalse.png"
    matrixcolor BrightnessMatrix(0.1)

image tab_pi_active:
    "images/Interactables/TabPink.png"

image tab_bl_idle:
    "images/Interactables/TabBlueFalse.png"

image tab_bl_highlighted:
    "images/Interactables/TabBlueFalse.png"
    matrixcolor BrightnessMatrix(0.1)

image tab_bl_active:
    "images/Interactables/TabBlue.png"

image tab_pu_idle:
    "images/Interactables/TabPurpleFalse.png"

image tab_pu_highlighted:
    "images/Interactables/TabPurpleFalse.png"
    matrixcolor BrightnessMatrix(0.1)

image tab_pu_active:
    "images/Interactables/TabPurple.png"

image tab_gr_idle:
    "images/Interactables/TabGreenFalse.png"

image tab_gr_highlighted:
    "images/Interactables/TabGreenFalse.png"
    matrixcolor BrightnessMatrix(0.1)

image tab_gr_active:
    "images/Interactables/TabGreen.png"
# endregion

# region UI Elements - Profiles
image i_profile_chisei:
    "images/Interactables/chiseiprofile.png"

image i_profile_chisei_hidden:
    "images/Interactables/chiseiprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_chisei_inactive:
    "images/Interactables/chiseiprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_dyre:
    "images/Interactables/dyreprofile.png"

image i_profile_dyre_hidden:
    "images/Interactables/dyreprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_dyre_inactive:
    "images/Interactables/dyreprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_ichita:
    "images/Interactables/ichitaprofile.png"

image i_profile_ichita_hidden:
    "images/Interactables/ichitaprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_ichita_inactive:
    "images/Interactables/ichitaprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_kazz:
    "images/Interactables/kazzprofile.png"

image i_profile_kazz_hidden:
    "images/Interactables/kazzprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_kazz_inactive:
    "images/Interactables/kazzprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_kietsu:
    "images/Interactables/kietsuprofile.png"

image i_profile_kietsu_hidden:
    "images/Interactables/kietsuprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_kietsu_inactive:
    "images/Interactables/kietsuprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_kitsune:
    "images/Interactables/kitsuneprofile.png"

image i_profile_kitsune_hidden:
    "images/Interactables/kitsuneprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_kitsune_inactive:
    "images/Interactables/kitsuneprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_mariko:
    "images/Interactables/marikoprofile.png"

image i_profile_mariko_hidden:
    "images/Interactables/marikoprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_mariko_inactive:
    "images/Interactables/marikoprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_momoko:
    "images/Interactables/momokoprofile.png"

image i_profile_momoko_hidden:
    "images/Interactables/momokoprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_momoko_inactive:
    "images/Interactables/momokoprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_mu:
    "images/Interactables/muprofile.png"

image i_profile_mu_hidden:
    "images/Interactables/muprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_mu_inactive:
    "images/Interactables/muprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_nanase:
    "images/Interactables/nanaseprofile.png"

image i_profile_nanase_hidden:
    "images/Interactables/nanaseprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_nanase_inactive:
    "images/Interactables/nanaseprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_setsuna:
    "images/Interactables/setsunaprofile.png"

image i_profile_setsuna_hidden:
    "images/Interactables/setsunaprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_setsuna_inactive:
    "images/Interactables/setsunaprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_shoma:
    "images/Interactables/shomaprofile.png"

image i_profile_shoma_hidden:
    "images/Interactables/shomaprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_shoma_inactive:
    "images/Interactables/shomaprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_taiga:
    "images/Interactables/taigaprofile.png"

image i_profile_taiga_hidden:
    "images/Interactables/taigaprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_taiga_inactive:
    "images/Interactables/taigaprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_rei:
    "images/Interactables/reiprofile.png"

image i_profile_rei_hidden:
    "images/Interactables/reiprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_rei_inactive:
    "images/Interactables/reiprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_rise:
    "images/Interactables/riseprofile.png"

image i_profile_rise_hidden:
    "images/Interactables/riseprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_rise_inactive:
    "images/Interactables/riseprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")

image i_profile_yoku:
    "images/Interactables/yokuprofile.png"

image i_profile_yoku_hidden:
    "images/Interactables/yokuprofile.png"
    matrixcolor TintMatrix("#000000FF")

image i_profile_yoku_inactive:
    "images/Interactables/yokuprofile.png"
    matrixcolor SaturationMatrix(0.1) * TintMatrix("#00000088")
# endregion

# region Panels
# Ch 1 Panels
define ch1_panel1 = "images/Interactables/Manga_Ch1_Panel_1.png"
define ch1_panel2 = "images/Interactables/Manga_Ch1_Panel_2.png"
define ch1_panel3 = "images/Interactables/Manga_Ch1_Panel_3.png"
define ch1_panel4 = "images/Interactables/Manga_Ch1_Panel_4.png"
define ch1_panel5 = "images/Interactables/Manga_Ch1_Panel_5.png"

# Ch 2 Panels
define ch2_p1panel1  = "images/Interactables/Manga_Ch2_Page1_Panel_1.png"
define ch2_p1panel2  = "images/Interactables/Manga_Ch2_Page1_Panel_2.png"
define ch2_p1panel3i = "images/Interactables/Manga_Ch2_Page1_Panel_3_I.png"
define ch2_p1panel3r = "images/Interactables/Manga_Ch2_Page1_Panel_3_R.png"
define ch2_p1panel4  = "images/Interactables/Manga_Ch2_Page1_Panel_4.png"
define ch2_p1panel5  = "images/Interactables/Manga_Ch2_Page1_Panel_5.png"
define ch2_p1panel6i = "images/Interactables/Manga_Ch2_Page1_Panel_6_I.png"
define ch2_p1panel6r = "images/Interactables/Manga_Ch2_Page1_Panel_6_R.png"

define ch2_p2panel1i  = "images/Interactables/Manga_Ch2_Page2_Panel_1_I.png"
define ch2_p2panel1r  = "images/Interactables/Manga_Ch2_Page2_Panel_1_R.png"
define ch2_p2panel2  = "images/Interactables/Manga_Ch2_Page2_Panel_2.png"
define ch2_p2panel3 = "images/Interactables/Manga_Ch2_Page2_Panel_3.png"
define ch2_p2panel4  = "images/Interactables/Manga_Ch2_Page2_Panel_4.png"
define ch2_p2panel5  = "images/Interactables/Manga_Ch2_Page2_Panel_5.png"
define ch2_p2panel6 = "images/Interactables/Manga_Ch2_Page2_Panel_6.png"

# Ch 3 Panels
# endregion

# Investigation Layout Rules & Flags
# EXTRA

default i_chapter_layouts = {
    c_chapter_one: {
        1: {
            "panel1": {"state": c_i_hidden, "image": ch1_panel1, "discovered": False, "group": None},
            "panel2": {"state": c_i_hidden, "image": ch1_panel2, "discovered": False, "group": None},
            "panel3": {"state": c_i_hidden, "image": ch1_panel3, "discovered": False, "group": None},
            "panel4": {"state": c_i_hidden, "image": ch1_panel4, "discovered": False, "group": None},
            "panel5": {"state": c_i_hidden, "image": ch1_panel5, "discovered": False, "group": None}
        }
    },

    c_chapter_two: {
        1: {
            "panel1":  {"state": c_i_hidden, "image": ch2_p1panel1,  "discovered": False, "group": None},
            "panel2":  {"state": c_i_hidden, "image": ch2_p1panel2,  "discovered": False, "group": None},
            "panel3":  {"state": c_i_hidden, "image": ch2_p1panel3i, "discovered": False, "group": 213},
            "panel4":  {"state": c_i_hidden, "image": ch2_p1panel4,  "discovered": False, "group": None},
            "panel5":  {"state": c_i_hidden, "image": ch2_p1panel5,  "discovered": False, "group": None},
            "panel6":  {"state": c_i_hidden, "image": ch2_p1panel6i, "discovered": False, "group": 216}
        },
        2: {
            "panel1":  {"state": c_i_hidden, "image": ch2_p2panel1i, "discovered": False, "group": 221},
            "panel2":  {"state": c_i_hidden, "image": ch2_p2panel2,  "discovered": False, "group": None},
            "panel3":  {"state": c_i_hidden, "image": ch2_p2panel3,  "discovered": False, "group": None},
            "panel4":  {"state": c_i_hidden, "image": ch2_p2panel4,  "discovered": False, "group": None},
            "panel5":  {"state": c_i_hidden, "image": ch2_p2panel5,  "discovered": False, "group": None},
            "panel6":  {"state": c_i_hidden, "image": ch2_p2panel6,  "discovered": False, "group": None}
        }
    }
}

default i_tab_layouts = {
    "pink":   {"number": 1, "idle": "tab_pi_idle", "hovered": "tab_pi_highlighted", "selected": "tab_pi_active"},
    "blue":   {"number": 2, "idle": "tab_bl_idle", "hovered": "tab_bl_highlighted", "selected": "tab_bl_active"},
    "purple": {"number": 3, "idle": "tab_pu_idle", "hovered": "tab_pu_highlighted", "selected": "tab_pu_active"},
    "green":  {"number": 4, "idle": "tab_gr_idle", "hovered": "tab_gr_highlighted", "selected": "tab_gr_active"}
}

default i_profile_list = {
    "chisei":  {"name":"Chisei Jikoma",    "available": c_i_profile_unavailable},
    "dyre":    {"name":"Dyre Okami",       "available": c_i_profile_unavailable},
    "ichita":  {"name":"Ichita Kinoshita", "available": c_i_profile_unavailable},
    "kazz":    {"name":"Kazz Kataki",      "available": c_i_profile_unavailable},
    "kietsu":  {"name":"Kietsu Himura",    "available": c_i_profile_hidden},
    "kitsune": {"name":"Kitsune Sumizome", "available": c_i_profile_unavailable},
    "mariko":  {"name":"Mariko Genki",     "available": c_i_profile_unavailable},
    "momoko":  {"name":"Momoko Yoshino",   "available": c_i_profile_unavailable},
    "nanase":  {"name":"Nanase Keisan",    "available": c_i_profile_hidden},
    "mu":      {"name":"Oshin Murakami",   "available": c_i_profile_unavailable},
    "rei":     {"name":"Rei Watabe",       "available": c_i_profile_unavailable},
    "rise":    {"name":"Rise Kisaki",      "available": c_i_profile_hidden},
    "setsuna": {"name":"Setsuna Hori",     "available": c_i_profile_unavailable},
    "shoma":   {"name":"Shoma Nishimoto",  "available": c_i_profile_hidden},
    "taiga":   {"name":"Taiga Sakurai",    "available": c_i_profile_hidden},
    "yoku":    {"name":"Yoku Teki",        "available": c_i_profile_hidden}
}

define i_profile_layouts = {
    1: {"y":-0.69, "y2": 0.21},
    2: {"y":-0.52, "y2": 0.38},
    3: {"y":-0.35, "y2": 0.55},
    4: {"y":-0.18, "y2": 0.72}
}

# Progress
default investigation_solve = False
default current_chapter = None
define current_i_page = 1

label investigation_board:

    $ investigation_first_enter = True
    $ clipboard_opened_state = False

    $ temp_culprit_list = False

    call investigation_check
    call screen investigation_board()

label investigation_check:
    python:
        investigation_solve = all(
            data["discovered"] is True
            for page, panels in i_chapter_layouts[current_chapter].items()
            for panel, data in panels.items()
        )

    return

label investigation_unlock:
    $ investigation_first_enter = True
    $ clipboard_opened_state = False

    $ temp_culprit_list = False

    show screen investigation_board()
    call screen block_interaction()

    hide screen investigation_board
    
    return

screen block_interaction():
    modal True
    imagebutton:
        idle "#00000000"
        hover "#00000000"
        action Return()

screen investigation_board():

    modal False

    image "#FFFFFF"

    image "images/Interactables/Manga Background.png":
        xpos 0.5
        xanchor 0.5

    for panels, data in i_chapter_layouts[current_chapter][current_i_page].items():
    
        $ new_image = data["image"]

        # REorganize layout by each slot -> 1 image only

        image new_image:
            xpos 0.5
            xanchor 0.5
            at panel_transforms(data["state"])

    textbutton "O":
        xpos 0.7625
        ypos 0.7125
        xanchor 0.5
        yanchor 0.5
        text_size 55
        if current_i_page == 1:
            action SetVariable("current_i_page", 2), renpy.restart_interaction
        else:
            action SetVariable("current_i_page", 1), renpy.restart_interaction

    textbutton "S O L V E":
        xpos 0.5
        ypos 0.85
        xanchor 0.5
        yanchor 0.5
        text_size 55
        if investigation_solve:
            action SetVariable("temp_culprit_list", True), renpy.restart_interaction

    if temp_culprit_list:
        vbox:
            xpos 1.0
            ypos 0.5
            xanchor 0.1
            yanchor 0.5

            for character, data in i_profile_list.items():
                textbutton data["name"]:
                    xanchor 1.0
                    yanchor 0.5
                    text_size 50
                    action Jump("chapter1_investigation_fail")
                    if character == "mariko":
                        action Jump("chapter1_interrogation")

    use investigation_board_interactives

screen investigation_board_interactives():
    # buttons and clipboards

    # For Closing Animation
    #default clipboard_reset = True

    # Profile Variables
    default profile_count = None
    default profile_position = None
    default profile_y = None
    default profile_y2 = None
    default new_image = None

    default start = None
    default end = None

    image "images/Interactables/clipboard.png":
        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 1.0
        if not investigation_first_enter:
            at (vertical_slide(0.1, 1.0, 1.5) if clipboard_opened_state else vertical_slide(1.0, 0.1, 1.5))

    imagebutton:
        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 1.0
        focus_mask True
        idle "clipboard_idle"
        hover "clipboard_hover"

        action [
            If(clipboard_opened_state,
                false = SetVariable("profile_page", 1)
            ),

            ToggleVariable("clipboard_opened_state"), SetVariable("investigation_first_enter", False), SetVariable("profile_animation_lock", False),
            
            renpy.restart_interaction
        ]

        if not investigation_first_enter:
            at (vertical_slide(0.1, 1.0, 1.5) if clipboard_opened_state else vertical_slide(1.0, 0.1, 1.5))

    for tab, data in i_tab_layouts.items():
        imagebutton:
            xpos 0.5
            ypos 0.1
            xanchor 0.5
            yanchor 1.0

            focus_mask True
            idle data["idle"]
            hover data["hovered"]
            insensitive data["selected"]

            if profile_page is not data["number"]:
                action SetVariable("profile_page", data["number"]), SetVariable("profile_animation_lock", True), renpy.restart_interaction

            if not investigation_first_enter:
                at (vertical_slide(0.1, 1.0, 1.5) if clipboard_opened_state else vertical_slide(1.0, 0.1, 1.5))

    $ profile_count = 0
    $ start = (profile_page - 1) * 4
    $ end = profile_page * 4

    for name, data in i_profile_list.items():
        $ profile_count += 1
        if start < profile_count <= end:
            $ profile_position = ((profile_count - 1) % 4) + 1
            $ profile_y = i_profile_layouts[profile_position]["y"]
            $ profile_y2 = i_profile_layouts[profile_position]["y2"]
            
            if data["available"] is c_i_profile_available:
                $ new_image = "i_profile_" + "[name]"
            elif data["available"] is c_i_profile_unavailable:
                $ new_image = "i_profile_" + "[name]" + "_inactive"
            else:
                $ new_image = "i_profile_" + "[name]" + "_hidden"

            image new_image:
                xpos 608
                if clipboard_opened_state:
                    ypos profile_y2
                else:
                    ypos profile_y
                xanchor 0.0
                yanchor 0.5

                if not investigation_first_enter:
                    at (vertical_slide(profile_y, profile_y2, 1.5) if clipboard_opened_state else vertical_slide(profile_y2, profile_y, 1.5))
                
                if profile_animation_lock:
                    at None

            textbutton data["name"]:
                xpos 1344
                if clipboard_opened_state:
                    ypos profile_y2
                else:
                    ypos profile_y
                xanchor 1.0
                yanchor 0.5
                text_size 60

                if data["available"] is c_i_profile_available:
                    action Jump(f"chapter{current_chapter}_investigation_{name}")
                else:
                    action None

                if not investigation_first_enter:
                    at (vertical_slide(profile_y, profile_y2, 1.5) if clipboard_opened_state else vertical_slide(profile_y2, profile_y, 1.5))
                
                if profile_animation_lock:
                    at None

transform reveal_panel:
    matrixcolor TintMatrix("#000000FF")
    easein 2.0 matrixcolor TintMatrix("#00000000")

transform vertical_slide(h_initial=0.0,h_dest=0.0,delta=0.0):
    ypos h_initial
    easein delta ypos h_dest