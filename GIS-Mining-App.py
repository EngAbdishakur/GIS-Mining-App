from osgeo import gdal
import matplotlib.pyplot as plt

# Replace 'path_to_your_geotiff_file.tif' with the actual path to your GeoTIFF file
file_path = 'path_to_your_geotiff_file.tif'

# Open the dataset
dataset = gdal.Open(file_path)

# Read raster data
data = dataset.ReadAsArray()

# Get raster information
geotransform = dataset.GetGeoTransform()
projection = dataset.GetProjection()

# Visualize raster data
plt.imshow(data, cmap='viridis')
plt.colorbar(label='Value')
plt.title('Spatial Mining Data Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
#Replace 'path_to_your_geotiff_file.tif' with the actual file path of your GeoTIFF file. This code snippet utilizes GDAL to open and read the raster data from the GeoTIFF file and then visualizes it using Matplotlib.
