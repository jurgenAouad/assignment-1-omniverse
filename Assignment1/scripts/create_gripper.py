from pxr import Usd, UsdGeom
#1.path
file_path  = "C:/Users/test/Documents/Assignment1/usda/gripper.usda"

#2.create new stage
stage = Usd.Stage.CreateNew(file_path)

#3.define transform
xform  = UsdGeom.Xform.Define(stage, "/Gripper")

#4.define sphere
sph    = UsdGeom.Sphere.Define(stage, "/Gripper/Sphere")

#5.set sphere attributes 
sph.GetRadiusAttr().Set(0.2)

#save
stage.GetRootLayer().Save()

