from skyfield.api import Loader
from skyfield.data import hipparcos
from fetchStarData import getStarData

# Specify the directory where you want to save the Hipparcos catalog
load = Loader(r"C:\Users\riley\PycharmProjects\Hipparcos")

# Open the Hipparcos catalog URL and load it into a DataFrame
with load.open(hipparcos.URL) as f:
    df = hipparcos.load_dataframe(f)

print("Hipparcos star catalog downloaded successfully.")

# Test the getStarData function
star_id = 12305  # Example star ID
latitude = 40.7128  # Example latitude (New York City)
longitude = -74.0060  # Example longitude (New York City)

star_data = getStarData(star_id, latitude, longitude)
print("Star data:", star_data)
