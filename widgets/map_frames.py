import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWebEngineCore as qtweb
import PySide6.QtWebEngineWidgets as qtwebw

import folium

import json
from urllib.request import urlopen
import os
  
class MapViewFrame(qtw.QFrame):

    def __init__(self,qt_main_window):
        self.qt_main_window = qt_main_window
        qtw.QFrame.__init__(self,qt_main_window)
        self.setParent(qt_main_window)
        self.setFrameStyle(qt_main_window.frame_style)
        self.layout=qtw.QVBoxLayout(qt_main_window)
        self.layout.setObjectName('map_view_frame_layout')

        self.web_view = qtwebw.QWebEngineView()
        self.web_view.setSizePolicy(qtw.QSizePolicy.Policy.Ignored,qtw.QSizePolicy.Policy.Ignored)
        self.init_base_layers()
        self.init_data_layers()
        self.web_map = folium.Map(location=[41.533,-70.683],zoom_start=15,tiles=self.base_layer['dark'])
        self.web_map.get_root().html.add_child(folium.JavascriptLink('./scripts/map_addons.js'))
        self.web_map.get_root().html.add_child(folium.CssLink('./styles/map_style.css'))
        for name in self.base_layer:
            if name != "dark":
                self.base_layer[name].add_to(self.web_map)
        for name in self.data_layer:
            self.data_layer[name].add_to(self.web_map)        
        folium.LayerControl().add_to(self.web_map) 
            
        self.web_view.setHtml(self.web_map.get_root().render())
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)     

    def show(self):
        self.web_view.show()    
        qtw.QFrame.show(self)
        
    def init_base_layers(self):
        self.base_layer = {}
        self.base_layer['dark']=folium.TileLayer(tiles='https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB Dark Matter',  
            attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
        self.base_layer['voyager']=folium.TileLayer(tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',name='CartoDB Voyager',
            attr= '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
        self.base_layer['posi']=folium.TileLayer(tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',name='CartoDB Positron',
	        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
        self.base_layer['osm']=folium.TileLayer(tiles='OpenStreetMap',name='Open Street Map')
        self.base_layer['usgs']=folium.TileLayer(tiles='https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}', name="USGS Imagery",
	        attr= 'Tiles courtesy of the <a href="https://usgs.gov/">U.S. Geological Survey</a>')
        self.base_layer['esri'] = folium.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', name="ESRI Imagery",
	        attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community')
        self.base_layer['massgis']=folium.TileLayer(tiles="https://tiles.arcgis.com/tiles/hGdibHYSPO59RG1h/arcgis/rest/services/MassGISBasemap/MapServer/WMTS/tile/1.0.0/MassGISBasemap/default/default028mm/{z}/{y}/{x}.png", name='Mass GIS Base',
            attr='Tiles courtesy of <a href="https://www.mass.gov/service-details/massgis-base-map">MassGIS</a>')

    def init_data_layers(self):
        self.data_layer = {}
        # FIXME: adding these blanks the map
        #self.data_layer['grat5']=folium.GeoJson('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_graticules_5.geojson',name = 'Grid 5')
        #self.data_layer['countries']=folium.GeoJson("http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson", name='Country borders')
        self.data_layer['whoi']=folium.GeoJson(os.path.join('geojson','woods_hole.json'))




def create_map_view_frame(qt_main_window):
    mvf = MapViewFrame(qt_main_window)
    return mvf