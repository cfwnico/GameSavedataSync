# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWlEJFVP.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.cloud_path_label = QLabel(self.centralwidget)
        self.cloud_path_label.setObjectName(u"cloud_path_label")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.cloud_path_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.cloud_path_label)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(64, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(64, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_8)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GameSavedataSync", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u540c\u6b65", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u94fe\u63a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u590d\u94fe\u63a5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u94fe\u63a5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u5217\u8868", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5217\u8868\u6392\u5e8f\u65b9\u5f0f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u6587\u4ef6\u5939\uff1a", None))
        self.cloud_path_label.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u5b58\u6863\u6587\u4ef6\u5939", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u5b58\u6863\u6587\u4ef6\u5939", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"icon", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u540d\u79f0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u72b6\u6001", None))
    # retranslateUi

