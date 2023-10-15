import maya.cmds as cmds

#Can't figure out how to get the "doesn't contain #" to function properly with the naming format

def Namer(string):
    selections = cmds.ls(sl=True)

    x = string
    txt = ""
    txt.find("#")
    try:
        x >= 0
        print(x)
    except:
        print("doesn't contain #")

    string.partition("##")
    for count, object in enumerate(selections):
        cmds.rename(object, string.partition('#')[0] + str(count + 1).zfill(string.count('#')) + string.rpartition('#')[2])

Namer("Leg_##_Jnt")
