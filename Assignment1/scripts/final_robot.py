# final_robot.py
from pxr import Usd, UsdGeom

# 1. Create new “robot.usda” stage
stage = Usd.Stage.CreateNew("C:/Users/test/Documents/Assignment1/usda/robot.usda")

# 2. Define root Xform prim
robot = UsdGeom.Xform.Define(stage, "/Robot")

# 3. Helper: add a reference + wrapper Xform
def addRef(name, filepath, parent, translate=(0,0,0), rotate=(0,0,0), scale=(1,1,1)):
    # a) Create a child Xform under parent
    x = UsdGeom.Xform.Define(stage, f"{parent.GetPath().AppendChild(name)}")
    # b) Reference the external prim (assumes each file has its component at path /<Name>)
    x.GetPrim().GetReferences().AddReference(f"{filepath}", f"/{name}")
    # c) Apply transform ops
    api = UsdGeom.XformCommonAPI(x)
    api.SetTranslate(translate)
    api.SetRotate(rotate)
    api.SetScale(scale)
    return x

# 4. Place Base at the origin
addRef("Base",     "base.usda",     robot, translate=(0,0,0))

# 5. Stack LowerArm on top of Base
addRef("LowerArm", "lower_arm.usda", robot,
       translate=(0, 0.2 + 0.6, 0))

# 6. Stack UpperArm on top of LowerArm
addRef("UpperArm", "upper_arm.usda", robot,
       translate=(0, 1.4 + 0.6, 0),
       rotate=(0, 0, 45))       # e.g. rotate 45° around Z

# 7. Attach Gripper at the tip of UpperArm
addRef("Gripper",  "gripper.usda",  robot,
       translate=(0, 2.0 + 0.2, 0))

# 8. Save!
stage.GetRootLayer().Save()
