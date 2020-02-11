import maya.cmds as cmds
import body_creation_duplication
import mirror_function
import center_pivot_to_zero
import tire_creation


def clear_selection():
    cmds.select(clear=True)

tire_creation_function(3,1,3,90,90,0,0.7,0.2,0.7,1)
mirror_function()
cmds.SelectAll()
selection = cmds.ls(sl=True)
obj_name = selection[0]
pivot_to_zero_axis(obj_name)
pivot_to_zero_axis(obj_name)
cmds.select(clear=True)
body_creation_function(0,1,0,5.7,0.5,8)
duplicate_function()
resize_duplicated_body_function(0,2.067,0,4.579,1.745,5.393)
cmds.select(clear=True)

