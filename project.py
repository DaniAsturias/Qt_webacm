import sys
import numpy as np
import cv2
import os
import pickle
import time
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from imutils.video import VideoStream
from imutils.video import FPS
import imutils

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('webcam.ui', self)

        self.video = self.findChild(QtWidgets.QWidget, 'marco')
        videoPreviewGroupBox = QGroupBox("", self.video)
        self.videoPreviewLabel = QLabel(videoPreviewGroupBox)
        self.videoPreviewLabel.setMinimumSize(QSize(600, 480))

        self.vs = VideoStream(src=0).start()
        self.fps=FPS().start()

        # Definiendo todos los tabs
        self.TabWidget = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
        self.Tab1=self.findChild(QtWidgets.QTabWidget, 'tab1')
        self.Tab2=self.findChild(QtWidgets.QTabWidget, 'tab2')
        self.Tab3=self.findChild(QtWidgets.QTabWidget, 'tab3')

        #Elementos del tab1
        self.check=self.findChild(QtWidgets.QCheckBox, 'checkBox')
        self.check.clicked.connect(self.check_connect)

        self.slider1=self.findChild(QtWidgets.QSlider, 'horizontalSlider')
        self.slider1.setValue(255)
        self.slider1.setVisible(False)
        #self.slider1.clicked.connect(self.getvalue)

        self.slider2=self.findChild(QtWidgets.QSlider, 'horizontalSlider_2')
        self.slider2.setVisible(False)
        #self.slider2.clicked.connect(self.getvalue)

        self.slider3=self.findChild(QtWidgets.QSlider, 'horizontalSlider_3')
        self.slider3.setValue(255)
        self.slider3.setVisible(False)
        #self.slider3.clicked.connect(self.getvalue)

        self.slider4=self.findChild(QtWidgets.QSlider, 'horizontalSlider_4')
        self.slider4.setVisible(False)
        #self.slider4.clicked.connect(self.getvalue)

        self.slider5=self.findChild(QtWidgets.QSlider, 'horizontalSlider_5')
        self.slider5.setValue(255)
        self.slider5.setVisible(False)
        #self.slider5.clicked.connect(self.getvalue)

        self.slider6=self.findChild(QtWidgets.QSlider, 'horizontalSlider_6')
        self.slider6.setVisible(False)
        #self.slider6.clicked.connect(self.getvalue)

        
       

        #Elementos del tab2
        
        self.check3=self.findChild(QtWidgets.QCheckBox, 'checkBox_3')
        self.check4=self.findChild(QtWidgets.QCheckBox, 'checkBox_4')

        #Elementos del tab3
        self.check5=self.findChild(QtWidgets.QCheckBox, 'checkBox_5')
        self.check5.clicked.connect(self.check_connect2)

        self.slider7=self.findChild(QtWidgets.QSlider, 'verticalSlider')
        self.slider7.setValue(255)
        self.slider7.setVisible(False)
        self.slider8=self.findChild(QtWidgets.QSlider, 'verticalSlider_2')
        self.slider8.setVisible(False)

        
        self.timer = QTimer(self.video)
        self.timer.timeout.connect(self.video_proc)  # When timeout is reached, call showCapture
        self.timer.start(40)  # Updates image every 40 milliseconds

        

        self.show()
    def check_connect(self):
    	if self.check.isChecked():
    		self.check5.setChecked(False)
    		self.slider1.setVisible(True)
    		self.slider2.setVisible(True)
    		self.slider3.setVisible(True)
    		self.slider4.setVisible(True)
    		self.slider5.setVisible(True)
    		self.slider6.setVisible(True)
    	else:
    		self.slider1.setVisible(False)
    		self.slider2.setVisible(False)
    		self.slider3.setVisible(False)
    		self.slider4.setVisible(False)
    		self.slider5.setVisible(False)
    		self.slider6.setVisible(False)

    def check_connect2(self):
    	if self.check5.isChecked():
    		self.check.setChecked(False)
    		self.slider7.setVisible(True)
    		self.slider8.setVisible(True)
    	else:
    		self.slider7.setVisible(False)
    		self.slider8.setVisible(False)




    def video_proc(self):
    	frame = self.vs.read()  # Get a picture from the webcam
    	frame = imutils.resize(frame, width=600)
    	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
	
    	if self.check.isChecked():
    		max_filter=np.array([self.slider1.value(),self.slider3.value(),self.slider5.value()])
    		min_filter=np.array([self.slider2.value(),self.slider4.value(),self.slider6.value()])
    		mask = cv2.inRange(frame, min_filter, max_filter)
    		assert isinstance(frame, np.ndarray)  # An image is just a NumPy array
    		frame = cv2.bitwise_and(frame, frame, mask=mask)
    		image = QImage(frame.tobytes(), frame.shape[1],  frame.shape[0], QImage.Format_RGB888)  
	    	self.videoPreviewLabel.setPixmap(QPixmap.fromImage(image))

    	elif self.check5.isChecked():
    		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    		frame = cv2.Canny(frame, self.slider8.value(), self.slider7.value())
    		assert isinstance(frame, np.ndarray)  # An image is just a NumPy array
    		image = QImage(frame.tobytes(), frame.shape[1],  frame.shape[0], QImage.Format_Grayscale8)  
	    	self.videoPreviewLabel.setPixmap(QPixmap.fromImage(image))
            
        
	    
    	else:
	    	assert isinstance(frame, np.ndarray)  # An image is just a NumPy array
	    	image = QImage(frame.tobytes(), frame.shape[1],  frame.shape[0], QImage.Format_RGB888)  
	    	self.videoPreviewLabel.setPixmap(QPixmap.fromImage(image))  # Show the image

    

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
