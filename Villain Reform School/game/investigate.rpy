init python:
    def panel_transforms(panel_state):
        if panel_state is c_i_hidden:
            return pitchblack
        elif panel_state is c_i_to_be_revealed:
            return reveal_panel
        elif panel_state is c_i_dual:
            return dual_panel
        else:
            return None

    def set_profile_availability(name, value):
        i_profile_list[name]["available"] = value
        return

    def fake_reveal_panel(page, panel_key, panel_name):
        if panel_name.discovered:
            return
        else:
            panel_name.discovered = True
            current_panel_slot = i_chapter_layouts[current_chapter][page][panel_key]
            
            if current_panel_slot.state is c_i_hidden:
                current_panel_slot.state = c_i_to_be_revealed
            
            if current_panel_slot.discovered_count > 0:
                current_panel_slot.state = c_i_dual
            else:
                current_panel_slot.display = panel_name
            
            current_panel_slot.possible.append(panel_name)
            current_panel_slot.discovered_count += 1

        return

    def real_reveal_panel(page, panel_key):
        current_panel_slot = i_chapter_layouts[current_chapter][page][panel_key]
        if current_panel_slot.state is c_i_to_be_revealed:
            current_panel_slot.state = c_i_revealed
        return

    class PanelSlot:
        def __init__(self):
            self.display = None
            self.possible = []
            self.discovered_count = 0
            self.state = c_i_hidden

        def swap(self):
            position = self.possible.index(self.display)
            position+= 1
            if position == self.discovered_count:
                position = 0
            self.display = self.possible[position]
            return

    class Panel:
        def __init__(self, image):
            self.discovered = False
            self.image = image

# Chapter Constants
define c_chapter_prologue = 0
define c_chapter_one = 1
define c_chapter_two = 2

# Investigation Panels Constants
define c_i_hidden = -1
define c_i_to_be_revealed = 0
define c_i_revealed = 1
define c_i_dual = 2

# Profile States
define c_i_profile_available = 1
define c_i_profile_unavailable = 0
define c_i_profile_hidden = -1

# UI States
define investigation_first_enter = True
define profile_animation_lock = False
default clipboard_opened_state = False
define profile_page = 1

# region UI Elements - Investigation
image clipboard_idle:
    "images/Interactables/clipboard_interactable.png"

image clipboard_hover:
    "images/Interactables/clipboard_interactable.png"
    matrixcolor BrightnessMatrix(0.1)

image page_flaps_idle:
    "images/Interactables/Manga page corners.png"

image page_flaps_hover:
    "images/Interactables/Manga page corners.png"
    matrixcolor ColorizeMatrix("#f00","#ffffff")

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
default ch1_p1panel1 = Panel("images/Interactables/Manga_Ch1_Panel_1.png")
default ch1_p1panel2 = Panel("images/Interactables/Manga_Ch1_Panel_2.png")
default ch1_p1panel3 = Panel("images/Interactables/Manga_Ch1_Panel_3.png")
default ch1_p1panel4 = Panel("images/Interactables/Manga_Ch1_Panel_4.png")
default ch1_p1panel5 = Panel("images/Interactables/Manga_Ch1_Panel_5.png")
default ch1_p1panel6 = Panel("images/Interactables/Manga_Ch1_Panel_6.png")

# Ch 2 Panels
default ch2_p1panel1  = Panel("images/Interactables/Manga_Ch2_Page1_Panel_1.png")
default ch2_p1panel2  = Panel("images/Interactables/Manga_Ch2_Page1_Panel_2.png")
default ch2_p1panel3i = Panel("images/Interactables/Manga_Ch2_Page1_Panel_3_I.png")
default ch2_p1panel3r = Panel("images/Interactables/Manga_Ch2_Page1_Panel_3_R.png")
default ch2_p1panel4  = Panel("images/Interactables/Manga_Ch2_Page1_Panel_4.png")
default ch2_p1panel5  = Panel("images/Interactables/Manga_Ch2_Page1_Panel_5.png")
default ch2_p1panel6i = Panel("images/Interactables/Manga_Ch2_Page1_Panel_6_I.png")
default ch2_p1panel6r = Panel("images/Interactables/Manga_Ch2_Page1_Panel_6_R.png")

default ch2_p2panel1i = Panel("images/Interactables/Manga_Ch2_Page2_Panel_1_I.png")
default ch2_p2panel1r = Panel("images/Interactables/Manga_Ch2_Page2_Panel_1_R.png")
default ch2_p2panel2  = Panel("images/Interactables/Manga_Ch2_Page2_Panel_2.png")
default ch2_p2panel3  = Panel("images/Interactables/Manga_Ch2_Page2_Panel_3.png")
default ch2_p2panel4  = Panel("images/Interactables/Manga_Ch2_Page2_Panel_4.png")
default ch2_p2panel5  = Panel("images/Interactables/Manga_Ch2_Page2_Panel_5.png")
default ch2_p2panel6  = Panel("images/Interactables/Manga_Ch2_Page2_Panel_6.png")

# Ch 3 Panels
# endregion

# region Investigation Layout Rules & Flags
default i_chapter_layouts = {
    c_chapter_one: {
        1: {
            "panel1": PanelSlot(),
            "panel2": PanelSlot(),
            "panel3": PanelSlot(),
            "panel4": PanelSlot(),
            "panel5": PanelSlot(),
            "panel6": PanelSlot()
        }
    },

    c_chapter_two: {
        1: {
            "panel1":  PanelSlot(),
            "panel2":  PanelSlot(),
            "panel3":  PanelSlot(),
            "panel4":  PanelSlot(),
            "panel5":  PanelSlot(),
            "panel6":  PanelSlot()
        },
        2: {
            "panel1":  PanelSlot(),
            "panel2":  PanelSlot(),
            "panel3":  PanelSlot(),
            "panel4":  PanelSlot(),
            "panel5":  PanelSlot(),
            "panel6":  PanelSlot()
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
# endregion

# region Initial Setup
label investigation_initial_preset:
    # Runs once to fill with black panels

    $ current_chapter = 1
    $ current_i_page = 1

    $ i_chapter_layouts[current_chapter][current_i_page]["panel1"].display = ch1_p1panel1
    $ i_chapter_layouts[current_chapter][current_i_page]["panel2"].display = ch1_p1panel2
    $ i_chapter_layouts[current_chapter][current_i_page]["panel3"].display = ch1_p1panel3
    $ i_chapter_layouts[current_chapter][current_i_page]["panel4"].display = ch1_p1panel4
    $ i_chapter_layouts[current_chapter][current_i_page]["panel5"].display = ch1_p1panel5
    $ i_chapter_layouts[current_chapter][current_i_page]["panel6"].display = ch1_p1panel6

    $ current_chapter = 2
    # Page 1

    $ i_chapter_layouts[current_chapter][current_i_page]["panel1"].display = ch2_p1panel1
    $ i_chapter_layouts[current_chapter][current_i_page]["panel2"].display = ch2_p1panel2
    $ i_chapter_layouts[current_chapter][current_i_page]["panel3"].display = ch2_p1panel3r
    $ i_chapter_layouts[current_chapter][current_i_page]["panel4"].display = ch2_p1panel4
    $ i_chapter_layouts[current_chapter][current_i_page]["panel5"].display = ch2_p1panel5
    $ i_chapter_layouts[current_chapter][current_i_page]["panel6"].display = ch2_p1panel6r

    $ current_i_page = 2

    $ i_chapter_layouts[current_chapter][current_i_page]["panel1"].display = ch2_p2panel1r
    $ i_chapter_layouts[current_chapter][current_i_page]["panel2"].display = ch2_p2panel2
    $ i_chapter_layouts[current_chapter][current_i_page]["panel3"].display = ch2_p2panel3
    $ i_chapter_layouts[current_chapter][current_i_page]["panel4"].display = ch2_p2panel4
    $ i_chapter_layouts[current_chapter][current_i_page]["panel5"].display = ch2_p2panel5
    $ i_chapter_layouts[current_chapter][current_i_page]["panel6"].display = ch2_p2panel6

    $ current_chapter = None
    $ current_i_page = 1

    return
# endregion

# Progress
default investigation_solve = False
default current_chapter = None
define current_i_page = 1

label investigation_board:

    scene backgroundwhite

    $ investigation_first_enter = True
    $ clipboard_opened_state = False

    $ current_i_page = 1

    call investigation_check
    call screen investigation_board()

label investigation_check:
    python:
        investigation_solve = all(
            data.discovered_count # Returns False if 0 is found
            for pages, panels in i_chapter_layouts[current_chapter].items()
            for panel, data in panels.items()
        )

    return
# Flashback
label investigation_unlock:
    $ investigation_first_enter = True
    $ clipboard_opened_state = False

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
    
        $ new_image = data.display.image

        imagebutton:
            focus_mask True
            idle new_image
            hover None
            xpos 0.5
            xanchor 0.5
            at panel_transforms(data.state)
            if (data.state == c_i_dual):
                action data.swap, renpy.restart_interaction
            else:
                action None
    
    if current_chapter == 2:
        imagebutton:
            focus_mask True
            idle "page_flaps_idle"
            hover "page_flaps_hover"
            xpos 0.5
            xanchor 0.5
            if current_i_page == 1:
                action SetVariable("current_i_page", 2), renpy.restart_interaction
            else:
                action SetVariable("current_i_page", 1), renpy.restart_interaction

    if eval("chapter" + str(current_chapter) + "_interrogation_chance") == True:
        if investigation_solve:
            textbutton "SOLVE":
                xpos 0.5
                ypos 0.85
                xanchor 0.5
                yanchor 0.5
                text_size 75
                action Jump(f"chapter{current_chapter}_investigation_narration")
    
    elif eval("chapter" + str(current_chapter) + "_solved") == True:
        text "Investigation Solved":
            xpos 0.5
            ypos 0.85
            xanchor 0.5
            yanchor 0.5
            size 55

    else:
        text "Investigation Unsuccessful":
            xpos 0.5
            ypos 0.85
            xanchor 0.5
            yanchor 0.5
            size 55

    use investigation_board_interactives

screen investigation_board_interactives():
    # Clipboard

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

transform dual_panel:
    easein 4.0 matrixcolor BrightnessMatrix(0.1)
    pause 2.0
    easein 4.0 matrixcolor BrightnessMatrix(-0.4)
    pause 2.0
    repeat

transform vertical_slide(h_initial=0.0,h_dest=0.0,delta=0.0):
    ypos h_initial
    easein delta ypos h_dest