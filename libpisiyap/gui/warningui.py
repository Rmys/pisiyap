# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning.ui'
#
# Created: Fri Jan 28 21:53:27 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QGridLayout, QLabel, QSizePolicy, QHBoxLayout, QSpacerItem, QPushButton

class Warning(QObject):
    def setupUi(self, Warning):
        Warning.setObjectName(self.tr("Warning"))
        Warning.setWindowModality(Qt.WindowModal)
        Warning.resize(540, 137)
        icon = QIcon.fromTheme("pisiyap")
        Warning.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Warning)
        self.label = QLabel(Warning)
        font = QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.warnings = QLabel(Warning)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warnings.sizePolicy().hasHeightForWidth())
        self.warnings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.warnings.setFont(font)
        self.warnings.setTextFormat(Qt.PlainText)
        self.warnings.setScaledContents(True)
        self.warnings.setAlignment(Qt.AlignCenter)
        self.warnings.setWordWrap(True)
        self.gridLayout.addWidget(self.warnings, 1, 0, 1, 1)
        self.label_2 = QLabel(Warning)
        font = QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        spacerItem = QSpacerItem(235, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QPushButton(Warning)
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
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.pushButton.clicked.connect(Warning.close)

        Warning.setWindowTitle(self.tr("PisiYap - Warning: Empty fields..!"))
        self.label.setText(self.tr("Empty Fields:"))
        self.label_2.setText(self.tr("Please, continue after filling in these fields!"))
        self.pushButton.setText(self.tr("Ok"))
