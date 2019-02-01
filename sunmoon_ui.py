# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sunmoon.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.twMain = QtWidgets.QTabWidget(self.centralwidget)
        self.twMain.setGeometry(QtCore.QRect(0, 0, 511, 401))
        self.twMain.setObjectName("twMain")
        self.tabSunMoon = QtWidgets.QWidget()
        self.tabSunMoon.setObjectName("tabSunMoon")
        self.pbStart = QtWidgets.QPushButton(self.tabSunMoon)
        self.pbStart.setGeometry(QtCore.QRect(280, 280, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbStart.setFont(font)
        self.pbStart.setObjectName("pbStart")
        self.lblElevation = QtWidgets.QLabel(self.tabSunMoon)
        self.lblElevation.setGeometry(QtCore.QRect(340, 80, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblElevation.setFont(font)
        self.lblElevation.setObjectName("lblElevation")
        self.label_4 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_4.setGeometry(QtCore.QRect(30, 14, 82, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pbStop = QtWidgets.QPushButton(self.tabSunMoon)
        self.pbStop.setGeometry(QtCore.QRect(390, 280, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbStop.setFont(font)
        self.pbStop.setObjectName("pbStop")
        self.pushButton = QtWidgets.QPushButton(self.tabSunMoon)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.leSunset = QtWidgets.QLineEdit(self.tabSunMoon)
        self.leSunset.setGeometry(QtCore.QRect(120, 70, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leSunset.setFont(font)
        self.leSunset.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leSunset.setReadOnly(True)
        self.leSunset.setObjectName("leSunset")
        self.lblRegion = QtWidgets.QLabel(self.tabSunMoon)
        self.lblRegion.setGeometry(QtCore.QRect(340, 120, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblRegion.setFont(font)
        self.lblRegion.setObjectName("lblRegion")
        self.deDate = QtWidgets.QDateEdit(self.tabSunMoon)
        self.deDate.setGeometry(QtCore.QRect(120, 10, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deDate.setFont(font)
        self.deDate.setObjectName("deDate")
        self.gvMoon = QtWidgets.QGraphicsView(self.tabSunMoon)
        self.gvMoon.setGeometry(QtCore.QRect(40, 170, 211, 171))
        self.gvMoon.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gvMoon.setInteractive(False)
        self.gvMoon.setObjectName("gvMoon")
        self.label_7 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_7.setGeometry(QtCore.QRect(270, 40, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_12.setGeometry(QtCore.QRect(270, 120, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_3 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_3.setGeometry(QtCore.QRect(30, 103, 82, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lblTimeZone = QtWidgets.QLabel(self.tabSunMoon)
        self.lblTimeZone.setGeometry(QtCore.QRect(340, 140, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTimeZone.setFont(font)
        self.lblTimeZone.setObjectName("lblTimeZone")
        self.lblLongitude = QtWidgets.QLabel(self.tabSunMoon)
        self.lblLongitude.setGeometry(QtCore.QRect(340, 60, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLongitude.setFont(font)
        self.lblLongitude.setObjectName("lblLongitude")
        self.label_6 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_6.setGeometry(QtCore.QRect(320, 244, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_9.setGeometry(QtCore.QRect(270, 80, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 82, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_8.setGeometry(QtCore.QRect(270, 60, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_11.setGeometry(QtCore.QRect(270, 100, 60, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.leDaylight = QtWidgets.QLineEdit(self.tabSunMoon)
        self.leDaylight.setGeometry(QtCore.QRect(120, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leDaylight.setFont(font)
        self.leDaylight.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leDaylight.setReadOnly(True)
        self.leDaylight.setObjectName("leDaylight")
        self.leMoonPhase = QtWidgets.QLineEdit(self.tabSunMoon)
        self.leMoonPhase.setGeometry(QtCore.QRect(120, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leMoonPhase.setFont(font)
        self.leMoonPhase.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leMoonPhase.setReadOnly(True)
        self.leMoonPhase.setObjectName("leMoonPhase")
        self.lblLocation = QtWidgets.QLabel(self.tabSunMoon)
        self.lblLocation.setGeometry(QtCore.QRect(340, 100, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLocation.setFont(font)
        self.lblLocation.setObjectName("lblLocation")
        self.pbSetCurrentDate = QtWidgets.QPushButton(self.tabSunMoon)
        self.pbSetCurrentDate.setGeometry(QtCore.QRect(280, 10, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbSetCurrentDate.setFont(font)
        self.pbSetCurrentDate.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pbSetCurrentDate.setObjectName("pbSetCurrentDate")
        self.label_2 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_2.setGeometry(QtCore.QRect(30, 73, 82, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.leSunrise = QtWidgets.QLineEdit(self.tabSunMoon)
        self.leSunrise.setEnabled(True)
        self.leSunrise.setGeometry(QtCore.QRect(120, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leSunrise.setFont(font)
        self.leSunrise.setFocusPolicy(QtCore.Qt.NoFocus)
        self.leSunrise.setReadOnly(True)
        self.leSunrise.setObjectName("leSunrise")
        self.label_10 = QtWidgets.QLabel(self.tabSunMoon)
        self.label_10.setGeometry(QtCore.QRect(260, 140, 71, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lblLatitude = QtWidgets.QLabel(self.tabSunMoon)
        self.lblLatitude.setGeometry(QtCore.QRect(340, 40, 100, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLatitude.setFont(font)
        self.lblLatitude.setObjectName("lblLatitude")
        self.label = QtWidgets.QLabel(self.tabSunMoon)
        self.label.setGeometry(QtCore.QRect(30, 43, 82, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.sbInterval = QtWidgets.QSpinBox(self.tabSunMoon)
        self.sbInterval.setGeometry(QtCore.QRect(370, 240, 42, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sbInterval.setFont(font)
        self.sbInterval.setMaximum(60)
        self.sbInterval.setObjectName("sbInterval")
        self.twMain.addTab(self.tabSunMoon, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.label_13 = QtWidgets.QLabel(self.tabConfig)
        self.label_13.setGeometry(QtCore.QRect(30, 20, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tabConfig)
        self.label_14.setGeometry(QtCore.QRect(30, 60, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tabConfig)
        self.label_15.setGeometry(QtCore.QRect(30, 140, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tabConfig)
        self.label_16.setGeometry(QtCore.QRect(30, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tabConfig)
        self.label_17.setGeometry(QtCore.QRect(30, 220, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tabConfig)
        self.label_18.setGeometry(QtCore.QRect(30, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tabConfig)
        self.label_19.setGeometry(QtCore.QRect(10, 300, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tabConfig)
        self.label_20.setGeometry(QtCore.QRect(30, 260, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.leLatitude = QtWidgets.QLineEdit(self.tabConfig)
        self.leLatitude.setGeometry(QtCore.QRect(170, 20, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLatitude.setFont(font)
        self.leLatitude.setObjectName("leLatitude")
        self.leLongitude = QtWidgets.QLineEdit(self.tabConfig)
        self.leLongitude.setGeometry(QtCore.QRect(170, 60, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLongitude.setFont(font)
        self.leLongitude.setObjectName("leLongitude")
        self.leElevation = QtWidgets.QLineEdit(self.tabConfig)
        self.leElevation.setGeometry(QtCore.QRect(170, 100, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leElevation.setFont(font)
        self.leElevation.setObjectName("leElevation")
        self.leTimeZone = QtWidgets.QLineEdit(self.tabConfig)
        self.leTimeZone.setGeometry(QtCore.QRect(170, 140, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leTimeZone.setFont(font)
        self.leTimeZone.setObjectName("leTimeZone")
        self.leLocation = QtWidgets.QLineEdit(self.tabConfig)
        self.leLocation.setGeometry(QtCore.QRect(170, 180, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLocation.setFont(font)
        self.leLocation.setObjectName("leLocation")
        self.leCountry = QtWidgets.QLineEdit(self.tabConfig)
        self.leCountry.setGeometry(QtCore.QRect(170, 220, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCountry.setFont(font)
        self.leCountry.setObjectName("leCountry")
        self.leMinimumInterval = QtWidgets.QLineEdit(self.tabConfig)
        self.leMinimumInterval.setGeometry(QtCore.QRect(170, 260, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leMinimumInterval.setFont(font)
        self.leMinimumInterval.setObjectName("leMinimumInterval")
        self.leTextColor = QtWidgets.QLineEdit(self.tabConfig)
        self.leTextColor.setGeometry(QtCore.QRect(170, 300, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leTextColor.setFont(font)
        self.leTextColor.setObjectName("leTextColor")
        self.pbSave = QtWidgets.QPushButton(self.tabConfig)
        self.pbSave.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.pbSave.setObjectName("pbSave")
        self.pbDiscard = QtWidgets.QPushButton(self.tabConfig)
        self.pbDiscard.setGeometry(QtCore.QRect(240, 340, 75, 23))
        self.pbDiscard.setObjectName("pbDiscard")
        self.pbClear = QtWidgets.QPushButton(self.tabConfig)
        self.pbClear.setGeometry(QtCore.QRect(320, 340, 75, 23))
        self.pbClear.setObjectName("pbClear")
        self.twMain.addTab(self.tabConfig, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.twMain.setCurrentIndex(1)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbStart.setText(_translate("MainWindow", "&Start"))
        self.lblElevation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Date:"))
        self.pbStop.setText(_translate("MainWindow", "S&top"))
        self.pushButton.setText(_translate("MainWindow", "&Quit"))
        self.leSunset.setText(_translate("MainWindow", "4:17 PM PST"))
        self.lblRegion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Latitude:"))
        self.label_12.setText(_translate("MainWindow", "Region:"))
        self.label_3.setText(_translate("MainWindow", "Daylight:"))
        self.lblTimeZone.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.lblLongitude.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Interval:"))
        self.label_9.setText(_translate("MainWindow", "Elevation:"))
        self.label_5.setText(_translate("MainWindow", "Moon Phase:"))
        self.label_8.setText(_translate("MainWindow", "Longitude:"))
        self.label_11.setText(_translate("MainWindow", "Location:"))
        self.leDaylight.setText(_translate("MainWindow", "8 hours, 45 minutes"))
        self.leMoonPhase.setText(_translate("MainWindow", "Day 23"))
        self.lblLocation.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.pbSetCurrentDate.setText(_translate("MainWindow", "&Current Date"))
        self.label_2.setText(_translate("MainWindow", "Sunset:"))
        self.leSunrise.setText(_translate("MainWindow", "7:27 AM PST"))
        self.label_10.setText(_translate("MainWindow", "Time Zone:"))
        self.lblLatitude.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\"><br/></span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Sunrise:"))
        self.twMain.setTabText(self.twMain.indexOf(self.tabSunMoon), _translate("MainWindow", "SunMoon"))
        self.label_13.setText(_translate("MainWindow", "Latutude:"))
        self.label_14.setText(_translate("MainWindow", "Longitude:"))
        self.label_15.setText(_translate("MainWindow", "Time Zone:"))
        self.label_16.setText(_translate("MainWindow", "Elevation (meters):"))
        self.label_17.setText(_translate("MainWindow", "Country:"))
        self.label_18.setText(_translate("MainWindow", "Location:"))
        self.label_19.setText(_translate("MainWindow", "Configuration Text Color:"))
        self.label_20.setText(_translate("MainWindow", "Minimum Interval:"))
        self.pbSave.setText(_translate("MainWindow", "S&ave"))
        self.pbDiscard.setText(_translate("MainWindow", "&Discard"))
        self.pbClear.setText(_translate("MainWindow", "&Clear"))
        self.twMain.setTabText(self.twMain.indexOf(self.tabConfig), _translate("MainWindow", "Configuration"))

