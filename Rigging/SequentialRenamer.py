import maya.cmds as cmds

def Namer(string):
    selections = cmds.ls(sl=True)

    if '#' not in string:
        cmds.warning("String doesn't contain '#' symbol.")
        return

    # Split the string into parts before and after the '#' symbol
    prefix, suffix = string.split('#', 1)

    for count, obj in enumerate(selections):
        # Rename each object by replacing '#' with the count
        new_name = f"{prefix}{count+1:0{len(suffix)}}{suffix}"
        cmds.rename(obj, new_name)

# Test the function
Namer("Leg_##_Jnt")
