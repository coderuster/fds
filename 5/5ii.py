import plotly.express as px 
cities = ['London', 'New York', 'Tokyo', 'Sydney', 'Cairo']
latitudes = [51.5074, 40.7128, 35.6762, -33.8688, 30.0444]
longitudes = [-0.1278, -74.0060, 139.6503, 151.2093, 31.2357]

city_data = pd.DataFrame({
    'City': cities,
    'Latitude': latitudes,
    'Longitude': longitudes
})

fig = px.scatter_geo(city_data, lat='Latitude', lon='Longitude', hover_name='City',projection="natural earth", title="Major Cities for Tourism Promotion")

fig.show()
