import maya.cmds as cmds

def change_color(color_int):
    selection = cmds.ls(selection=True)

    for select in selection:
        cmds.setAttr(select + ".overrideEnabled", True)
        cmds.setAttr(select + ".overrideColor", color_int)

def create_color_change_ui():
    if cmds.window("colorChangeWindow", exists=True):
        cmds.deleteUI("colorChangeWindow", window=True)

    window = cmds.window("colorChangeWindow", title="Change Object Color")
    cmds.columnLayout(adjustableColumn=True)
    
    # Header for Control Color section
    cmds.text(label="Control Color", align="center", font="boldLabelFont")

    cmds.text(label="Select a color to change object(s) color:")
    cmds.button(label="Red", command=lambda *args: change_color(13))
    cmds.button(label="Blue", command=lambda *args: change_color(6))
    cmds.button(label="Green", command=lambda *args: change_color(14))
    cmds.button(label="Yellow", command=lambda *args: change_color(17)) # Changed to 17 for yellow

    # Separator
    cmds.separator(style='single')

    # Header for Animation section
    cmds.text(label="Animation", align="center", font="boldLabelFont")

    cmds.button(label="Create Keyframes Every 25 Frames", command=create_keyframes_every_25_frames)

    # Separator
    cmds.separator(style='single')

    # Header for Broken FK section
    cmds.text(label="Broken FK", align="center", font="boldLabelFont")

    cmds.button(label="Create Parent and Scale Constraints", command=create_parent_child_controls)

    cmds.showWindow(window)

def create_keyframes_every_25_frames():
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)
    
    # Check if there are any selected objects
    if not selected_objects:
        cmds.warning("No objects selected. Please select at least one object.")
        return
    
    # Get the current timeline range
    start_frame = cmds.playbackOptions(q=True, min=True)
    end_frame = cmds.playbackOptions(q=True, max=True)
    
    # Create keyframes every 25 frames for each selected object
    for obj in selected_objects:
        for frame in range(int(start_frame), int(end_frame) + 1, 25):
            cmds.setKeyframe(obj, time=frame)

def create_parent_child_controls():
    # Get selection, separate parent control and child control
    sels = cmds.ls(sl=True)  # [parent control, child control]
    if len(sels) != 2:
        cmds.warning("Please select exactly 2 objects.")
        return
    parent_ctrl = sels[0]
    child_ctrl = sels[1]

    # Get parent group of the child control
    child_ctrl_grp = cmds.listRelatives(child_ctrl, parent=True)[0]  # [child control's parent node]

    # Create constraints
    p_constraint1 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipRotate=['x', 'y', 'z'], weight=1)[0]  # Constraints translate
    p_constraint2 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipTranslate=['x', 'y', 'z'], weight=1)[0]  # Constraints rotate
    cmds.scaleConstraint(parent_ctrl, child_ctrl_grp, weight=1)

    # Create attributes on the child control
    if not cmds.attributeQuery('FollowTranslate', node=child_ctrl, exists=True):
        cmds.addAttr(child_ctrl, ln='FollowTranslate', at='double', min=0, max=1, dv=1)
        cmds.setAttr('%s.FollowTranslate' % (child_ctrl), e=True, keyable=True)
    if not cmds.attributeQuery('FollowRotate', node=child_ctrl, exists=True):
        cmds.addAttr(child_ctrl, ln='FollowRotate', at='double', min=0, max=1, dv=1)
        cmds.setAttr('%s.FollowRotate' % (child_ctrl), e=True, keyable=True)

    # Connect attributes from child control to constraint weights
    cmds.connectAttr('%s.FollowTranslate' % (child_ctrl), '%s.w0' %(p_constraint1), f=True)
    cmds.connectAttr('%s.FollowRotate' % (child_ctrl), '%s.w0' %(p_constraint2), f=True)

# Call the function to create the color change UI
create_color_change_ui()
