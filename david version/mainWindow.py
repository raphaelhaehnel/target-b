# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
# Created by: PyQt5 UI code generator 5.13.0
# From HUJI Project, by Raphael Haehnel, David Telepnev


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from points import Points
from electromagnet import Electromagnet
from calc_B import Calc_B
from Show_image_3 import Window_image_draw, Window_image
from DrawToPoints import draws_to_points
import arduino_control

import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(657, 314)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(657, 314))
        MainWindow.setMaximumSize(QtCore.QSize(657, 314))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/favicon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("res/favicon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 656, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("res/magnet_left.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("res/magnet_right.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 291, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(430, 40, 211, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("res/logo_huji.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionUpload)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.checkBox.toggled['bool'].connect(self.lineEdit.setEnabled)
        self.checkBox_2.toggled['bool'].connect(self.lineEdit_2.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the menu bar to slots
        self.connectMenubar()

        # Connect the buttons to slots
        self.connectButtons()
        
        # David data :)
        self.three_point_CT = [[], [], []]# = np.zeros((3, 1, 2))# = [[], [], []]
        self.file_path = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Redefine points"))
        self.pushButton_3.setText(_translate("MainWindow", "Display Image"))
        self.pushButton_4.setText(_translate("MainWindow", "COMPUTE"))
        self.label_5.setText(_translate("MainWindow", "I = 0A"))
        self.label_6.setText(_translate("MainWindow", "I = 0A"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.label.setText(_translate("MainWindow", "Magnetic field"))
        self.label_2.setText(_translate("MainWindow", "Time constant"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def connectMenubar(self):
        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.actionNew.triggered.connect(self.slot_New)
        self.actionOpen.triggered.connect(self.slot_Open)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionUpload.triggered.connect(self.slot_Upload)

    def connectButtons(self):
        self.pushButton.clicked.connect(self.slot_UploadImage)
        self.pushButton_2.clicked.connect(self.slot_RedefinePoints)
        self.pushButton_3.clicked.connect(self.slot_DisplayPoints)
        self.pushButton_4.clicked.connect(self.slot_Compute)

    def slot_Upload(self):
        arduino_control.startArduino()

    def slot_New(self):
        """
        Slot connected to the action "New".
        :return: none
        """
        pass

    def slot_Open(self):
        """
        Slot connected to the action "Open".
        :return: none
        """
        path = self.open_file()
        if path:
            print("Open file is here , code ctrl+F: 123444")
            pass

    def slot_UploadImage(self):
        """
        Slot connected to the button "Upload Image".
        :return: none
        """
        path = self.open_file()
        if path:
            pass

    def slot_RedefinePoints(self):
        """
        Slot connected to the button "Redefine Points".
        :return: none
        """
        #self.three_point_CT = [[], [], []] # the data from what the user draw
        self.w = Window_image_draw(self.file_path, self.three_point_CT)
        self.w.show()

    def slot_DisplayPoints(self):
        """
        Slot connected to the button "Display Points".
        :return: none
        """
        #print(self.three_point_CT)
        self.dtp = draws_to_points(self.three_point_CT)
        self.points_from_image = self.dtp.get_points_from_image()
        print(self.points_from_image)
        points = self.points_from_image
        point1 = points[0]
        point2 = points[1] 
        
        if (self.file_path != None):
            #self.w2 = Window_image(self.file_path)
            self.w2 = Window_image(self.w.get_image_label(), point1, point2)
            self.w2.show()

    def slot_Compute(self):
        """
        Slot connected to the button "Compute".
        :return: none
        """
        magnetic_field = self.lineEdit.text()
        time_constant = self.lineEdit_2.text()
        
        try:
            magnetic_field = float(magnetic_field.split()[0])
            print(magnetic_field)
        except:
            print("Bad input, we will get minimum B for I = 1 A")
            magnetic_field = 0
            
        #print(float(magnetic_field.split()[0]), type(magnetic_field), float("123"))
        #print("sdf")
        
        #############################################################################################################################################
        #print("In function 'slot_Compute' we need to update the points 3-4 points from 'three_point_CT'")
        # Need to make a line throw all 3 "objects".
        # 1 data set in three_point_CT: one side of th body. a curve line
        # 2 data set in three_point_CT: circle around the deasis. a circle (closed loop->use a center of mass inside the loop)
        # 3 data set in three_point_CT: second side of the body. a curve line
        #############################################################################################################################################
        points = self.points_from_image
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]
        p4 = points[3]
        all_points = Points(p1, p3, p2, p4) #Points([5,0], [2,0], [-1,0], [-8,0]) # TODO: need to be taken from the image points
        electromagnet_parameters = Electromagnet(170, 0.05, 10**5) # TODO: need to be ac onstant and can be changed from settings tab.
        
        self.calculation_of_B = Calc_B(magnetic_field, all_points, electromagnet_parameters)
        self.calculation_of_B.calculate_B_and_I_coil1()
        self.calculation_of_B.calculate_B_and_I_coil2()
        
        print("Computed B for coil 1:", self.calculation_of_B.get_B_coil1())
        print("Computed I for coil 1:", self.calculation_of_B.get_I_coil1())
        print("Computed B for coil 2:", self.calculation_of_B.get_B_coil2())
        print("Computed I for coil 2:", self.calculation_of_B.get_I_coil2())
        
        _translate = QtCore.QCoreApplication.translate
        
        I1 = f'{self.calculation_of_B.get_I_coil1():.4f}'
        I2 = f'{self.calculation_of_B.get_I_coil2():.4f}'
        self.label_5.setText(_translate("MainWindow", "I = " + str(I1) + "A"))
        self.label_6.setText(_translate("MainWindow", "I = " + str(I2) + "A"))
        #print("Compute", self.lineEdit.text(), self.lineEdit_2.text())

    def open_file(self):
        """
        This function is opening the file explorer and return the path of the chosen file
        :return: the file path
        """
        path = QFileDialog.getOpenFileName(MainWindow, "Open")[0]
        if path:
            self.file_path = path
        return path

    def save(self):
        """
        This function is opening the file explorer to save a file
        :return: none
        """
        if self.file_path is None:
            self.save_as()
        else:
            with open(self.file_path, "w") as f:
                pass

    def save_as(self):
        """
        This function is opening the file explorer to save a file by using the function save()
        :return: none
        """
        path = QFileDialog.getSaveFileName(MainWindow, "Save As")[0]
        if path:
            self.file_path = path
            self.save()

    def show_about_dialog(self):
        """
        Display the 'about' window
        :return: none
        """
        text = "<center>" \
               "<h1>Electromagnet Tool</h1>" \
               "&#8291;" \
               "<img src=res/just_logo.png>" \
               "</center>" \
               "<p>Version 1.0<br/>" \
               "by Raphael Haehnel, David Telepnev<br/>" \
               "&copy; Hebrew University.</p>"
        QMessageBox.about(MainWindow, "About Electromagnet Tool", text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
