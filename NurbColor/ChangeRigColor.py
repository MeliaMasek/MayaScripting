import maya.cmds as cmds

#Colors are from 0-31
#red 13, blue 6, green 14, yellow 18
def ChangeColor(ColorInt):
    selection = cmds.ls(selection = True)

    for select in selection:
        cmds.setAttr(select + ".overrideEnabled", True)
        cmds.setAttr(select + ".overrideColor", ColorInt)
ChangeColor(13)



#function for color change with names, notes from class
#def ChangeNurbColor(color):
#       if color == "red":
#           color  = 13
#       if color > 31:
#           color = 0
#       else:
#           color == 0
#ChangeColor("red")

