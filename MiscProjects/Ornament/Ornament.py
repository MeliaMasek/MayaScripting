import maya.cmds as cmds

#Creates Ornanament
cmds.polySphere(sx=18, sy=15, r=5)
cmds.scale(1, 0.668207, 1, r=True)

cmds.polySelect('pSphere1', edgeRing=18)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=17)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=16)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=15)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=14)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=13)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=12)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=11)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=10)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=9)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=8)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=7)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=6)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=5)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=4)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=3)
cmds.scale(1.2, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=2)
cmds.scale(.8, 0.85, 0.85, r=True)
cmds.polySelect('pSphere1', edgeRing=1)
cmds.scale(1.2, 0.85, 0.85, r=True)

#Creates hook
cmds.polyTorus( sx=15, sy=15, r=1, sr=.35)
cmds.move(0, 3.40, 0, r=True)
cmds.rotate(-90, 0, 0, r=True, os=True, fo=True,)
cmds.scale(1, 0.612283, 1, r=True)





