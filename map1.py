import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
nombre = list(data["NAME"])
elevacao = list(data["ELEV"])

map = folium.Map(location= [latitude[30], longitude[30]], zoom_start= 6)

fg = folium.FeatureGroup(name="My Map")

for lat, lon, el, nm in zip(latitude, longitude, elevacao, nombre):
    fg.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup("Vulcao: "+str(nm)+"----"+"Elev: "+str(el)+"mts", parse_html = 'true'),  icon = folium.Icon(color='green')))

map.add_child(fg)

map.save("Vulcoes Americanos.html")
