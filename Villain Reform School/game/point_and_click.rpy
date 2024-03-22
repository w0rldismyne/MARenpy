default check_book = False
default check_cd = False
default check_mic = False
default check_laptop = False

label mini_game:

    scene backgroundavroom

    while check_book is False or check_cd is False or check_mic is False or check_laptop is False:
        call screen mini_game
        label interaction_complete:
            pass
    
    "Complete"
    return


screen mini_game:

    modal True

    imagebutton:
        idle Null()
        hover "gui/button/announcementlist.png"
        xysize (296, 164)
        xycenter (150, 647)
        action SetVariable("check_book", True), Hide("mini_game"), Jump("mini_game_book")

    imagebutton:
        idle Null()
        hover "gui/button/cds.png"
        xysize (800, 716)
        xycenter (656, 358)
        action SetVariable("check_cd", True), Hide("mini_game"), Jump("mini_game_cd")

    imagebutton:
        idle Null()
        hover "gui/button/microphone.png"
        xysize (368, 371)
        xycenter (1498, 224)
        action SetVariable("check_mic", True), Hide("mini_game"), Jump("mini_game_mic")

    imagebutton:
        idle Null()
        hover "gui/button/laptop.png"
        xysize (398, 323)
        xycenter (1595, 683)
        action SetVariable("check_laptop", True), Hide("mini_game"), Jump("mini_game_laptop")

label mini_game_book:
    "Book Test"
    jump interaction_complete

label mini_game_cd:
    "CD Test"
    jump interaction_complete

label mini_game_mic:
    "Mic Test"
    jump interaction_complete

label mini_game_laptop:
    "Laptop Test"
    jump interaction_complete