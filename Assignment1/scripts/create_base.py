
from pxr import Usd, UsdGeom

# 1. path
file_path   = "C:/Users/test/Documents/Assignment1/usda/base.usda"


# 2. Create a new stage 
stage = Usd.Stage.CreateNew(file_path)

# 4. Define a Cylinder prim at path /Base
cyl = UsdGeom.Cylinder.Define(stage, "/Base")

# 5. Set dimensions
cyl.GetHeightAttr().Set(0.2)
cyl.GetRadiusAttr().Set(0.5)

# 6. Save to disk and confirm
stage.GetRootLayer().Save()

