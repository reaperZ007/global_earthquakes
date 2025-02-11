import requests
import json
import pandas as pd
import plotly.express as px

# Fetch past 30 days of earthquake data
def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching earthquake data:", e)
        return None

# Extract earthquake details
def extract_earthquake_data(data):
    if not data or "features" not in data:
        print("Invalid data format.")
        return pd.DataFrame()  

    earthquake_list = []
    
    for eq_dict in data["features"]:
        try:
            mag = eq_dict["properties"].get("mag", 1.0)  # Default to 1.0 if missing
            lon = eq_dict["geometry"]["coordinates"][0]
            lat = eq_dict["geometry"]["coordinates"][1]
            depth = eq_dict["geometry"]["coordinates"][2]
            eq_title = eq_dict["properties"].get("title", "Unknown Event")
            time = eq_dict["properties"]["time"]
            
            # Convert time to readable date format
            date = pd.to_datetime(time, unit='ms').date()
            
            # Ensure magnitude is always positive
            mag = max(mag, 0.5)  # If mag < 0, set it to 0.5
            
            earthquake_list.append([date, lat, lon, mag, depth, eq_title])
        except (KeyError, TypeError, IndexError) as e:
            print(f"Skipping invalid entry: {e}")

    # Convert to DataFrame
    df = pd.DataFrame(earthquake_list, columns=["Date", "Latitude", "Longitude", "Magnitude", "Depth", "Title"])
    
    # Ensure data is sorted by date for smooth animation
    df = df.sort_values("Date")
    
    return df

# Plot animated earthquake timeline
def plot_earthquake_timeline(df):
    df["Date"] = df["Date"].astype(str)  # Convert Date to string for animation
    
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        size="Magnitude",  # Fixed size issue
        color="Magnitude",
        color_continuous_scale="Turbo",
        
        animation_frame="Date",  # Animate by date
        projection="natural earth",
        title="🌍 Earthquake Timeline Animation (Past 30 Days)",
        hover_name="Title",
        hover_data={"Magnitude": True, "Depth": True},
        
    )

    fig.update_layout(
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        geo=dict(showland=True, landcolor="rgb(217, 217, 217)")
    )

    fig.show()

# Fetch and plot data
data = fetch_earthquake_data()
df = extract_earthquake_data(data)

if not df.empty:
    plot_earthquake_timeline(df)
else:
    print("No valid earthquake data available.")
