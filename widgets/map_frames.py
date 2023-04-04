import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWebEngineCore as qtweb
import PySide6.QtWebEngineWidgets as qtwebw

import folium

class MapViewFrame(qtw.QFrame):

    def __init__(self,qt_main_window):
        self.qt_main_window = qt_main_window
        qtw.QFrame.__init__(self)
        self.setParent(qt_main_window)
        self.setFrameStyle(qt_main_window.frame_style)
        self.layout=qtw.QVBoxLayout(qt_main_window)
        self.web_view = qtwebw.QWebEngineView()
        self.layout.addWidget(self.web_view)
        self.start_tile_set=folium.TileLayer('OpenStreetMap',name='OPEN STREET MAP')
        self.web_map = folium.Map(location=[42.1,-70.3],zoom_start=13,tiles=self.start_tile_set)  
        self.web_map.render()     
        self.web_view.setHtml(self.web_map._repr_html_())
        #self.web_view.show()
        #self.show()
        
def create_map_view_frame(qt_main_window):
    mvf = MapViewFrame(qt_main_window)
    return mvf