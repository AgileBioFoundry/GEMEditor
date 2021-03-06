# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PubmedWebBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PubmedBrowser(object):
    def setupUi(self, PubmedBrowser):
        PubmedBrowser.setObjectName("PubmedBrowser")
        PubmedBrowser.resize(916, 754)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PubmedBrowser.sizePolicy().hasHeightForWidth())
        PubmedBrowser.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(PubmedBrowser)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonPrevious = QtWidgets.QPushButton(PubmedBrowser)
        self.buttonPrevious.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/left_arrow_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPrevious.setIcon(icon)
        self.buttonPrevious.setIconSize(QtCore.QSize(20, 20))
        self.buttonPrevious.setObjectName("buttonPrevious")
        self.horizontalLayout_2.addWidget(self.buttonPrevious)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchBox = QtWidgets.QGroupBox(PubmedBrowser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBox.sizePolicy().hasHeightForWidth())
        self.searchBox.setSizePolicy(sizePolicy)
        self.searchBox.setObjectName("searchBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.searchBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchInput = QtWidgets.QLineEdit(self.searchBox)
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout.addWidget(self.searchInput)
        self.buttonSearch = QtWidgets.QPushButton(self.searchBox)
        self.buttonSearch.setEnabled(False)
        self.buttonSearch.setObjectName("buttonSearch")
        self.horizontalLayout.addWidget(self.buttonSearch)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.searchBox)
        self.resultsBox = QtWidgets.QGroupBox(PubmedBrowser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsBox.sizePolicy().hasHeightForWidth())
        self.resultsBox.setSizePolicy(sizePolicy)
        self.resultsBox.setObjectName("resultsBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.resultsBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.numCurrent = QtWidgets.QLabel(self.resultsBox)
        self.numCurrent.setObjectName("numCurrent")
        self.horizontalLayout_3.addWidget(self.numCurrent)
        self.ofLabel = QtWidgets.QLabel(self.resultsBox)
        self.ofLabel.setObjectName("ofLabel")
        self.horizontalLayout_3.addWidget(self.ofLabel)
        self.numTotal = QtWidgets.QLabel(self.resultsBox)
        self.numTotal.setObjectName("numTotal")
        self.horizontalLayout_3.addWidget(self.numTotal)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.skipKnowns = QtWidgets.QCheckBox(self.resultsBox)
        self.skipKnowns.setChecked(True)
        self.skipKnowns.setObjectName("skipKnowns")
        self.horizontalLayout_3.addWidget(self.skipKnowns)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonLoadKnowns = QtWidgets.QPushButton(self.resultsBox)
        self.buttonLoadKnowns.setObjectName("buttonLoadKnowns")
        self.horizontalLayout_3.addWidget(self.buttonLoadKnowns)
        self.buttonSaveKnowns = QtWidgets.QPushButton(self.resultsBox)
        self.buttonSaveKnowns.setObjectName("buttonSaveKnowns")
        self.horizontalLayout_3.addWidget(self.buttonSaveKnowns)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.buttonAdd = QtWidgets.QPushButton(self.resultsBox)
        self.buttonAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAdd.setIcon(icon1)
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout_3.addWidget(self.buttonAdd)
        self.buttonNonAdd = QtWidgets.QPushButton(self.resultsBox)
        self.buttonNonAdd.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/no_download_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNonAdd.setIcon(icon2)
        self.buttonNonAdd.setObjectName("buttonNonAdd")
        self.horizontalLayout_3.addWidget(self.buttonNonAdd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.webView = QtWebEngineWidgets.QWebEngineView(self.resultsBox)
        self.webView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setProperty("url", QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout_2.addWidget(self.webView)
        self.progressBar = QtWidgets.QProgressBar(self.resultsBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.resultsBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.buttonNext = QtWidgets.QPushButton(PubmedBrowser)
        self.buttonNext.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/right_arrow_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(icon3)
        self.buttonNext.setIconSize(QtCore.QSize(20, 20))
        self.buttonNext.setObjectName("buttonNext")
        self.horizontalLayout_2.addWidget(self.buttonNext)

        self.retranslateUi(PubmedBrowser)
        self.buttonSearch.clicked.connect(PubmedBrowser.search_pubmed)
        self.buttonNext.clicked.connect(PubmedBrowser.next_entry)
        self.buttonPrevious.clicked.connect(PubmedBrowser.previous_entry)
        self.searchInput.returnPressed.connect(PubmedBrowser.search_pubmed)
        self.webView.loadStarted.connect(PubmedBrowser.show_progressbar)
        self.webView.loadFinished['bool'].connect(PubmedBrowser.hide_progressbar)
        self.buttonAdd.clicked.connect(PubmedBrowser.add_publication)
        self.buttonNonAdd.clicked.connect(PubmedBrowser.push_publication_to_nonread)
        self.searchInput.textChanged['QString'].connect(PubmedBrowser.toggle_search_button)
        self.buttonLoadKnowns.clicked.connect(PubmedBrowser.load_knowns)
        self.buttonSaveKnowns.clicked.connect(PubmedBrowser.save_knowns)
        QtCore.QMetaObject.connectSlotsByName(PubmedBrowser)

    def retranslateUi(self, PubmedBrowser):
        _translate = QtCore.QCoreApplication.translate
        PubmedBrowser.setWindowTitle(_translate("PubmedBrowser", "Pubmed Browser"))
        self.searchBox.setTitle(_translate("PubmedBrowser", "Search"))
        self.buttonSearch.setText(_translate("PubmedBrowser", "Go"))
        self.resultsBox.setTitle(_translate("PubmedBrowser", "Results"))
        self.numCurrent.setText(_translate("PubmedBrowser", "currentNum"))
        self.ofLabel.setText(_translate("PubmedBrowser", "of"))
        self.numTotal.setText(_translate("PubmedBrowser", "totalNum"))
        self.skipKnowns.setText(_translate("PubmedBrowser", "Skip knowns"))
        self.buttonLoadKnowns.setText(_translate("PubmedBrowser", "Load visited"))
        self.buttonSaveKnowns.setText(_translate("PubmedBrowser", "Save visited"))

from PyQt5 import QtWebEngineWidgets
from GEMEditor.icons_rc import *
