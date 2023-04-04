import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWebEngineCore as qtweb
import PySide6.QtWebEngineWidgets as qtwebw

import folium

class MapViewFrame(qtw.QFrame):

    def __init__(self,qt_main_window):
        self.qt_main_window = qt_main_window
        qtw.QFrame.__init__(self,qt_main_window)
        self.setParent(qt_main_window)
        self.setFrameStyle(qt_main_window.frame_style)
        self.layout=qtw.QVBoxLayout(qt_main_window)
        self.place_name=qtw.QLabel('navigate')
        self.place_name.setFrameStyle(qt_main_window.frame_style)
        # self.layout.addWidget(self.place_name)
        self.web_view = qtwebw.QWebEngineView()
        self.web_view.setSizePolicy(qtw.QSizePolicy.Policy.Ignored,qtw.QSizePolicy.Policy.Ignored)
        self.start_tile_set=folium.TileLayer('OpenStreetMap',name='OPEN STREET MAP')
        self.web_map = folium.Map(location=[41.1,-70.6],zoom_start=13,tiles=self.start_tile_set)  
        self.web_map.render()     
        self.web_view.setHtml(self.web_map._repr_html_())
        self.layout.addWidget(self.web_view)
        self.setLayout(self.layout)     
    
    def show(self):
        self.web_view.show()    
        qtw.QFrame.show(self)
        
def create_map_view_frame(qt_main_window):
    mvf = MapViewFrame(qt_main_window)
    return mvf