import maya.cmds as cmds


def mirror_function():
    selection = cmds.ls(sl=True)
    print(selection)
    for item in selection:
        x = cmds.getAttr('{}.translate'.format(item))
        print(x)
        for tup in x:
            for item in tup:
                print(item)
    if tup[0] and tup[2] >=0:
        print('right_to_left')
        cmds.polyMirrorFace(cm=True, a=0, ad=1, mm=1, mtt=0, mt=0.001,ma=2, mps=0, sa=30, fuv=0, ch=True)
        print('front_to_back')
        cmds.polyMirrorFace(cm=True, a=2, ad=1, mm=1, mtt=0, mt=0.001,ma=2, mps=0, sa=30, fuv=1, ch=True)
    elif tup[0] and tup[2] < 0:
        print('left_to_right')
        cmds.polyMirrorFace(cm=True, a=0, ad=1, mm=1, mtt=0, mt=0.001,ma=2, mps=0, sa=30, fuv=0, ch=True)
        print('back_to_front')
        cmds.polyMirrorFace(cm=True, a=2, ad=0, mm=1, mtt=0, mt=0.001,ma=2, mps=0, sa=30, fuv=1, ch=True)
    cmds.MirrorPolygonGeometry(axisDirection=1)

if __name__ == "__main__":
    mirror_function()




