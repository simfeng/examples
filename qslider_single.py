# -*- coding: utf-8 -*-

"""
qslider 单滑块数值显示
"""
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QVBoxLayout,
                             QHBoxLayout, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
            

class QSliderSingle(QWidget):
    def __init__(self, current_value, max_value, min_value):
        super().__init__()
        self.current_value = str(current_value)
        self.max_value = str(max_value)
        self.min_value = str(min_value)
        self.initUI()
        
        
    def initUI(self):
        self.main_box = QVBoxLayout()
        self.current_value_box = QHBoxLayout()
        self.current_value_box.setAlignment(Qt.AlignCenter)
        self.slider_box = QHBoxLayout()

        self.current_value_label = QLabel(self)
        self.current_value_label.setText(self.current_value)

        self.max_value_label = QLabel(self)
        self.max_value_label.setText(self.max_value)
        self.min_value_label = QLabel(self)
        self.min_value_label.setText(self.min_value)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setValue(int(self.current_value))
        self.slider.setMaximum(int(self.max_value))
        self.slider.setMinimum(int(self.min_value))
        self.slider.valueChanged[int].connect(self.changeValue)

        self.current_value_box.addWidget(self.current_value_label)

        self.slider_box.addWidget(self.min_value_label)
        self.slider_box.addWidget(self.slider)
        self.slider_box.addWidget(self.max_value_label)

        self.main_box.addLayout(self.current_value_box)
        self.main_box.addLayout(self.slider_box)


        self.setLayout(self.main_box)
        self.show()

    def changeValue(self, value):
        self.current_value_label.setText(str(value))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = QSliderSingle(20, 99, 0)
    sys.exit(app.exec_())    
