# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_R6.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_R6(object):
    def setupUi(self, R6):
        R6.setObjectName("R6")
        R6.resize(713, 311)
        font = QtGui.QFont()
        font.setPointSize(8)
        R6.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/R6.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        R6.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(R6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leR6SpToMatch = QtWidgets.QLineEdit(R6)
        self.leR6SpToMatch.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.leR6SpToMatch.setObjectName("leR6SpToMatch")
        self.horizontalLayout.addWidget(self.leR6SpToMatch)
        self.butR6Match = QtWidgets.QPushButton(R6)
        self.butR6Match.setObjectName("butR6Match")
        self.horizontalLayout.addWidget(self.butR6Match)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbR6Select = QtWidgets.QLabel(R6)
        self.lbR6Select.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbR6Select.sizePolicy().hasHeightForWidth())
        self.lbR6Select.setSizePolicy(sizePolicy)
        self.lbR6Select.setMinimumSize(QtCore.QSize(73, 0))
        self.lbR6Select.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lbR6Select.setObjectName("lbR6Select")
        self.horizontalLayout_2.addWidget(self.lbR6Select)
        self.cmbSpToMap = QtWidgets.QComboBox(R6)
        self.cmbSpToMap.setEnabled(False)
        self.cmbSpToMap.setObjectName("cmbSpToMap")
        self.horizontalLayout_2.addWidget(self.cmbSpToMap)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cbIncSpBelow = QtWidgets.QCheckBox(R6)
        self.cbIncSpBelow.setEnabled(False)
        self.cbIncSpBelow.setObjectName("cbIncSpBelow")
        self.verticalLayout.addWidget(self.cbIncSpBelow)
        spacerItem = QtWidgets.QSpacerItem(20, 177, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.butGetR6Data = QtWidgets.QPushButton(R6)
        self.butGetR6Data.setEnabled(False)
        self.butGetR6Data.setObjectName("butGetR6Data")
        self.horizontalLayout_3.addWidget(self.butGetR6Data)
        self.butCancel = QtWidgets.QPushButton(R6)
        self.butCancel.setObjectName("butCancel")
        self.horizontalLayout_3.addWidget(self.butCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(R6)
        QtCore.QMetaObject.connectSlotsByName(R6)

    def retranslateUi(self, R6):
        _translate = QtCore.QCoreApplication.translate
        R6.setWindowTitle(_translate("R6", "Get Recorder 6 data"))
        self.leR6SpToMatch.setPlaceholderText(_translate("R6", "Enter species search text"))
        self.butR6Match.setText(_translate("R6", "Match taxon name..."))
        self.lbR6Select.setText(_translate("R6", "Select taxon:"))
        self.cbIncSpBelow.setText(_translate("R6", "Include taxa below"))
        self.butGetR6Data.setText(_translate("R6", "Get R6 data"))
        self.butCancel.setText(_translate("R6", "Cancel"))
