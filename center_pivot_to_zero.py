import maya.cmds as cmds


def pivot_to_zero_axis(name):
    cmds.move(0, 0, 0, "{}.scalePivot".format(name),"{}.rotatePivot".format(name), absolute=True)


cmds.SelectAll()
selection = cmds.ls(sl=True)
obj_name = selection[0]
pivot_to_zero_axis(obj_name)







