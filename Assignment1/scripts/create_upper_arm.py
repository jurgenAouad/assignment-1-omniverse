
from pxr import Usd, UsdGeom
#1.path
file_path  = "C:/Users/test/Documents/Assignment1/usda/upper_arm.usda"

#2.create new stage
stage = Usd.Stage.CreateNew(file_path)

#3.define transform
xform = UsdGeom.Xform.Define(stage, "/UpperArm")

#4.define cube
cube  = UsdGeom.Cube.Define(stage, "/UpperArm/Cube")

#5.set cube attributes 
cube.GetSizeAttr().Set(1.0)

#6.set scale for xform
UsdGeom.XformCommonAPI(xform).SetScale((0.3, 1.2, 0.3))

#save
stage.GetRootLayer().Save()

