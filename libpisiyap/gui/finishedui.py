# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finished.ui'
#
# Created: Fri Jan 28 21:53:18 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QGridLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QPushButton


class FinishDialog(QObject):
    def setupUi(self, FinishDialog):
        FinishDialog.setWindowModality(Qt.WindowModal)
        FinishDialog.resize(285, 85)
        icon = QIcon.fromTheme("pisiyap")
        FinishDialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(FinishDialog)
        self.label = QLabel(FinishDialog)
        font = QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        spacerItem = QSpacerItem(235, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QPushButton(FinishDialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon1 = QIcon.fromTheme("dialog-ok")
        self.pushButton.setIcon(icon1)
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QSpacerItem(232, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.pushButton.clicked.connect(FinishDialog.close)

        FinishDialog.setWindowTitle(self.tr("PiSiYap - Finished!"))
        self.label.setText(self.tr("PiSi source files successfully created."))
        self.pushButton.setText(self.tr("Ok"))
