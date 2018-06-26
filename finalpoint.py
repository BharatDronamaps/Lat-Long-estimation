from osgeo import gdal
import numpy as np
from pyproj import Proj, transform

Filepath_Filter = 'E:/DronaMaps/20062018/imgs/out.csv'

# Open tif file
dataset = gdal.Open("Orthomosaic_export.tif")
# GDAL affine transform parameters, According to gdal
# documentation xoff/yoff are image left corner,
# a/e are pixel wight/height and b/d is rotation
# and is zero if image is north up.

##print("Driver: {}/{}".format(dataset.GetDriver().ShortName,
##                             dataset.GetDriver().LongName))
##print("Size is {} x {} x {}".format(dataset.RasterXSize,
##                                    dataset.RasterYSize,
##                                    dataset.RasterCount))
##print("Projection is {}".format(dataset.GetProjection()))
##geotransform = dataset.GetGeoTransform()
##if geotransform:
##    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
##    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))

## Extract file

xoff, a, b, yoff, d, e = dataset.GetGeoTransform()

def pixel2coord(x, y):
    """Returns global coordinates from pixel x, y coords"""
    xp = a * x + b * y + xoff
    yp = d * x + e * y + yoff
    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x1,y1 = transform(inProj, outProj, xp, yp)
    return(x1, y1)


# get columns and rows of your image from gdalinfo
rows = 3059
colms = 5754

##for row in  range(0,rows):
##    for col in  range(0,colms):
##        print pixel2coord(col,row)

print pixel2coord(3059, 5754)
print pixel2coord(3058 ,5755)
print pixel2coord(3057, 5756)
print pixel2coord(3057 ,5757)
print pixel2coord(3057, 5758)
print pixel2coord(3056, 5759)
print pixel2coord(3055, 5760)
print pixel2coord(3054, 5761)
print pixel2coord(3053, 5762)
print pixel2coord(3053, 5763)
print pixel2coord(3053, 5764)
print pixel2coord(3053, 5765)
print pixel2coord(3053, 5766)
print pixel2coord(3053, 5767)
print pixel2coord(3053, 5768)
print pixel2coord(3053, 5769)
print pixel2coord(3052, 5770)
print pixel2coord(3051, 5770)
print pixel2coord(3051, 5771)
print pixel2coord(3051, 5772)
print pixel2coord(3050, 5773)
print pixel2coord(3050, 5774)
print pixel2coord(3049, 5775)
print pixel2coord(3049, 5776)
print pixel2coord(3048, 5777)
print pixel2coord(3047, 5777)
print pixel2coord(3046, 5777)
print pixel2coord(3045, 5777)
print pixel2coord(3044, 5777)
print pixel2coord(3043, 5777)
print pixel2coord(3042, 5777)
print pixel2coord(3041, 5777)
print pixel2coord(3040, 5777)
print pixel2coord(3039, 5776)

print pixel2coord(3038, 5776)
print pixel2coord(3037, 5775)
print pixel2coord(3036, 5775)
print pixel2coord(3035, 5774)
print pixel2coord(3034, 5774)
print pixel2coord(3033, 5773)
print pixel2coord(3032, 5773)
print pixel2coord(3031, 5772)
print pixel2coord(3030, 5772)
print pixel2coord(3029, 5771)
print pixel2coord(3028, 5771)
print pixel2coord(3027, 5770)
print pixel2coord(3026, 5770)
print pixel2coord(3025, 5769)
print pixel2coord(3024, 5769)
print pixel2coord(3023, 5768)
print pixel2coord(3022, 5768)
print pixel2coord(3023, 5768)
print pixel2coord(3024, 5769)
print pixel2coord(3025, 5769)
print pixel2coord(3026, 5770)
print pixel2coord(3027, 5770)
print pixel2coord(3028, 5771)
print pixel2coord(3029, 5771)
print pixel2coord(3030, 5772)
print pixel2coord(3031, 5772)
print pixel2coord(3032, 5773)
print pixel2coord(3033, 5773)
print pixel2coord(3034, 5774)
print pixel2coord(3035, 5774)
print pixel2coord(3036, 5775)
print pixel2coord(3037, 5775)
print pixel2coord(3038, 5776)
print pixel2coord(3039, 5776)

print pixel2coord(3040, 5777)
print pixel2coord(3041, 5777)
print pixel2coord(3042, 5778)
print pixel2coord(3043, 5778)
print pixel2coord(3044, 5779)
print pixel2coord(3045, 5779)
print pixel2coord(3046, 5780)
print pixel2coord(3047, 5780)
print pixel2coord(3048, 5780)
print pixel2coord(3048, 5779)
print pixel2coord(3048, 5778)
print pixel2coord(3049, 5777)
print pixel2coord(3049, 5776)
print pixel2coord(3050, 5775)
print pixel2coord(3050, 5774)
print pixel2coord(3050, 5773)
print pixel2coord(3051, 5772)
print pixel2coord(3051, 5771)
print pixel2coord(3052, 5770)
print pixel2coord(3053, 5770)
print pixel2coord(3053, 5769)
print pixel2coord(3053, 5768)
print pixel2coord(3054, 5767)
print pixel2coord(3054, 5766)
print pixel2coord(3054, 5765)
print pixel2coord(3054, 5764)
print pixel2coord(3054, 5763)
print pixel2coord(3054, 5762)
print pixel2coord(3055, 5761)
print pixel2coord(3056, 5760)
print pixel2coord(3057, 5759)
print pixel2coord(3057, 5758)
print pixel2coord(3057, 5757)
print pixel2coord(3058, 5756)
print pixel2coord(3059, 5755)

print pixel2coord(593, 2230)

