import maya.cmds as cmds

def body_creation_function(tx,ty,tz,sx,sy,sz):
    cmds.select(clear=True)
    cmds.polyCube(name='car_body')
    cmds.setAttr('car_body.t', tx, ty, tz, typ='double3')
    cmds.setAttr('car_body.s', sx, sy, sz, typ='double3')

def duplicate_function():
    sel = cmds.ls(sl=True)
    cmds.duplicate(sel)


def resize_duplicated_body_function(tx,ty,tz,sx,sy,sz):
    sel = cmds.ls(sl=True)
    cmds.setAttr('{}.t'.format(sel[0]), tx, ty, tz, type='double3')
    cmds.setAttr('{}.s'.format(sel[0]), sx, sy, sz, typ='double3')
    
if __name__ == "__main__":
    body_creation_function(0,1,0,5.7,0.5,8)
    duplicate_function()
    resize_duplicated_body_function(0,2.067,0,4.579,1.745,5.393)
    cmds.select(clear=True)



