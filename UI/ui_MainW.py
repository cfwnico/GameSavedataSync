# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWwxDVaJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setMinimumSize(QSize(1024, 576))
        MainWindow.setMaximumSize(QSize(1024, 576))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.sync_listwidget = QListWidget(self.centralwidget)
        self.sync_listwidget.setObjectName(u"sync_listwidget")
        font = QFont()
        font.setPointSize(15)
        self.sync_listwidget.setFont(font)

        self.verticalLayout.addWidget(self.sync_listwidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.sync_status_label = QLabel(self.centralwidget)
        self.sync_status_label.setObjectName(u"sync_status_label")
        self.sync_status_label.setFont(font1)

        self.gridLayout.addWidget(self.sync_status_label, 3, 1, 1, 1)

        self.savepath_label = QLabel(self.centralwidget)
        self.savepath_label.setObjectName(u"savepath_label")
        self.savepath_label.setMinimumSize(QSize(0, 50))
        self.savepath_label.setFont(font1)
        self.savepath_label.setWordWrap(True)

        self.gridLayout.addWidget(self.savepath_label, 6, 0, 1, 2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 11, 0, 1, 1)

        self.cloudata_path_label = QLabel(self.centralwidget)
        self.cloudata_path_label.setObjectName(u"cloudata_path_label")
        self.cloudata_path_label.setMinimumSize(QSize(0, 50))
        self.cloudata_path_label.setFont(font1)
        self.cloudata_path_label.setWordWrap(True)

        self.gridLayout.addWidget(self.cloudata_path_label, 9, 0, 1, 2)

        self.create_time_label = QLabel(self.centralwidget)
        self.create_time_label.setObjectName(u"create_time_label")
        self.create_time_label.setFont(font1)

        self.gridLayout.addWidget(self.create_time_label, 11, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 12, 0, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.icon_label = QLabel(self.centralwidget)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_label, 0, 0, 1, 2)

        self.gamename_label = QLabel(self.centralwidget)
        self.gamename_label.setObjectName(u"gamename_label")
        self.gamename_label.setMinimumSize(QSize(300, 0))
        self.gamename_label.setMaximumSize(QSize(300, 16777215))
        self.gamename_label.setFont(font)
        self.gamename_label.setAlignment(Qt.AlignCenter)
        self.gamename_label.setWordWrap(True)

        self.gridLayout.addWidget(self.gamename_label, 1, 0, 1, 2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 2)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 10, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.open_cloudata_btn = QPushButton(self.centralwidget)
        self.open_cloudata_btn.setObjectName(u"open_cloudata_btn")

        self.horizontalLayout_5.addWidget(self.open_cloudata_btn)


        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)

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
        font2 = QFont()
        font2.setPointSize(19)
        self.label_6.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.cloud_path_label = QLabel(self.centralwidget)
        self.cloud_path_label.setObjectName(u"cloud_path_label")
        font3 = QFont()
        font3.setPointSize(19)
        font3.setBold(False)
        self.cloud_path_label.setFont(font3)

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

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GameSavedataSync", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u65f6\u95f4", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u540d\u79f0", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u65f6\u95f4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u72b6\u6001\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u5b58\u6863\u6587\u4ef6\u5939\uff1a", None))
        self.sync_status_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.savepath_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u5b58\u6863\u6587\u4ef6\u5939\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u65e5\u671f\uff1a", None))
        self.cloudata_path_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.create_time_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_label.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u56fe\u6807", None))
        self.gamename_label.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u540d\u79f0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5b58\u6863\u4f4d\u7f6e", None))
        self.open_cloudata_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u540c\u6b65", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u94fe\u63a5", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u590d\u94fe\u63a5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u94fe\u63a5", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u5217\u8868", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u6587\u4ef6\u5939\uff1a", None))
        self.cloud_path_label.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
    # retranslateUi

