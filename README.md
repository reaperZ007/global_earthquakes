
# global_earthquakes
# Global Earthquake Data Visualization with Plotly

This project demonstrates how to fetch, process, and visualize global earthquake data using a JSON API and Plotly. It retrieves earthquake information from a publicly available API (e.g., USGS Earthquake API) and uses Plotly to create interactive visualizations of the data.

## Description

This application retrieves real-time earthquake data from a JSON API.  It fetches data based on specified criteria (e.g., time range, magnitude) and parses the JSON response to extract relevant information such as:

*   Magnitude of the earthquake
*   Location (latitude and longitude)
*   Time of occurrence
*   Depth of the earthquake
*   Other relevant details provided by the API

The retrieved data is then visualized using Plotly, creating interactive plots such as:

*   **Scatter Map:**  Displays earthquake locations on a world map, with marker size and color representing magnitude.
*   **Magnitude vs. Time:** Shows the distribution of earthquake magnitudes over time.
*   **Depth vs. Magnitude:**  Explores the relationship between earthquake depth and magnitude.

This project serves as a practical example of:

*   Making HTTP requests to a RESTful API
*   Handling JSON responses
*   Data processing and manipulation
*   Creating interactive visualizations with Plotly

## Technologies Used

*   Programming Language (Python)
*   Libraries/Modules used( `requests` for Python)
*   JSON handling libraries (`json` in Python)
*   Plotly](https://plotly.com/python/)
