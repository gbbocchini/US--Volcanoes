import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
nombre = list(data["NAME"])
elevacao = list(data["ELEV"])

map = folium.Map(location= [latitude[30], longitude[30]], zoom_start= 6)

def cor_icone(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
    

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, el, nm in zip(latitude, longitude, elevacao, nombre):
    fgv.add_child(folium.CircleMarker(location = [lat, lon], popup = folium.Popup("Vulcao: "+str(nm)+"----"+"Elev: "+str(el)+"mts", parse_html = 'true'), fill ='true',
    fill_color = cor_icone(el), color = 'grey', fill_opacity = 0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding ='utf-8-sig').read(), style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Vulcoes Americanos.html")
