#!/usr/bin/env python3
'''
SunMoon is a Python project using PyQt5 (non commercial) and Astral to show sunrise, sunset, and moon phase.
Author: Tom Bingham
'''

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtCore import Qt, QDate, QDateTime, QTimer
from PyQt5.QtGui import QBrush, QColor, QPen
from astral import Location
from sunmoon_ui import *

import tombo.configfile


class SunMoonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupGraphicsScene()
        self.configuration = tombo.configfile.ConfigFile('sunmoon.conf')
        self.astral = self.configuration.getItems('ASTRAL')
        self.miscellaneous = self.configuration.getItems('MISCELLANEOUS')
        self.location = Location((self.astral['name'], self.astral['region'], float(self.astral['latitude']), float(self.astral['longitude']), self.astral['timezone'], self.astral['elevation']))
        self.minimum_interval = self.miscellaneous['minimum_interval']
        self.timer = QTimer()
        self.setupMethods()
        self.setCurrentDate()
        self.setConfigurationText()
        self.displayedDate = QDateTime(self.ui.deDate.date())
        self.show()

    def setConfigurationText(self):
        config_label_text_color = "#" + self.miscellaneous['config_text_color']
        self.ui.lblLatitude.setText("<font color='" + config_label_text_color + "'>" + self.astral['latitude'] + "</font>")
        self.ui.lblLongitude.setText("<font color='" + config_label_text_color + "'>" + self.astral['longitude'] + "</font>")
        self.ui.lblElevation.setText("<font color='" + config_label_text_color + "'>" + self.astral['elevation'] + "</font>")
        self.ui.lblLocation.setText("<font color='" + config_label_text_color + "'>" + self.astral['name'] + "</font>")
        self.ui.lblRegion.setText("<font color='" + config_label_text_color + "'>" + self.astral['region'] + "</font>")
        self.ui.lblTimeZone.setText("<font color='" + config_label_text_color + "'>" + self.astral['timezone'] + "</font>")

    def setCurrentDate(self):
        self.ui.deDate.setDate(QDate.currentDate())

    def setupGraphicsScene(self):
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(Qt.black)
        self.scene.setSceneRect(0, 0, 209, 169)
        self.ui.gvMoon.setScene(self.scene)
        self.brushWhite = QBrush(QColor(Qt.white))
        self.brushBlack = QBrush(QColor(Qt.black))
        self.pen = QPen(Qt.NoPen)
        self.ellipseWhite = self.scene.addEllipse(50, 30, 100, 100, self.pen, self.brushWhite)
        self.ellipseBlack = self.scene.addEllipse(50, 30, 100, 100, self.pen, self.brushBlack)

    def setupMethods(self):
        self.ui.deDate.dateChanged.connect(self.setTimes)
        self.ui.pbStart.clicked.connect(lambda: self.autoStartStop("start"))
        self.ui.pbStop.clicked.connect(lambda: self.autoStartStop("stop"))
        self.timer.timeout.connect(self.advanceDate)
        self.ui.pbSetCurrentDate.clicked.connect(self.setCurrentDate)

    def autoStartStop(self, action):
        if action == 'start':
            if self.ui.sbInterval.value() == 0:
                self.timer.setInterval(int(self.miscellaneous['minimum_interval']))
            else:
                self.timer.setInterval(self.ui.sbInterval.value() * 1000)
            self.timer.start()
        elif action == 'stop':
            self.timer.stop()

    def advanceDate(self):
        self.displayedDate = self.displayedDate.addDays(1)
        self.ui.deDate.setDate(self.displayedDate.date())

    def setTimes(self):
        date_displayed = self.ui.deDate.date().toPyDate()
        astral_info = self.location.sun(date_displayed)
        self.ui.leSunrise.setText(astral_info['sunrise'].strftime('%I:%M %p'))
        self.ui.leSunset.setText(astral_info['sunset'].strftime('%I:%M %p'))
        self.ui.leDaylight.setText(self.calcDaylight(astral_info['sunset'] - astral_info['sunrise']))
        self.ui.leMoonPhase.setText('Day ' + str(self.location.moon_phase(date_displayed, type(float))))
        self.setMoonPhase(self.location.moon_phase(date_displayed, type(float)))
        #print(self.location.moon_phase(date=None, rtype=type(float)))

    def calcDaylight(self, timedelta):
        return '{} hours, {} minutes'.format(timedelta.seconds // 3600, (timedelta.seconds // 60) % 60)

    def setMoonPhase(self, moon_phase):
        print(moon_phase)
        increment = 100 / 14
        self.scene.removeItem(self.ellipseBlack)

        #if self.day > 28: self.day = 0
        #self.day += 1
        # print(self.day)
        if moon_phase < 15:
            self.ellipseBlack = self.scene.addEllipse((moon_phase * -increment) + 50, 30, 100, 100, self.pen, self.brushBlack)
        else:
            self.ellipseBlack = self.scene.addEllipse(((moon_phase - 28) * -increment) + 50, 30, 100, 100, self.pen, self.brushBlack)
        # self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    smw = SunMoonWindow()
    smw.show()
    sys.exit(app.exec_())
