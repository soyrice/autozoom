# autozoom
Fast and automated zoom toolkit for Folium maps

# Summary
autozoom parses and manages your geoJSON data to make [Folium](python-visualization.github.io/folium/) more convient. For example, autozoom will zoom to a specific state in a map of the US. When the map loads, it will be centered on that state instead of Folium's default extent, which in this case would be the entire country. autozoom calculates the 3D centroid of the spherical polygon created by the maximum bounding triangle of a specified geography. Folium then zooms to extent of bounding polygon and centers the map on the polygon's spherical center of mass.

autozoom is built to work in Folium without additional dependencies, and calculations use only standard libraries. It's based off of [Shapely](https://pypi.python.org/pypi/Shapely), but is designed to be cloned and run within your own projects to reduce dependencies and speed up processing. It offers a set of spherical geometry and and spatial statistics tools that integrate seamlessly into Folium, Leaflet and web mapping workflows. Check out the full set of features and the development progress below.

# Motivation
autozoom grew out of a [series](cyrusmaden.com/hotspots) of data analysis projects for the Rhode Island Division of Planning, where I worked with the Statewide Planning Program to analyze [RIGIS data](rigis.org/data) and identify where suburban sprawl occurred and is likely to accelerate. After the analysis finished, I got fixated on why sprawl was happening in some places (like the southern part of the state) and not others (the north). I aim to use Census [nonemployer statistics](www.census.gov/data/api/available/nonemployer-statistics-and-county-business-patterns.html) to analyze trends in the workforce that accompany or drive sprawl.

# Updates
1/15/17: installed `parse()`. `parse()` works with pandas to manage geoJSON latitude and longitude data when developing a Folium chloropleth. Enter any dataframe to into `parse(df)` to zoom to the geography (e.g., a database of states) specified in the dataframe. Pandas dataframes bind with Folium chloropleths using the sample below.

```python
map_it.choropleth(geo_path = geo_path,
                 data = df,
                 columns = ['code', 'value'],
                 key_on = 'feature.properties.STATE',
                 fill_color = 'PuRd',
                 fill_opacity = 0.9,
                 line_opacity = 0.2)
```

1/24/17: started `center()`. `center()` finds the spherical centroid of data entered into `parse()`. `center()` makes it easy for Folium to center a map on a geoJSON file, or on a sub-section of geoJSON data specified with a pandas dataframe.

Next: test and update center(); install `manager()`, a system to connects various functions, such as `parse()` and `center()`, in a user-friendly interface you can call in your web mapping workflow.
