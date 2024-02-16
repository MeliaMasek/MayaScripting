def create_parent_child_controls():
    # Get selection, separate parent control and child control
    sels = cmds.ls(sl=True)  # [parent control, child control]
    if len(sels) != 2:
        cmds.warning("Please select exactly 2 objects.")
        return
    parent_ctrl = sels[0]
    child_ctrl = sels[1]

    # Get parent group of the child control
    parent_group = cmds.listRelatives(child_ctrl, parent=True)
    if not parent_group:
        cmds.warning("The selected child control has no parent group.")
        return
    child_ctrl_grp = parent_group[0]  # [child control's parent node]

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
