#created and initiated by Pranay Joshi
import pandas as pd
import folium
import os
import branca
m = folium.Map([39.4133, -105.7567], zoom_start=5)
#creating a simple dataframe with the data.csv which is the tableof all the members extracted from the wikki page
main = pd.read_csv("main.csv")
#accessing tooltip
tooltip = 'OSGeo Members'
#using custom OSGeo logo
logoIcon = folium.features.CustomIcon('icon.png', icon_size=(50, 50))
# follium popup does not support new line as it works a/c to html tag so we need to just create a html file 
# so just creating an html file of new line and some intial text using the 'branca' module
html = '''
name:  
'''
html1 ='''
<br>
City: 
'''
html2 = '''
<br>
Country: 
'''
html3 = '''
<br>
contact:
'''
country = 'city, country =   '
contact = 'contact us =   '
folium.CircleMarker(
    location=[42.466470, -70.942110],
    radius=50,
    popup='OSGeo headquarters',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)
for index, row in main.iterrows():
    text = html + row['laboratory'] + html1 + row['city']+ html2 + row['country'] + html3 + row['contact']
    folium.Marker([row['lat'], row['long']],
                  popup = folium.Popup(text, max_width=300,min_width=300)  ,
                  tooltip=tooltip,
                  icon= folium.features.CustomIcon('icon.png', icon_size=(50, 50)),
                 ).add_to(m)
m.save('map.html')