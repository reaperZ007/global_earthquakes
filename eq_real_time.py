import requests
import json
import plotly.express as px

# Fetch real-time earthquake data from USGS API
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

try:
    response = requests.get(url, timeout=10)  # Set a timeout for network stability
    response.raise_for_status()  # Raise an error if the request fails
    data = response.json()  # Parse JSON response
except requests.exceptions.RequestException as e:
    print("Error fetching earthquake data:", e)
    exit()

# Ensure data contains features
if "features" not in data:
    print("Invalid data format: 'features' key not found.")
    exit()

# Extract earthquake details
all_eq_dicts = data["features"]
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    try:
        mag = eq_dict["properties"]["mag"]
        lon = eq_dict["geometry"]["coordinates"][0]
        lat = eq_dict["geometry"]["coordinates"][1]
        eq_title = eq_dict["properties"]["title"]

        # Check for missing or invalid values
        if mag is not None and lon is not None and lat is not None:
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
            eq_titles.append(eq_title)
    except (KeyError, TypeError, IndexError) as e:
        print(f"Skipping invalid earthquake entry: {e}")

# Ensure there is data to plot
if not mags:
    print("No valid earthquake data available.")
    exit()

# Create a scatter map of the earthquakes
title = "Real-Time Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=[max(m, 0.1) for m in mags],  # Ensure size is non-zero
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)

# Show the map
fig.show()

"""
Key Fixes and Improvements:
✅ Added Exception Handling → Catches network errors, missing data, or JSON issues.
✅ Prevents Zero-Size Markers → Ensures all points have a visible size.
✅ Handles Missing Data → Skips entries with missing latitude, longitude, or magnitude.
✅ Ensures features Key Exists → Prevents crashes if API response format changes."""