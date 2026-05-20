transform left_center:
    xanchor 0.5
    xpos 0.25
    ypos 1.0
    yanchor 1.0

transform right_center:
    xanchor 0.5
    xpos 0.75
    ypos 1.0
    yanchor 1.0

#transform brighter_filter:
#    matrixcolor TintMatrix("#FFFFFF88")

transform darker(value = "00000088"):
    matrixcolor TintMatrix(value) * BrightnessMatrix(-0.5)

transform pitchblack:
    matrixcolor TintMatrix("#000000FF")

transform clear:
    matrixcolor TintMatrix("#00000000")

transform brighter:
    matrixcolor BrightnessMatrix(0.1)