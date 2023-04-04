
from cmath import nan
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import date, time, datetime, timedelta
import json
from dateutil import parser
import math
import sys
import os

import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
import PySide6.QtWebEngineCore as qtweb

import core.map_node as map_node
import widgets.qt_central_widget as central_widget
import widgets.qt_left_toolbar as left_toolbar   
import styles.qt_style_sheet as qt_style_sheet
import core.keyboard_shortcuts as keyboard_shortcuts

class MappyMap(qtw.QMainWindow):
    
    def __init__(self):
        self.app = qtw.QApplication(sys.argv)
        qtw.QMainWindow.__init__(self) 
        self.title = "MapMap"
        self.description = "Simple Map for ROS"
        self.version_str = "0.3.3" 
        self.copyright_str = "(c) copyright 2023, Matthew Grund"
        self.screen = self.app.primaryScreen()
        self.screen_size =  self.screen.size()
        self.setWindowTitle(self.title)
        self.resize(int(self.screen_size.width()*0.80),int(self.screen_size.height()*0.80))
        self.app.setStyleSheet(qt_style_sheet.qss)
        self.frame_style = qtw.QFrame.Shape.Panel  # .Panel for designing, .NoFrame for a clean look    

        self.setup_central_widget()
        self.setup_left_toolbar()
        keyboard_shortcuts.setup(self)
 

    def setup_left_toolbar(self):
        self.left_toolbar = left_toolbar.QTLeftToolBar(self)    


    def setup_central_widget(self):
        central_widget.configure(self)
        central_widget.setup(self)
  
  
    def home_page(self):
        self.stack.setCurrentIndex(0)   
        
        
    def menu_callback(self,parent_name, action_name):   
        print("Menu" + parent_name + ":" + action_name)
        self.statusBar().showMessage(parent_name + ":" + action_name)
        self.stack.setCurrentIndex(self.frame_dict[parent_name][action_name]['index'])


    def max_min(self):          
        if self.isFullScreen():
            # self.setWindowFlags(self._flags)
            self.showNormal()
        else:
            self._flags = self.windowFlags()
            # self.setWindowFlags(qtc.Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
            self.showFullScreen() 


################################################
#
#  Start the QT app, which starts the ROS node
#
################################################        
def main(args=None):
    # rclpy.init(args=args)
    map = MappyMap()
    map.show()
    ret=map.app.exec()
    # rclpy.shutdown()
    # map.ros_node.destroy_node()
    sys.exit(ret)

if __name__ == '__main__':
    main()        
