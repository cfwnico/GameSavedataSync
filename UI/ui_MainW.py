# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWHQPnCb.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 576)
        MainWindow.setMinimumSize(QSize(1024, 576))
        MainWindow.setMaximumSize(QSize(1024, 576))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_sync_btn = QPushButton(self.centralwidget)
        self.create_sync_btn.setObjectName(u"create_sync_btn")

        self.horizontalLayout.addWidget(self.create_sync_btn)

        self.fix_sync_btn = QPushButton(self.centralwidget)
        self.fix_sync_btn.setObjectName(u"fix_sync_btn")

        self.horizontalLayout.addWidget(self.fix_sync_btn)

        self.del_sync_btn = QPushButton(self.centralwidget)
        self.del_sync_btn.setObjectName(u"del_sync_btn")

        self.horizontalLayout.addWidget(self.del_sync_btn)

        self.check_sync_btn = QPushButton(self.centralwidget)
        self.check_sync_btn.setObjectName(u"check_sync_btn")

        self.horizontalLayout.addWidget(self.check_sync_btn)

        self.about_btn = QPushButton(self.centralwidget)
        self.about_btn.setObjectName(u"about_btn")

        self.horizontalLayout.addWidget(self.about_btn)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.serach_btn = QPushButton(self.centralwidget)
        self.serach_btn.setObjectName(u"serach_btn")

        self.horizontalLayout_7.addWidget(self.serach_btn)


        self.horizontalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setPointSize(19)
        self.label_6.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.cloud_path_label = QLabel(self.centralwidget)
        self.cloud_path_label.setObjectName(u"cloud_path_label")
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(False)
        self.cloud_path_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.cloud_path_label)

        self.open_cloud_btn = QPushButton(self.centralwidget)
        self.open_cloud_btn.setObjectName(u"open_cloud_btn")
        self.open_cloud_btn.setMaximumSize(QSize(64, 16777215))

        self.horizontalLayout_2.addWidget(self.open_cloud_btn)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(64, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_7.setFont(font2)

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 8, 0, 1, 1)

        self.sync_status_label = QLabel(self.frame)
        self.sync_status_label.setObjectName(u"sync_status_label")
        self.sync_status_label.setFont(font2)
        self.sync_status_label.setScaledContents(True)
        self.sync_status_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.sync_status_label, 3, 1, 1, 1)

        self.savepath_label = QLabel(self.frame)
        self.savepath_label.setObjectName(u"savepath_label")
        self.savepath_label.setFont(font2)
        self.savepath_label.setScaledContents(True)
        self.savepath_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.savepath_label, 6, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 11, 0, 1, 1)

        self.cloudata_path_label = QLabel(self.frame)
        self.cloudata_path_label.setObjectName(u"cloudata_path_label")
        self.cloudata_path_label.setFont(font2)
        self.cloudata_path_label.setScaledContents(True)
        self.cloudata_path_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.cloudata_path_label, 9, 0, 1, 2)

        self.create_time_label = QLabel(self.frame)
        self.create_time_label.setObjectName(u"create_time_label")
        self.create_time_label.setFont(font2)
        self.create_time_label.setScaledContents(True)
        self.create_time_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.create_time_label, 11, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 12, 0, 1, 2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)

        self.icon_label = QLabel(self.frame)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setScaledContents(True)
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.icon_label, 0, 0, 1, 2)

        self.gamename_label = QLabel(self.frame)
        self.gamename_label.setObjectName(u"gamename_label")
        font3 = QFont()
        font3.setPointSize(15)
        self.gamename_label.setFont(font3)
        self.gamename_label.setScaledContents(True)
        self.gamename_label.setAlignment(Qt.AlignCenter)
        self.gamename_label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.gamename_label, 1, 0, 1, 2)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 2)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 7, 0, 1, 2)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 10, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.edit_savedata_btn = QPushButton(self.frame)
        self.edit_savedata_btn.setObjectName(u"edit_savedata_btn")

        self.horizontalLayout_5.addWidget(self.edit_savedata_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.open_cloudata_btn = QPushButton(self.frame)
        self.open_cloudata_btn.setObjectName(u"open_cloudata_btn")

        self.horizontalLayout_6.addWidget(self.open_cloudata_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 8, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)

        self.horizontalLayout_4.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.sync_listwidget = QListWidget(self.centralwidget)
        self.sync_listwidget.setObjectName(u"sync_listwidget")
        self.sync_listwidget.setFont(font3)

        self.gridLayout.addWidget(self.sync_listwidget, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GameSavedataSync", None))
        self.create_sync_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u540c\u6b65", None))
        self.fix_sync_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u590d\u94fe\u63a5", None))
        self.del_sync_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u94fe\u63a5", None))
        self.check_sync_btn.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u6240\u6709\u94fe\u63a5", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.serach_btn.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65\u6587\u4ef6\u5939\uff1a", None))
        self.cloud_path_label.setText(QCoreApplication.translate("MainWindow", u"path", None))
        self.open_cloud_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
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
        self.edit_savedata_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5b58\u6863\u4f4d\u7f6e", None))
        self.open_cloudata_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
    # retranslateUi

