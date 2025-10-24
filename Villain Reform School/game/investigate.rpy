default reveal_flag1 = False
default reveal_flag2 = False
default reveal_flag3 = False
default reveal_flag4 = False
default reveal_flag5 = False
default reveal1 = False
default reveal2 = False
default reveal3 = False
default reveal4 = False
default reveal5 = False

default clipboard = True

define temporary_investigation_flashback = False

init python:
    class Profile:
        def __init__(self, Identifier, Name, Order):
            self._Identifier = Identifier
            self._Name = Name
            self._Order = Order
            self._Show = False

        @property
        def ID(self):
            return self._Identifier
        
        @property
        def Name(self):
            return self._Name

        @property
        def Order(self):
            return self._Order

        @property
        def Visibility(self):
            return self._Show

        @Visibility.setter
        def SetVisibility(self, value):
            if value is True or value is False:
                self._Show = value
            else:
                raise ValueError("Cannot be a value other than True or False.")

define profile_kazz = Profile("kazz", "Kazz Kataki", 0)
define profile_momoko = Profile("momoko", "Momoko Yoshino", 1)
define profile_mariko = Profile("mariko", "Mariko Genki", 2)
define profile_chisei = Profile("chisei", "Chisei Jikoma", 3)
define profile_setsuna = Profile("setsuna", "Setsuna Hori", 4)
define profile_dyre = Profile("dyre", "Dyre Okami", 5)
define profile_kitsune = Profile("kitsune", "Kitsune Sumizome", 6)
define profile_rei = Profile("rei", "Rei Watabe", 7)
define profile_ichita = Profile("ichita", "Ichita Kinoshita", 8)
define profile_mu = Profile("mu", "Oshin Murakami", 9)

default all_clipboard_profiles = []
default clipboard_profiles = []
default profile_count = 0
default profile_tab = 0

# call investigation_profile_set(profile_mariko, True)

label profile_cards_setup:

    $ all_clipboard_profiles = [profile_kazz, profile_momoko, profile_mariko, profile_chisei, profile_setsuna, profile_dyre, profile_kitsune, profile_rei, profile_ichita, profile_mu]
    $ clipboard_profiles = []

    return

label investigation_profile_set(object, value = False):

    $ all_clipboard_profiles[all_clipboard_profiles.index(object)].SetVisibility = value

    return


label investigation_progress_update:

    # Reset clipboard animation
    $ clipboard = True
    $ temporary_investigation_flashback = True

    show screen investigate

    window hide
    pause

    hide screen investigate

    $ temporary_investigation_flashback = False

    return

label investigation_interaction_mode:

    call screen investigate

label investigation_interaction_clipboard_mode:

    show screen investigate
    call screen clipboard

screen investigate():
    modal False

    image "#FFFFFF"

    textbutton "?":
        xpos 0.5
        ypos 0.85
        xanchor 0.5
        yanchor 0.5
        text_size 55

    if temporary_investigation_flashback is False:
        textbutton "Back":
            xpos 0.1
            ypos 0.1
            xanchor 0.5
            yanchor 0.5
            text_size 55
            action Jump("chapter1_freetime")

    image "images/Interactables/Manga Background.png":
        xpos 0.5
        xanchor 0.5

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Interactables/Manga_Ch1_Panel_1.png"
        hover "images/Interactables/Manga_Ch1_Panel_1.png"
        #if reveal1 is False:
        #    foreground "images/Clues/Manga_Ch1_Panel_1black.png"
        #action SetVariable("reveal1", not reveal1), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Interactables/Manga_Ch1_Panel_2.png"
        hover "images/Interactables/Manga_Ch1_Panel_2.png"
        #if reveal2 is False:
        #    foreground "images/Clues/Manga_Ch1_Panel_2black.png"
        #action SetVariable("reveal2", not reveal2), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Interactables/Manga_Ch1_Panel_3.png"
        hover "images/Interactables/Manga_Ch1_Panel_3.png"
        #if reveal3 is False:
        #    foreground "images/Clues/Manga_Ch1_Panel_3black.png"
        #action SetVariable("reveal3", not reveal3), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Interactables/Manga_Ch1_Panel_4.png"
        hover "images/Interactables/Manga_Ch1_Panel_4.png"
        #if reveal4 is False:
        #    foreground "images/Clues/Manga_Ch1_Panel_4black.png"
        #action SetVariable("reveal4", not reveal4), renpy.restart_interaction

    imagebutton:
        xpos 0.5
        xanchor 0.5
        focus_mask True
        idle "images/Interactables/Manga_Ch1_Panel_5.png"
        hover "images/Interactables/Manga_Ch1_Panel_5.png"
        #if reveal5 is False:
        #    foreground "images/Clues/Manga_Ch1_Panel_5black.png"
        #action SetVariable("reveal5", not reveal5), renpy.restart_interaction

    if reveal1 is False:
        image "images/Interactables/Manga_Ch1_Panel_1black.png":
            xpos 0.5
            xanchor 0.5
            if reveal_flag1 is True:
                at ch1_inv_img_1

    if reveal2 is False:
        image "images/Interactables/Manga_Ch1_Panel_2black.png":
            xpos 0.5
            xanchor 0.5
            if reveal_flag2 is True:
                at ch1_inv_img_2

    if reveal3 is False:
        image "images/Interactables/Manga_Ch1_Panel_3black.png":
            xpos 0.5
            xanchor 0.5
            if reveal_flag3 is True:
                at ch1_inv_img_3

    if reveal4 is False:
        image "images/Interactables/Manga_Ch1_Panel_4black.png":
            xpos 0.5
            xanchor 0.5
            if reveal_flag4 is True:
                at ch1_inv_img_4
            
    if reveal5 is False:
        image "images/Interactables/Manga_Ch1_Panel_5black.png":
            xpos 0.5
            xanchor 0.5
            if reveal_flag5 is True:
                at ch1_inv_img_5
    if temporary_investigation_flashback is False:
        imagebutton:
            xpos 0.5
            ypos 0.1
            xanchor 0.5
            yanchor 1.0
            focus_mask True
            idle "images/Interactables/clipboard.png"
            hover "images/Interactables/clipboard.png"
            if clipboard is False:
                at clipboard_slide_up
            action SetVariable("clipboard", True), Jump("investigation_interaction_clipboard_mode")
    
        $ profile_count = 0
        $ clipboard_profiles.clear()
    
        for profile in all_clipboard_profiles:
            if (profile.Visibility is True):
                $ clipboard_profiles.append(profile)
                $ profile_count += 1
    
        $ profile_tracker = 4 * profile_tab
    
        if (profile_tracker < profile_count):
            image f"images/Interactables/{clipboard_profiles[profile_tracker].ID}profile.png":
                xpos 608
                ypos -0.69
                xanchor 0.0
                yanchor 0.5
    
                if clipboard is False:
                    at profile_1_slide_up
    
            text f"{clipboard_profiles[profile_tracker].Name}":
                xpos 1338
                ypos -0.69
                xanchor 1.0
                yanchor 0.5
                size 60
                font "true-crimes.ttf"
                color '#888888'
    
                if clipboard is False:
                    at profile_1_slide_up
    
        if (profile_tracker + 1 < profile_count):
            image f"images/Interactables/{clipboard_profiles[profile_tracker + 1].ID}profile.png":
                xpos 608
                ypos -0.52
                xanchor 0.0
                yanchor 0.5
    
                if clipboard is False:
                    at profile_2_slide_up
    
            text f"{clipboard_profiles[profile_tracker + 1].Name}":
                xpos 1338
                ypos -0.52
                xanchor 1.0
                yanchor 0.5
                size 60
                font "true-crimes.ttf"
                color '#888888'
    
                if clipboard is False:
                    at profile_2_slide_up
    
        if (profile_tracker + 2 < profile_count):
            image f"images/Interactables/{clipboard_profiles[profile_tracker + 2].ID}profile.png":
                xpos 608
                ypos -0.35
                xanchor 0.0
                yanchor 0.5
    
                if clipboard is False:
                    at profile_3_slide_up
    
            text f"{clipboard_profiles[profile_tracker + 2].Name}":
                xpos 1338
                ypos -0.35
                xanchor 1.0
                yanchor 0.5
                size 60
                font "true-crimes.ttf"
                color '#888888'
    
                if clipboard is False:
                    at profile_3_slide_up
    
        if (profile_tracker + 3 < profile_count):
            image f"images/Interactables/{clipboard_profiles[profile_tracker + 3].ID}profile.png":
                xpos 608
                ypos -0.18
                xanchor 0.0
                yanchor 0.5
    
                if clipboard is False:
                    at profile_4_slide_up
    
            text f"{clipboard_profiles[profile_tracker + 3].Name}":
                xpos 1338
                ypos -0.18
                xanchor 1.0
                yanchor 0.5
                size 60
                font "true-crimes.ttf"
                color '#888888'
    
                if clipboard is False:
                    at profile_4_slide_up
    
        $ profile_tab = 0

screen clipboard():

    modal True

    textbutton "Back":
        xpos 0.1
        ypos 0.1
        xanchor 0.5
        yanchor 0.5
        text_size 55
        action SetVariable("clipboard", False), ui.ChoiceJump("Interaction", "investigation_interaction_mode"), Hide("investigate")

    frame:

        background None

        image "images/Interactables/clipboard.png"

        xpos 0.5
        ypos 0.1
        xanchor 0.5
        yanchor 1.0

        if clipboard is True:
            at clipboard_slide_down

    $ profile_count = 0
    $ clipboard_profiles.clear()

    for profile in all_clipboard_profiles:
        if (profile.Visibility is True):
            $ clipboard_profiles.append(profile)
            $ profile_count += 1

    $ profile_tracker = 4 * profile_tab

    if (profile_tracker < profile_count):
        image f"images/Interactables/{clipboard_profiles[profile_tracker].ID}profile.png":
            xpos 608
            ypos 0.21
            xanchor 0.0
            yanchor 0.5

            if clipboard is True:
                at profile_1_slide_down

        textbutton f"{clipboard_profiles[profile_tracker].Name}":
            xpos 1344
            ypos 0.21
            xanchor 1.0
            yanchor 0.5
            text_size 60
            action Hide("investigate"), Jump(f"chapter1_investigation_{clipboard_profiles[profile_tracker].ID}")
            
            if clipboard is True:
                at profile_1_slide_down

    if (profile_tracker + 1 < profile_count):
        image f"images/Interactables/{clipboard_profiles[profile_tracker + 1].ID}profile.png":
            xpos 608
            ypos 0.38
            xanchor 0.0
            yanchor 0.5

            if clipboard is True:
                at profile_2_slide_down

        textbutton f"{clipboard_profiles[profile_tracker + 1].Name}":
            xpos 1344
            ypos 0.38
            xanchor 1.0
            yanchor 0.5
            text_size 60
            action Hide("investigate"), Jump(f"chapter1_investigation_{clipboard_profiles[profile_tracker + 1].ID}")
            
            if clipboard is True:
                at profile_2_slide_down

    if (profile_tracker + 2 < profile_count):
        image f"images/Interactables/{clipboard_profiles[profile_tracker + 2].ID}profile.png":
            xpos 608
            ypos 0.55
            xanchor 0.0
            yanchor 0.5

            if clipboard is True:
                at profile_3_slide_down

        textbutton f"{clipboard_profiles[profile_tracker + 2].Name}":
            xpos 1344
            ypos 0.55
            xanchor 1.0
            yanchor 0.5
            text_size 60
            action Hide("investigate"), Jump(f"chapter1_investigation_{clipboard_profiles[profile_tracker + 2].ID}")
            
            if clipboard is True:
                at profile_3_slide_down

    if (profile_tracker + 3 < profile_count):
        image f"images/Interactables/{clipboard_profiles[profile_tracker + 3].ID}profile.png":
            xpos 608
            ypos 0.72
            xanchor 0.0
            yanchor 0.5

            if clipboard is True:
                at profile_4_slide_down

        textbutton f"{clipboard_profiles[profile_tracker + 3].Name}":
            xpos 1344
            ypos 0.72
            xanchor 1.0
            yanchor 0.5
            text_size 60
            action Hide("investigate"), Jump(f"chapter1_investigation_{clipboard_profiles[profile_tracker + 3].ID}")
            
            if clipboard is True:
                at profile_4_slide_down


transform ch1_inv_img_1:
    alpha 1.0
    easein 2.0 alpha 0.0

transform ch1_inv_img_2:
    alpha 1.0
    easein 2.0 alpha 0.0

transform ch1_inv_img_3:
    alpha 1.0
    easein 2.0 alpha 0.0

transform ch1_inv_img_4:
    alpha 1.0
    easein 2.0 alpha 0.0

transform ch1_inv_img_5:
    alpha 1.0
    easein 2.0 alpha 0.0

transform clipboard_slide_down:
    ypos 0.1
    easein 1.5 ypos 1.0

transform clipboard_slide_up:
    ypos 1.0
    easein 1.5 ypos 0.1

transform profile_1_slide_down:
    ypos -0.69
    easein 1.5 ypos 0.21

transform profile_1_slide_up:
    ypos 0.21
    easein 1.5 ypos -0.69

transform profile_2_slide_down:
    ypos -0.52
    easein 1.5 ypos 0.38

transform profile_2_slide_up:
    ypos 0.38
    easein 1.5 ypos -0.52

transform profile_3_slide_down:
    ypos -0.35
    easein 1.5 ypos 0.55

transform profile_3_slide_up:
    ypos 0.55
    easein 1.5 ypos -0.35

transform profile_4_slide_down:
    ypos -0.18
    easein 1.5 ypos 0.72

transform profile_4_slide_up:
    ypos 0.72
    easein 1.5 ypos -0.18