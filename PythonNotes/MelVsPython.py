import maya.cmds as cmds

sels = cmds.ls(selection=True)
sel = sels[0]

pos = cmds.xform(sel, q=True, ws=True, rotatePivot=True)

loc = cmds.spaceLocator(p=(0, 0, 0))[0]
#loc = locs[0]

cmds.xform(loc, ws=True, translation=pos)